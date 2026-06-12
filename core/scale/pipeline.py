"""新泛化 Pipeline：种子题目 → Fact Sheet → LLM 编题 → 度规替换 → 形式变换 → 软改写 → 去重

每个 Phase 是独立可调用的函数，接收/返回统一格式 (problems, fact_sheets):
  problems:     list of Problem 对象
  fact_sheets:  dict mapping seq → fact_sheet dict

拼装方式：
  p, fs, lb = phase_cognitive_fanout(seed_dict, forms=["derivation", "numerical", ...])
  p, fs, lb = phase_metric_substitute(p, lb, fs, seed_tags, num_subs=3)
  p, fs, lb = phase_form_change(p, lb, fs, target_forms=["multiple_choice", "code", "conceptual"])
  p, fs, lb = phase_soft_rewrite(p, lb, fs, num_soft=2)
  p     = phase_batch_validate(p, lb, output_dir)
  p     = phase_ngram_dedup(p)

或一键运行：
  p = fan_through(seed_json_path, forms=["derivation", ...], num_subs=3, num_soft=2)
"""

import json
import re
import time
from dataclasses import asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from core.common.api_client import ask_ai, get_llm_stats
from core.common.cleaner import clean_problem
from core.common.config import MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC
from core.common.metric_library import METRIC_LIBRARY
from core.common.stats import PhaseStats, PipelineResult, Timer, compute_diversity_from_problems
from core.common.sympy_engine import compute_fact_sheet
from core.common.fact_sheet_cache import get_cached_fact_sheet
from core.scale.prompts import (
    SYSTEM_PROMPT_COMPOSE, SYSTEM_PROMPT_SUBSTITUTE, SYSTEM_PROMPT_PICK_METRIC,
    SYSTEM_PROMPT_CONTRAST, SYSTEM_PROMPT_VERIFY, SYSTEM_PROMPT_DESIGN, SYSTEM_PROMPT_REDUCE,
    SYSTEM_PROMPT_FORM_CHANGE,
    GENERALIZATION_AXES,
)
from core.verify.validator import validate_and_fix_loop
from schema import Problem, Metadata, PhysicalData, Origin, TYPE_TO_COGNITIVE, COGNITIVE_TO_TYPE

# 度规库描述
_METRIC_DESCRIPTIONS = {
    # 非 heavy 度规
    "Schwarzschild": "静态球对称黑洞度规，真空解，Einstein 张量为零",
    "Minkowski": "平直时空度规（笛卡尔坐标），所有曲率量为零",
    "DeSitter": "de Sitter 度规，正宇宙学常数，Ricci 标量正常数",
    "AntiDeSitter": "anti-de Sitter 度规（球坐标），负宇宙学常数，Ricci 标量负常数",
    "AntiDeSitterStatic": "anti-de Sitter 静态坐标版本，Ricci 标量 R=-12",
    "MinkowskiCartesian": "Minkowski 平直时空（笛卡尔坐标），所有曲率为零",
    "MinkowskiPolar": "Minkowski 平直时空（球坐标），Christoffel 符号非零但曲率为零",
    "FLRW": "Friedmann-Lemaître-Robertson-Walker 宇宙度规，标度因子 a(t)",
    "Godel": "Gödel 旋转宇宙度规，存在闭合类时曲线，Ricci 张量非零",
    "BarriolaVilekin": "Barriola-Vilenkin 宇宙弦度规，拓扑缺陷时空，具有圆锥奇点",
    "BertottiKasner": "Bertotti-Kasner 电磁时空度规，常曲率产品空间",
    "CMetric": "C-度规，加速黑洞解，包含加速参数",
    "Davidson": "Davidson 宇宙学度规，柱对称解",
    "JanisNewmanWinicour": "Janis-Newman-Winicour 度规，裸奇点解（无电荷 Schwarzschild 一般化）",
    # Heavy 度规（需先运行 precompute --include-heavy 缓存 Fact Sheet）
    "ReissnerNordstrom": "带电静态黑洞度规（heavy），真空 Einstein 方程解但有电磁场",
    "Kerr": "旋转黑洞度规（heavy），稳态轴对称解，具有 ergoregion",
    "Ernst": "Ernst 磁化黑洞度规（heavy），Kerr 解在磁场中的推广",
    "KerrNewman": "旋转带电黑洞度规（heavy），最一般稳态轴对称 Einstein-Maxwell 解",
    "AlcubierreWarp": "Alcubierre 曲速引擎度规（heavy），允许超光速移动的时空构造",
    "BesselGravitationalWave": "Bessel 引力波度规（heavy），圆柱引力波解",
}

# 软改写类型映射
SOFT_REWRITE_TYPES = {
    "contrast": {"prompt": SYSTEM_PROMPT_CONTRAST, "model": MODEL_COMPOSE},
    "verify":   {"prompt": SYSTEM_PROMPT_VERIFY,   "model": MODEL_COMPOSE},
    "design":   {"prompt": SYSTEM_PROMPT_DESIGN,   "model": MODEL_COMPOSE},
    "reduce":   {"prompt": SYSTEM_PROMPT_REDUCE,   "model": MODEL_COMPOSE},
}

# 形式变换配置（暂时关闭，跳过 form_change 阶段）
FORM_CHANGE_TARGETS = []

# 只对有确定答案的认知形式做形式变换
FORM_CHANGE_SOURCE_TYPES = {"derivation", "numerical"}


# ==================== 通用工具 ====================


def _parse_llm_json(text: str) -> dict:
    """解析 LLM 返回的 JSON，处理 markdown 代码块和 LaTeX 转义问题。

    核心问题：LLM 输出的 LaTeX 命令如 \\theta 在 JSON 中只用单反斜杠 \\theta，
    而 JSON 规范要求字符串值内的反斜杠双写。更糟的是，\\t/\\f/\\r/\\n 是 JSON
    合法 escape，JSON 解析器会"成功"解析但把 \\theta 变成 tab+hetad 等——
    这些是错误结果，需要检测并重新修复。

    修复策略：
    1. 先尝试直接解析，成功但含控制字符→重试修复版
    2. 失败或含控制字符→保护双反斜杠和 quote escape，再全局修复单反斜杠
    3. 再失败→去掉控制字符兜底
    """
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # 尝试1：直接解析，但检查是否有不该出现的控制字符
    # （\t→tab, \f→form-feed, \r→cr 等被误解释）
    try:
        result = json.loads(text)
        if not _has_control_chars(result):
            return _fix_latex_concat_in_result(result)
        # 解析成功但含控制字符→说明 LaTeX \t/\f/\r/\n 被误解释了，需要修复
    except json.JSONDecodeError:
        pass

    # 尝试2：修复所有单反斜杠为双反斜杠，但保护已有的双反斜杠和 quote escape
    P1 = ''  # 保护 \\ (JSON 中的双反斜杠 → 字符串中的单反斜杠)
    P2 = ''  #保护 \" (quote escape)
    fixed = text.replace('\\\\', P1)      # 保护双反斜杠
    fixed = fixed.replace('\\\"', P2)     # 保护 quote escape
    fixed = fixed.replace('\\', '\\\\')   # 所有剩余单反斜杠 → 双反斜杠
    fixed = fixed.replace(P2, '\\\"')     # 恢复 quote escape
    fixed = fixed.replace(P1, '\\\\\\\\')  # 恢复双反斜杠 (4个反斜杠 → JSON 中的 \\)

    try:
        result = json.loads(fixed)
        if not _has_control_chars(result):
            return _fix_latex_concat_in_result(result)
    except json.JSONDecodeError:
        pass

    # 尝试3：去掉控制字符后重试
    cleaned = ''.join(c for c in fixed if ord(c) >= 32 or c == '\n')
    try:
        result = json.loads(cleaned)
        return _fix_latex_concat_in_result(result)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"LLM JSON 无法解析（已尝试3种修复策略，最后错误：{e.msg}）",
            text, 0
        )


def _has_control_chars(obj, depth=0):
    """检查解析结果中是否包含不该出现的控制字符（tab/form-feed/cr 等）。
    LaTeX 上下文中不应出现 tab/form-feed/cr/vt 这些控制字符。"""
    if depth > 10:
        return False
    if isinstance(obj, str):
        for c in obj:
            if c in '\t\f\r\x0b':
                return True
        return False
    if isinstance(obj, dict):
        return any(_has_control_chars(v, depth+1) for v in obj.values())
    if isinstance(obj, list):
        return any(_has_control_chars(v, depth+1) for v in obj)
    return False


def _fix_latex_concat_in_result(obj):
    """递归修复解析结果中所有字符串的 LaTeX 命令粘连。

    LLM 输出常见错误：\\gammar → 应为 \\gamma r
    cleaner.py 的 _fix_command_concatenation 只在 _clean_math_segment 中调用，
    但 _parse_llm_json 在 clean 之前解析，需要在解析后也修复。
    """
    from core.common.cleaner import _fix_command_concatenation
    if isinstance(obj, str):
        return _fix_command_concatenation(obj)
    if isinstance(obj, dict):
        return {k: _fix_latex_concat_in_result(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_fix_latex_concat_in_result(item) for item in obj]
    return obj


def _ensure_tags_dict(data: dict) -> dict:
    """确保 metadata.tags 是 dict 格式，并清理 LLM 输出的 "key:value" 污染。

    LLM 经常输出 "target_object:effective_potential" 格式，
    应为 "effective_potential"。自动剥离已知 key 的前缀。
    """
    from core.common.constants import TAG_KEYS

    if isinstance(data["metadata"]["tags"], list):
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    # 清理 "key:value" 污染：剥离与 key 名匹配的前缀
    tags = data["metadata"]["tags"]
    if isinstance(tags, dict):
        for key in list(tags.keys()):
            val = tags[key]
            if isinstance(val, str) and val.startswith(f"{key}:"):
                tags[key] = val[len(key) + 1:].strip()
            # 也处理嵌套前缀如 "scenario:photon_equatorial_motion"
            # 和冒号括号格式如 "coordinate:(t, r, theta, phi)"
            if isinstance(val, str) and ":" in val:
                # 只剥离第一个冒号前恰好是某个已知 tag key 的部分
                prefix = val.split(":")[0]
                if prefix in TAG_KEYS:
                    tags[key] = val[len(prefix) + 1:].strip()
    return data


def _save_raw(problem: Problem, label: str, output_dir: str = None) -> Problem:
    """只保存原始 JSON（不验证）。生成阶段完成后调用。"""
    if output_dir:
        out = Path(output_dir)
        problem_dict = clean_problem(problem)
        path = out / f"{label}.json"
        path.write_text(json.dumps(problem_dict, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  已保存 {label} (raw, 未验证)")
    return problem


def _validate_and_save(problem_dict: dict, label: str, output_dir: str = None,
                       base_temperature: float = 0.7) -> dict:
    """验证并保存到文件，失败直接标记 degraded（不修正）。

    Args:
        problem_dict: 题目的 dict 表示（非 Problem 对象）
        label: 文件名标签
        output_dir: 输出目录
        base_temperature: 验证的基础温度（未使用，保留兼容）

    Returns: 验证后的 problem_dict（失败时标记 degraded）
    """
    problem_dict = validate_and_fix_loop(problem_dict, max_attempts=1, base_temperature=base_temperature)
    if output_dir:
        out = Path(output_dir)
        path = out / f"{label}.json"
        path.write_text(json.dumps(problem_dict, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  验证完成 {label} (validated={problem_dict['metadata']['validated']}, degraded={problem_dict['metadata'].get('degraded', '?')})")
    return problem_dict


def _get_fact_sheet_for_seed(seed_dict: dict) -> dict:
    """获取种子题的 Fact Sheet（优先缓存）。无度规时返回空 dict。"""
    # 无度规种子题：返回空 Fact Sheet（不崩溃）
    if seed_dict.get("physical_data", {}).get("metric") is None:
        return {}

    cached_fs = seed_dict.get("cached_fact_sheet")
    if cached_fs and "error" not in cached_fs:
        return cached_fs
    from core.verify.validator import _compute_fact_sheet_for_problem
    fs = _compute_fact_sheet_for_problem(seed_dict)
    if "error" in fs:
        raise ValueError(f"种子题度规 Fact Sheet 计算失败: {fs['error']}")
    return fs


def _build_problem_from_llm_data(data: dict) -> Problem:
    """从 LLM 返回的 dict 构建 Problem 对象（过滤掉多余字段）。"""
    return Problem(
        metadata=Metadata(**{k: v for k, v in data["metadata"].items() if k in Metadata.__dataclass_fields__}),
        physical_data=PhysicalData(**{k: v for k, v in data["physical_data"].items() if k in PhysicalData.__dataclass_fields__}),
        origin=Origin(**{k: v for k, v in data["origin"].items() if k in Origin.__dataclass_fields__}),
    )


# ==================== 程序化字段统一填充 ====================


def _fill_programmatic_fields(data: dict, seed_dict: dict, seq: int,
                               stage: str, metric_data: dict,
                               cognitive_form: str = None,
                               soft_variant: str = None,
                               target_metric_name: str = None) -> dict:
    """统一填充所有程序化 metadata 和 physical_data 字段，覆盖 LLM 输出。

    LLM 只需输出 tags, target, origin 等创造性内容，
    所有可硬编码的字段由此函数统一填充。

    Args:
        data: LLM 返回的 dict（可能只包含部分字段）
        seed_dict: 种子题 dict（用于继承 source_id 等）
        seq: 序号（用于生成 id）
        stage: 当前 stage 名称
        metric_data: 度规数据 dict（dimension, variables, metric, metric_sympy）
        cognitive_form: 指定的认知形式（None 时从 LLM 输出推断）
        soft_variant: 软变体类型
        target_metric_name: 目标度规名（跨度规/替换时使用）
    """
    original_id = seed_dict["metadata"]["id"]
    source_id = seed_dict["metadata"].get("source_id", seed_dict["metadata"].get("source", ""))

    # ---- metadata ----
    data["metadata"]["id"] = f"{original_id}-{seq}"
    data["metadata"]["source"] = "generated"
    data["metadata"]["source_id"] = source_id
    data["metadata"]["source_type"] = seed_dict["metadata"].get("source_type", "problem_set")
    data["metadata"]["stage"] = stage
    data["metadata"]["lineage"] = (seed_dict["metadata"].get("lineage", [source_id])) + [data["metadata"]["id"]]

    # cognitive_form → type 映射
    if cognitive_form:
        data["metadata"]["cognitive_form"] = cognitive_form
        data["metadata"]["type"] = COGNITIVE_TO_TYPE.get(cognitive_form, "calculate")
    else:
        data["metadata"]["cognitive_form"] = TYPE_TO_COGNITIVE.get(data["metadata"].get("type", "calculate"), "numerical")

    # 度规环境
    if target_metric_name:
        data["metadata"]["physics_env"] = target_metric_name
        data["metadata"]["tags"]["metric"] = target_metric_name
    else:
        # 同度规模式：从种子题取 tags.metric
        seed_metric_name = seed_dict["metadata"].get("tags", {}).get("metric", "")
        if seed_metric_name and seed_metric_name not in ("metric", "", seed_metric_name.lower()):
            data["metadata"]["physics_env"] = seed_metric_name
            data["metadata"]["tags"]["metric"] = seed_metric_name
        else:
            data["metadata"]["physics_env"] = seed_dict["metadata"].get("physics_env", "") or seed_dict["metadata"].get("tags", {}).get("metric", "")
            # tags.metric 可能是 LLM 输出的占位符，也尝试清理
            current = data["metadata"]["tags"].get("metric", "")
            if current in ("metric", ""):
                data["metadata"]["tags"]["metric"] = seed_dict["metadata"].get("tags", {}).get("metric", "")

    data["metadata"]["soft_variant"] = soft_variant or ""
    data["metadata"]["tools_used"] = ["EinsteinPy"]
    data["metadata"]["validated"] = False

    # ---- physical_data ----
    data["physical_data"]["dimension"] = metric_data["dimension"]
    data["physical_data"]["variables"] = metric_data["variables"]
    data["physical_data"]["metric"] = metric_data["metric"]
    data["physical_data"]["metric_sympy"] = metric_data.get("metric_sympy")

    return data


# ==================== 泛化轴发现 ====================


def _discover_available_axes(seed_dict: dict, fact_sheet: dict) -> list:
    """基于种子题内容和 Fact Sheet，判断哪些泛化轴可用。

    对于无度规种子题，Fact Sheet 为空，需要从题目内容推断可用轴。
    Returns:
        list of (axis_name, axis_description) tuples
    """
    axes = []
    target = seed_dict["physical_data"].get("target", [])
    target_strs = [str(t) for t in target]
    question = seed_dict["origin"].get("question", "")
    answer = seed_dict["origin"].get("answer", "")
    metric_sympy = seed_dict["physical_data"].get("metric_sympy", [])
    seed_has_metric = seed_dict.get("physical_data", {}).get("metric") is not None

    # apply 轴：如果种子题推导了某个表达式，可以要求做极值/临界分析
    if any("V_eff" in t or "V_{\\text{eff}}" in t or "potential" in t.lower() or "effective" in t.lower() or "\\text{eff}" in t for t in target_strs):
        axes.append(("apply", GENERALIZATION_AXES["apply"]))
    # apply 轴：如果种子题求了某个张量分量，可以要求做进一步物理预测
    elif any("Gamma" in t or "Christoffel" in t or "Riemann" in t or "Ricci" in t or "Einstein" in t for t in target_strs):
        axes.append(("apply", GENERALIZATION_AXES["apply"]))
    # apply 轴（无度规题）：题目涉及守恒律、物理量关系等，可以要求做应用/极值分析
    elif not seed_has_metric and any(kw in question for kw in ["conserved", "守恒", "constant", "constant of motion", "invariant", "energy", "momentum", "angular", "effective", "period", "频率", "frequency", "orbit", "轨道", "trajectory", "potential", "势", "force", "力", "acceleration", "加速度", "stress", "压强", "pressure", "density", "密度", "mass", "质量", "energy density", "能量密度"]):
        axes.append(("apply", GENERALIZATION_AXES["apply"]))

    # extend 轴：Fact Sheet 有种子题没直接用到的几何量（仅度规种子题）
    if seed_has_metric:
        available_geom = set()
        if fact_sheet.get("christoffel"):
            available_geom.add("christoffel")
        if fact_sheet.get("riemann"):
            available_geom.add("riemann")
        if fact_sheet.get("ricci_tensor"):
            available_geom.add("ricci_tensor")
        if fact_sheet.get("einstein_tensor"):
            available_geom.add("einstein_tensor")
        if fact_sheet.get("killing_vectors"):
            available_geom.add("killing_vectors")
        if len(available_geom) >= 2:
            axes.append(("extend", GENERALIZATION_AXES["extend"]))
    # extend 轴（无度规题）：题目涉及物理概念体系，可以延伸到相关概念
    elif not seed_has_metric and any(kw in question for kw in ["tensor", "张量", "covariant", "协变", "derivative", "导数", "geodesic", "测地线", "curvature", "曲率", "symmetry", "对称", "Killing", "isometry", "同构", "Lorentz", "洛伦兹", "boost", "变换", "transform", "invariant", "不变量", "conserved", "守恒", "coordinate", "坐标", "frame", "参考系", "observer", "观测者", "redshift", "红移", "blueshift", "引力", "gravity", "gravitational", "Newtonian", "牛顿", "relativistic", "相对论性"]):
        axes.append(("extend", GENERALIZATION_AXES["extend"]))

    # limit 轴：度规有物理参数可取极限（仅度规种子题）
    if seed_has_metric and metric_sympy:
        has_M = any("M" in str(cell) for row in metric_sympy for cell in row)
        has_alpha = any("alpha" in str(cell) for row in metric_sympy for cell in row)
        has_a = any("a(t)" in str(cell) or "a**2" in str(cell) or "a(t)**2" in str(cell) for row in metric_sympy for cell in row)
        if has_M or has_alpha or has_a:
            axes.append(("limit", GENERALIZATION_AXES["limit"]))
    # limit 轴（无度规题）：题目有物理参数（速度、质量等）可取极端值
    elif not seed_has_metric and any(kw in question for kw in ["mass", "质量", "velocity", "速度", "speed", "频率", "frequency", "energy", "能量", "temperature", "温度", "pressure", "压强", "density", "密度", "radius", "半径", "distance", "距离", "limit", "极限", "approximation", "近似", "small", "large", "slow", "fast", "weak", "强", "strong field", "weak field", "Newtonian limit", "低速", "高速", "极端", "extreme"]):
        axes.append(("limit", GENERALIZATION_AXES["limit"]))

    # compare 轴：种子题涉及特定粒子类型或约束条件（只添加一次）
    compare_triggered = False
    if any("光子" in question or "photon" in question.lower() or "null geodesic" in question.lower() or "massless" in question.lower() for _ in [1]):
        axes.append(("compare", GENERALIZATION_AXES["compare"]))
        compare_triggered = True
    if not compare_triggered and ("赤道面" in question or "equatorial" in question.lower() or "theta = pi/2" in question.lower()):
        axes.append(("compare", GENERALIZATION_AXES["compare"]))
        compare_triggered = True
    # compare 轴（无度规题）：题目涉及不同参考系/不同条件下的对比
    if not compare_triggered and not seed_has_metric and any(kw in question for kw in ["observer", "观测者", "frame", "参考系", "inertial", "惯性", "accelerated", "加速", "rest", "静止", "moving", "运动", "不同", "compare", "比较", "contrast", "对比", "versus", "relative", "相对", "coordinate", "坐标变换", "different", "various", "multiple"]):
        axes.append(("compare", GENERALIZATION_AXES["compare"]))
        compare_triggered = True

    # invert 轴：种子题有明确的数值或表达式结论
    if answer and "无答案" not in answer and answer.strip() and len(answer.strip()) < 200:
        axes.append(("invert", GENERALIZATION_AXES["invert"]))

    # verify 轴：表达式有可验证的性质（极限行为、对称性等）
    if any("V_eff" in t or "V_{\\text{eff}}" in t or "\\text{eff}" in t or "potential" in t.lower() for t in target_strs):
        axes.append(("verify", GENERALIZATION_AXES["verify"]))
    # verify 轴（无度规题）：结论有可验证的极限/对称性质
    elif not seed_has_metric and any(kw in question.lower() for kw in ["verify", "验证", "prove", "证明", "show", "说明", "check", "检查", "limit", "极限", "symmetry", "对称", "dimensionless", "无量纲", "reduces to", "退化为", "coincides", "一致", "equals", "等于"]):
        axes.append(("verify", GENERALIZATION_AXES["verify"]))

    # 如果没有发现任何轴，默认提供全部
    if not axes:
        axes = list(GENERALIZATION_AXES.items())

    return axes


# ==================== n-gram 去重 ====================


def _get_ngrams(text: str, n: int = 4) -> set:
    """从文本提取 n-gram（按词级别）。"""
    clean = re.sub(r'\$[^$]+\$', ' MATH ', text)
    clean = re.sub(r'\\[a-zA-Z]+\{[^}]*\}', ' ', clean)
    clean = re.sub(r'[^\w\s]', ' ', clean)
    words = clean.lower().split()
    if len(words) < n:
        return set()
    return set(" ".join(words[i:i+n]) for i in range(len(words) - n + 1))


def _ngram_similarity(text_a: str, text_b: str, n: int = 4) -> float:
    """计算两段文本的 n-gram Jaccard 相似度。"""
    ngrams_a = _get_ngrams(text_a, n)
    ngrams_b = _get_ngrams(text_b, n)
    if not ngrams_a or not ngrams_b:
        return 0.0
    intersection = len(ngrams_a & ngrams_b)
    union = len(ngrams_a | ngrams_b)
    return intersection / union if union > 0 else 0.0


# ==================== Phase 1: cognitive_fanout ====================


def _generate_one(seed_dict: dict, seq: int, cognitive_form: str = None,
                   generalization_axis: str = None,
                   target_metric: dict = None):
    """单次生成：种子题 → Fact Sheet → LLM 编题。

    Args:
        seed_dict: 种子题 dict
        seq: 序号
        cognitive_form: 指定认知形式，None 时 LLM 自选
        generalization_axis: 指定泛化轴（apply/extend/limit/compare/invert/verify），None 时 LLM 自选
        target_metric: 目标度规 dict（来自 METRIC_LIBRARY），None 时使用种子题度规

    Returns (Problem, fact_sheet_dict).
    """
    tags = seed_dict["metadata"]["tags"]
    if isinstance(tags, list):
        from core.common.constants import TAG_KEYS
        tags = {k: v for k, v in zip(TAG_KEYS[:len(tags)], tags)}

    # 决定使用的度规和 Fact Sheet
    if target_metric:
        # 跨度规模式：使用目标度规
        metric_name = target_metric["name"]
        fact_sheet = get_cached_fact_sheet(metric_name)
        if fact_sheet is None:
            fact_sheet = compute_fact_sheet(target_metric["metric"], target_metric["variables"], metric_name=metric_name)
        used_pd = target_metric
        soft_variant = "cross_metric"
        print(f"  [{seq}] {metric_name} Fact Sheet 就绪, 开始跨度规编题 (axis={generalization_axis}, form={cognitive_form})...")
    else:
        # 同度规模式：使用种子题度规
        fact_sheet = _get_fact_sheet_for_seed(seed_dict)
        used_pd = seed_dict["physical_data"]
        soft_variant = generalization_axis or "extend"
        print(f"  [{seq}] Fact Sheet 就绪, 开始编题 (axis={generalization_axis}, form={cognitive_form})...")

    seed_question = seed_dict["origin"]["question"]
    seed_target = seed_dict["physical_data"]["target"]

    # 构造泛化轴指令
    axis_instruction = ""
    if generalization_axis:
        axis_desc = GENERALIZATION_AXES.get(generalization_axis, "")
        axis_instruction = (
            f"\n\n=== 泛化轴指令 ===\n"
            f"你必须沿 **{generalization_axis}** 轴泛化：{axis_desc}\n"
            f"metadata.tags.generalization_axis 必须写 \"{generalization_axis}\"。\n"
        )
    else:
        # 发现可用轴并提供给 LLM 选择
        available_axes = _discover_available_axes(seed_dict, fact_sheet)
        axis_lines = "\n".join(f"  - {name}: {desc}" for name, desc in available_axes)
        axis_instruction = (
            f"\n\n=== 可选泛化轴 ===\n"
            f"请从以下泛化轴中选择一个，沿该轴编题：\n{axis_lines}\n"
            f"metadata.tags.generalization_axis 写你选择的轴名称。\n"
        )

    if cognitive_form:
        type_hint = COGNITIVE_TO_TYPE.get(cognitive_form, "calculate")
        form_instruction = (
            f"请基于这份几何属性数据，围绕种子题目的物理场景，编出一道 **{cognitive_form}** 形式的题目。\n"
            f"题目类型 (metadata.type) 必须为 \"{type_hint}\"。\n"
        )
    else:
        form_instruction = (
            f"请基于这份几何属性数据，围绕种子题目的物理场景自行选择一个有意义的泛化方向，"
            f"编出一道后续延伸题目。\n"
        )

    # 跨度规时需要提示目标度规信息；同度规时提示度规数据由程序填充
    seed_has_metric = seed_dict.get("physical_data", {}).get("metric") is not None
    metric_instruction = ""
    fact_sheet_section = ""
    seed_metric_section = ""

    if target_metric:
        metric_instruction = (
            f"\n\n=== 目标度规信息 ===\n"
            f"度规名称: {metric_name}\n"
            f"物理场景: {target_metric['tags']['scenario']}\n"
            f"请将种子题的设问思路迁移到这个度规的物理场景中，编出一道在新度规下有意义的题目。\n"
            f"physical_data 中的度规数据由程序自动填充（dimension={target_metric['dimension']}，"
            f"variables={target_metric['variables']}），你只需指定 target。\n"
        )
        # 跨度规时用目标度规的 Fact Sheet
        if fact_sheet:
            fact_sheet_section = f"=== 几何属性数据 ===\n{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
    elif seed_has_metric:
        metric_instruction = (
            f"\n\nphysical_data 中的度规数据由程序自动填充（使用种子题度规），你只需指定 target。\n"
        )
        fact_sheet_section = f"=== 几何属性数据 ===\n{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        seed_metric_section = (
            f"=== 种子题的度规 ===\n"
            f"dimension: {seed_dict['physical_data']['dimension']}\n"
            f"variables: {seed_dict['physical_data']['variables']}\n"
            f"metric: {json.dumps(seed_dict['physical_data']['metric'], ensure_ascii=False)}\n"
        )
    else:
        # 无度规种子题：不需要 Fact Sheet 和度规数据
        metric_instruction = (
            f"\n\n种子题无显式度规。请基于种子题的物理概念和场景编出一道延伸题目。"
            f"不需要度规相关的计算，物理概念内核应保持一致。"
            f"physical_data.metric 设 null，dimension 和 variables 按题意填写。\n"
        )

    prompt = (
        f"{fact_sheet_section}"
        f"=== 种子题目 ===\n"
        f"设问方向：{tags['target_object']}\n"
        f"求解目标：{seed_target}\n"
        f"题目原文：{seed_question}\n\n"
        f"{seed_metric_section}"
        f"{form_instruction}"
        f"{axis_instruction}"
        f"{metric_instruction}"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_COMPOSE, model=MODEL_COMPOSE)
    data = _parse_llm_json(response)

    # 诊断：检查解析后的结构是否缺少必需键
    missing_keys = [k for k in ("metadata", "physical_data", "origin") if k not in data or not isinstance(data.get(k), dict)]
    if missing_keys:
        print(f"    [gen-{seq}] ⚠ LLM 输出缺少键: {missing_keys}")
        print(f"    [gen-{seq}] 解析后的顶层键: {list(data.keys())}")
        # 输出 LLM 原始 response（截断到 2000 字符以防过长）
        print(f"    [gen-{seq}] LLM 原始输出 (前2000字):\n{response[:2000]}")
        # 输出解析后的 data 结构概要
        print(f"    [gen-{seq}] 解析后 data 概要:")
        for k, v in data.items():
            if isinstance(v, dict):
                print(f"      {k}: dict with keys {list(v.keys())[:10]}")
            elif isinstance(v, str) and len(v) > 100:
                print(f"      {k}: str({len(v)} chars)")
            else:
                print(f"      {k}: {repr(v)[:80]}")

    _ensure_tags_dict(data)

    # 统一填充程序化字段
    target_metric_name = target_metric["name"] if target_metric else None
    # 从 LLM 输出中提取泛化轴（如果没有指定，则从 tags 读取）
    actual_axis = generalization_axis or data["metadata"]["tags"].get("generalization_axis", "")
    if not soft_variant or soft_variant == "extend":
        soft_variant = actual_axis or "extend"

    _fill_programmatic_fields(
        data, seed_dict, seq=seq,
        stage="scale:cognitive_fanout",
        metric_data=used_pd,
        cognitive_form=cognitive_form,
        soft_variant=soft_variant,
        target_metric_name=target_metric_name,
    )

    # 确保 generalization_axis 写入 tags
    data["metadata"]["tags"]["generalization_axis"] = actual_axis

    return (_build_problem_from_llm_data(data), fact_sheet)


def phase_cognitive_fanout(seed_dict: dict,
                           cognitive_forms: list = None,
                           generalization_axes: list = None,
                           num: int = 3,
                           cross_metric: bool = False,
                           num_cross_metrics: int = 2,
                           output_dir: str = None,
                           stem: str = None) -> tuple[list[Problem], list[str], dict]:
    """Phase 1: 从种子题扇出多道基础题（每种认知形式×泛化轴独立编题）。

    Args:
        seed_dict: 种子题 dict
        cognitive_forms: 认知形式列表（指定时每种 form 独立生成一道，覆盖 num）
        generalization_axes: 泛化轴列表（指定时每道题沿特定轴泛化；None 时 LLM 自选）
        num: LLM 自选方向的生成数量（forms=None 时使用）
        cross_metric: True 时增加跨度规泛化，为每种认知形式在不同目标度规下额外生成题目
        num_cross_metrics: 跨度规模式下挑选的目标度规数量
        output_dir: 输出目录
        stem: 文件名前缀

    Returns: (problems_list, fact_sheets_dict)
        problems_list: list of Problem
        fact_sheets_dict: dict mapping index → fact_sheet
    """
    fact_sheet_for_axes = _get_fact_sheet_for_seed(seed_dict)
    available_axes = _discover_available_axes(seed_dict, fact_sheet_for_axes)

    if cognitive_forms is None:
        forms_to_generate = [None] * num
    else:
        forms_to_generate = cognitive_forms

    # 泛化轴分配：如果没有指定，从可用轴中轮换
    if generalization_axes is None:
        # 自动从可用轴中轮换分配（避免所有题走同一方向）
        axis_pool = [ax[0] for ax in available_axes]
        axes_to_generate = []
        for i in range(len(forms_to_generate)):
            axes_to_generate.append(axis_pool[i % len(axis_pool)] if axis_pool else None)
    else:
        axes_to_generate = generalization_axes

    n_base = len(forms_to_generate)

    # 跨度规模式：挑选目标度规
    cross_metrics = []
    if cross_metric:
        seed_tags = seed_dict["metadata"]["tags"]
        if isinstance(seed_tags, list):
            from core.common.constants import TAG_KEYS
            seed_tags = {k: v for k, v in zip(TAG_KEYS[:len(seed_tags)], seed_tags)}
        cross_metrics = _pick_compatible_metrics_llm(seed_tags, num_cross_metrics)
        print(f"=== Phase 1: cognitive_fanout — {n_base} 道基础题 (axes: {axes_to_generate}) + {n_base} × {len(cross_metrics)} 道跨度规题 ===")
    else:
        print(f"=== Phase 1: cognitive_fanout — 生成 {n_base} 道基础题 (axes: {axes_to_generate}) ===")

    # 基础题：同度规 + 各认知形式 × 各泛化轴
    tasks = [(seed_dict, i, form, axis, None) for i, (form, axis) in enumerate(zip(forms_to_generate, axes_to_generate))]

    # 跨度规题：每种认知形式 × 每个目标度规
    seq_offset = n_base
    if cross_metric:
        for i, (form, axis) in enumerate(zip(forms_to_generate, axes_to_generate)):
            for j, metric in enumerate(cross_metrics):
                tasks.append((seed_dict, seq_offset + i * len(cross_metrics) + j, form, axis, metric))

    def do_gen(task):
        seed_dict, seq, form, axis, metric = task
        try:
            problem, fact_sheet = _generate_one(seed_dict, seq, cognitive_form=form, generalization_axis=axis, target_metric=metric)
            label = f"{stem or 'seed'}_gen_{seq}"
            _save_raw(problem, label, output_dir)
            return (seq, problem, fact_sheet, label)
        except Exception as e:
            import traceback
            print(f"    [gen-{seq}] 生成失败 (axis={axis}, form={form}): {e}")
            traceback.print_exc(limit=5)
            return None

    problems = []
    labels = []
    fact_sheets = {}
    with ThreadPoolExecutor(max_workers=min(len(tasks), 6)) as pool:
        futures = {pool.submit(do_gen, t): t for t in tasks}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                seq, problem, fact_sheet, label = result
                problems.append(problem)
                labels.append(label)
                fact_sheets[seq] = fact_sheet

    print(f"  Phase 1 完成: {len(problems)} 道题 ({n_base} 基础 + {len(problems) - n_base} 跨度规)")
    return problems, labels, fact_sheets


# ==================== Phase 2: metric_substitute ====================


def _pick_compatible_metrics_llm(problem_tags: dict, num_subs: int) -> list:
    """让 LLM 从度规库中挑选最适合替换的度规。

    Heavy 度规纳入候选的条件：缓存中已有该度规的 Fact Sheet（用户需先运行 precompute --include-heavy）。
    """
    current_metric = problem_tags.get("metric", "")
    # 清理无效的度规名（LLM 可能输出概念关键词而非真实度规名）
    invalid_names = {"metric", "killing_vector", "Killing_vector", "geodesic", "tensor", "coordinate", "none", "None", "null", "Null", ""}
    if current_metric in invalid_names:
        current_metric = "无显式度规"
    catalog_lines = []
    # 检查哪些 heavy 度规的缓存已就绪
    from core.common.fact_sheet_cache import _load_cache
    cache = _load_cache()

    for name, desc in _METRIC_DESCRIPTIONS.items():
        data = METRIC_LIBRARY[name]
        is_heavy = data.get("heavy", False)
        # heavy 度规：缓存可用才纳入
        if is_heavy:
            cached_fs = cache.get(name)
            if cached_fs is None or "error" in cached_fs:
                print(f"  {name} 是 heavy 度规且缓存未就绪，跳过（请先运行 precompute --include-heavy）")
                continue
            desc = desc.replace("(heavy)", "(heavy, 缓存已就绪)")
        if name == current_metric:
            continue
        catalog_lines.append(f"- {name}: {desc}")
    catalog = "\n".join(catalog_lines)

    system = SYSTEM_PROMPT_PICK_METRIC.format(metric_catalog=catalog, current_metric=current_metric)
    prompt = (
        f"题目信息：\n"
        f"- scenario: {problem_tags.get('scenario', '')}\n"
        f"- target_object: {problem_tags.get('target_object', '')}\n"
        f"- 当前度规: {current_metric}\n"
        f"- 需要挑选: {num_subs} 个最适合替换的度规\n\n"
        f"请输出一个 JSON 数组，包含挑选出的度规名称，按适合程度排序。只输出 JSON 数组，不要有其他文字。"
    )
    print(f"  挑选替换度规 (当前: {current_metric}, 需要: {num_subs} 个)...")
    response = ask_ai(prompt, system=system, model=MODEL_PICK_METRIC)
    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        names = json.loads(text)
    except json.JSONDecodeError:
        names = re.findall(r'"(\w+)"', text)

    result = []
    result_names = set()
    cache = _load_cache()
    for name in names:
        if name in METRIC_LIBRARY and name != current_metric and name not in result_names:
            data = METRIC_LIBRARY[name]
            is_heavy = data.get("heavy", False)
            # heavy 度规：缓存可用才纳入
            if is_heavy:
                cached_fs = cache.get(name)
                if cached_fs is None or "error" in cached_fs:
                    continue  # 跳过未缓存的 heavy 度规
            result.append(data)
            result_names.add(name)
        if len(result) >= num_subs:
            break

    # 如果挑选不够，补充候选（也遵循缓存优先，且保证名称不重复）
    if len(result) < num_subs:
        for name, data in METRIC_LIBRARY.items():
            if name != current_metric and name not in result_names:
                is_heavy = data.get("heavy", False)
                if is_heavy:
                    cached_fs = cache.get(name)
                    if cached_fs is None or "error" in cached_fs:
                        continue  # 跳过未缓存的 heavy 度规
                result.append(data)
                result_names.add(name)
                if len(result) >= num_subs:
                    break
    return result


def _substitute_metric(problem: Problem, original_fact_sheet: dict, new_metric: dict, seq: int) -> Problem:
    """将一道题目的度规替换为新度规。"""
    metric_name = new_metric["name"]
    new_fact_sheet = get_cached_fact_sheet(metric_name)
    if new_fact_sheet is None:
        print(f"    [sub-{seq}] 计算 {metric_name} Fact Sheet（无缓存）...")
        new_fact_sheet = compute_fact_sheet(new_metric["metric"], new_metric["variables"], metric_name=metric_name)
    else:
        print(f"    [sub-{seq}] {metric_name} Fact Sheet 就绪...")

    prompt = (
        f"以下是一道已编写好的题目及其原始 Fact Sheet，以及一份新度规的 Fact Sheet。\n\n"
        f"=== 原题目 ===\n{json.dumps(asdict(problem), ensure_ascii=False, indent=2)}\n\n"
        f"=== 原度规 Fact Sheet ===\n{json.dumps(original_fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"=== 新度规 Fact Sheet ===\n{json.dumps(new_fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"请将原题目适配到新度规上。保持题目类型和结构不变，用新度规的数据替换原度规的数据。\n"
        f"physical_data 中的度规数据由程序自动填充（使用新度规数据），你只需指定 target。\n"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_SUBSTITUTE, model=MODEL_SUBSTITUTE)
    data = _parse_llm_json(response)

    # 诊断：检查解析后的结构是否缺少必需键
    missing_keys = [k for k in ("metadata", "physical_data", "origin") if k not in data or not isinstance(data.get(k), dict)]
    if missing_keys:
        print(f"    [sub-{seq}] ⚠ LLM 输出缺少键: {missing_keys}")
        print(f"    [sub-{seq}] 解析后的顶层键: {list(data.keys())}")
        print(f"    [sub-{seq}] LLM 原始输出 (前2000字):\n{response[:2000]}")
        for k, v in data.items():
            if isinstance(v, dict):
                print(f"      {k}: dict with keys {list(v.keys())[:10]}")
            elif isinstance(v, str) and len(v) > 100:
                print(f"      {k}: str({len(v)} chars)")
            else:
                print(f"      {k}: {repr(v)[:80]}")

    # 统一填充程序化字段
    # seed_dict 从原始 problem 的 metadata 构造
    seed_dict_from_problem = {
        "metadata": {
            "id": problem.metadata.id,
            "source_id": problem.metadata.source_id or problem.metadata.source or "",
            "source_type": problem.metadata.source_type or "problem_set",
            "lineage": problem.metadata.lineage or [problem.metadata.source_id or problem.metadata.source or ""],
            "tags": {k: v for k, v in problem.metadata.tags.items()} if isinstance(problem.metadata.tags, dict) else {},
        },
    }
    # substitute 保持原题 type
    data["metadata"]["type"] = problem.metadata.type

    _fill_programmatic_fields(
        data, seed_dict_from_problem, seq=seq,
        stage="scale:metric_substitute",
        metric_data=new_metric,
        soft_variant="substitute",
        target_metric_name=metric_name,
    )
    _ensure_tags_dict(data)

    return _build_problem_from_llm_data(data)


def phase_metric_substitute(problems: list[Problem],
                             labels: list[str],
                             fact_sheets: dict,
                             seed_tags: dict,
                             num_subs: int = 2,
                             output_dir: str = None,
                             stem: str = None) -> tuple[list[Problem], list[str], dict]:
    """Phase 2: 对每道基础题做度规替换。

    Args:
        problems: Phase 1 产出的 Problem 列表
        labels: Phase 1 产出的 labels 列表
        fact_sheets: Phase 1 产出的 fact_sheets dict（key=seq）
        seed_tags: 种子题的 tags dict（用于挑选替换度规）
        num_subs: 每道题替换几个度规
        output_dir: 输出目录
        stem: 文件名前缀

    Returns: (problems_list, fact_sheets_dict) — 包含 Phase 1 + Phase 2 的所有题目
    """
    print(f"\n=== Phase 2: metric_substitute — {len(problems)} × {num_subs} = {len(problems) * num_subs} 道 ===")

    if isinstance(seed_tags, list):
        from core.common.constants import TAG_KEYS
        seed_tags = {k: v for k, v in zip(TAG_KEYS[:len(seed_tags)], seed_tags)}

    sub_metrics = _pick_compatible_metrics_llm(seed_tags, num_subs)
    print(f"  替换度规: {[m['name'] for m in sub_metrics]}")

    sub_tasks = []
    sub_seq = 0
    for i, problem in enumerate(problems):
        for metric in sub_metrics:
            sub_seq += 1
            sub_tasks.append((problem, fact_sheets.get(i, {}), metric, sub_seq))

    def do_sub(task):
        problem, fs, metric, sub_seq = task
        try:
            new_problem = _substitute_metric(problem, fs, metric, sub_seq)
            label = f"{stem or 'seed'}_sub_{sub_seq}_{metric['name']}"
            _save_raw(new_problem, label, output_dir)
            return (sub_seq, metric["name"], new_problem, label)
        except Exception as e:
            import traceback
            print(f"    [sub-{sub_seq}] 度规替换 → {metric['name']} 失败: {e}")
            traceback.print_exc(limit=5)
            return None

    sub_problems = []
    sub_labels = []
    sub_fact_sheets = {}
    with ThreadPoolExecutor(max_workers=min(len(sub_tasks), 6)) as pool:
        futures = {pool.submit(do_sub, t): t for t in sub_tasks}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                sub_seq, metric_name, new_problem, label = result
                sub_problems.append(new_problem)
                sub_labels.append(label)

    # 合并 Phase 1 + Phase 2 的题目
    all_problems = problems + sub_problems
    all_labels = labels + sub_labels
    all_fact_sheets = {**fact_sheets}
    for i, p in enumerate(sub_problems):
        all_fact_sheets[len(problems) + i] = fact_sheets.get(0, {})

    print(f"  Phase 2 完成: {len(sub_problems)} 道替换题，总计 {len(all_problems)} 道")
    return all_problems, all_labels, all_fact_sheets


# ==================== Phase 2.5: form_change ====================


def _form_change_one(problem: Problem, fact_sheet: dict, target_form: str, seq: int) -> Problem:
    """将一道题目变换为目标认知形式（multiple_choice/code/conceptual）。

    Args:
        problem: 原题目 Problem 对象
        fact_sheet: 原度规的 Fact Sheet
        target_form: 目标认知形式（"multiple_choice" | "code" | "conceptual"）
        seq: 序号

    Returns: 变换后的 Problem 对象
    """
    if target_form not in FORM_CHANGE_TARGETS:
        raise ValueError(f"未知的形式变换目标: {target_form}")

    system_prompt = SYSTEM_PROMPT_FORM_CHANGE.replace("{target_form}", target_form)

    prompt = (
        f"以下是一道原题目及其度规的 Fact Sheet。\n\n"
        f"=== 原题目 ===\n{json.dumps(asdict(problem), ensure_ascii=False, indent=2)}\n\n"
        f"=== 度规 Fact Sheet ===\n{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"请将原题目变换为 **{target_form}** 形式的题目。"
        f"物理内核（度规、求解对象、核心结论）不变，但做题者需要用不同的方式回答。\n"
        f"physical_data 中的度规数据由程序自动填充（使用原题度规），你只需指定 target。\n"
    )

    print(f"    [form-{seq}] 形式变换 → {target_form}...")
    response = ask_ai(prompt, system=system_prompt, model=MODEL_COMPOSE)
    data = _parse_llm_json(response)

    # 诊断
    missing_keys = [k for k in ("metadata", "physical_data", "origin") if k not in data or not isinstance(data.get(k), dict)]
    if missing_keys:
        print(f"    [form-{seq}] ⚠ LLM 输出缺少键: {missing_keys}")
        print(f"    [form-{seq}] 解析后的顶层键: {list(data.keys())}")
        print(f"    [form-{seq}] LLM 原始输出 (前2000字):\n{response[:2000]}")

    # seed_dict 从原始 problem 的 metadata 构造
    seed_dict_from_problem = {
        "metadata": {
            "id": problem.metadata.id,
            "source_id": problem.metadata.source_id or problem.metadata.source or "",
            "source_type": problem.metadata.source_type or "problem_set",
            "lineage": problem.metadata.lineage or [problem.metadata.source_id or problem.metadata.source or ""],
            "tags": {k: v for k, v in problem.metadata.tags.items()} if isinstance(problem.metadata.tags, dict) else {},
            "physics_env": problem.metadata.physics_env or "",
        },
        "physical_data": {
            "dimension": problem.physical_data.dimension,
            "variables": problem.physical_data.variables,
            "metric": problem.physical_data.metric,
            "metric_sympy": problem.physical_data.metric_sympy,
        },
    }

    # 形式变换的 type 由 target_form 决定
    data["metadata"]["type"] = COGNITIVE_TO_TYPE.get(target_form, "calculate")

    _fill_programmatic_fields(
        data, seed_dict_from_problem, seq=seq,
        stage="scale:form_change",
        metric_data=seed_dict_from_problem["physical_data"],
        cognitive_form=target_form,
        soft_variant=f"form_change:{target_form}",
        target_metric_name=problem.metadata.physics_env or problem.metadata.tags.get("metric", ""),
    )
    _ensure_tags_dict(data)

    # 确保 generalization_axis 写入 tags
    data["metadata"]["tags"]["generalization_axis"] = f"form_change:{target_form}"

    return _build_problem_from_llm_data(data)


def phase_form_change(problems: list[Problem],
                      labels: list[str],
                      fact_sheets: dict,
                      target_forms: list = None,
                      output_dir: str = None,
                      stem: str = None) -> tuple[list[Problem], list[str], dict]:
    """Phase 2.5: 对 derivation/numerical 题目做形式变换。

    只对 cognitive_form in FORM_CHANGE_SOURCE_TYPES 的题目做变换，
    每道题变换为所有指定的 target_forms。

    Args:
        problems: Phase 1+2 产出的 Problem 列表
        fact_sheets: Phase 1+2 产出的 fact_sheets dict
        target_forms: 形式变换目标列表（默认 ["multiple_choice", "code", "conceptual"]）
        output_dir: 输出目录
        stem: 文件名前缀

    Returns: (problems_list, fact_sheets_dict) — 包含 Phase 1+2+2.5 的所有题目
    """
    if target_forms is None:
        target_forms = FORM_CHANGE_TARGETS

    # 过滤可变换的题目（只对 derivation/numerical 做）
    transformable_indices = [
        i for i, p in enumerate(problems)
        if (p.metadata.cognitive_form or TYPE_TO_COGNITIVE.get(p.metadata.type, ""))
        in FORM_CHANGE_SOURCE_TYPES
    ]

    if not transformable_indices:
        print(f"\n=== Phase 2.5: form_change — 跳过（无 derivation/numerical 题） ===")
        return problems, labels, fact_sheets

    n_transformable = len(transformable_indices)
    n_total = n_transformable * len(target_forms)
    print(f"\n=== Phase 2.5: form_change — {n_transformable} × {len(target_forms)} = {n_total} 道 ===")

    fc_tasks = []
    fc_seq = 0
    for i in transformable_indices:
        for tf in target_forms:
            fc_seq += 1
            fc_tasks.append((problems[i], fact_sheets.get(i, {}), tf, fc_seq))

    def do_fc(task):
        problem, fs, tf, fc_seq = task
        try:
            new_problem = _form_change_one(problem, fs, tf, fc_seq)
            label = f"{stem or 'seed'}_fc_{fc_seq}_{tf}"
            _save_raw(new_problem, label, output_dir)
            return (fc_seq, tf, new_problem, label)
        except Exception as e:
            import traceback
            print(f"    [form-{fc_seq}] 形式变换 → {tf} 失败: {e}")
            traceback.print_exc(limit=5)
            return None

    fc_problems = []
    fc_labels = []
    with ThreadPoolExecutor(max_workers=min(len(fc_tasks), 6)) as pool:
        futures = {pool.submit(do_fc, t): t for t in fc_tasks}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                fc_seq, tf, new_problem, label = result
                fc_problems.append(new_problem)
                fc_labels.append(label)

    all_problems = problems + fc_problems
    all_labels = labels + fc_labels
    all_fact_sheets = {**fact_sheets}
    for i, p in enumerate(fc_problems):
        all_fact_sheets[len(problems) + i] = fact_sheets.get(0, {})

    print(f"  Phase 2.5 完成: {len(fc_problems)} 道形式变换题，总计 {len(all_problems)} 道")
    return all_problems, all_labels, all_fact_sheets


# ==================== Phase 3: soft_rewrite ====================


def _soft_rewrite_one(problem: Problem, fact_sheet: dict, rewrite_type: str, seq: int) -> Problem:
    """软改写一道题目（对照/校验/设计/归约）。"""
    if rewrite_type not in SOFT_REWRITE_TYPES:
        raise ValueError(f"未知的软改写类型: {rewrite_type}")

    rw_config = SOFT_REWRITE_TYPES[rewrite_type]
    system_prompt = rw_config["prompt"]
    model = rw_config["model"]

    # contrast 类型需要另一个度规的 Fact Sheet
    extra_context = ""
    contrast_metric_name = None
    if rewrite_type == "contrast":
        current_metric = problem.metadata.tags.get("metric", "")
        from core.common.fact_sheet_cache import _load_cache as _fs_load_cache
        fs_cache = _fs_load_cache()
        for name in METRIC_LIBRARY:
            if name == current_metric:
                continue
            is_heavy = METRIC_LIBRARY[name].get("heavy", False)
            # heavy 度规：缓存可用才考虑
            if is_heavy:
                cached = fs_cache.get(name)
                if cached is None or "error" in cached:
                    continue
            contrast_fs = get_cached_fact_sheet(name)
            if contrast_fs is None:
                contrast_fs = compute_fact_sheet(METRIC_LIBRARY[name]["metric"], METRIC_LIBRARY[name]["variables"], metric_name=name)
            contrast_metric_name = name
            extra_context = f"\n\n=== 对比度规 ({name}) Fact Sheet ===\n{json.dumps(contrast_fs, ensure_ascii=False, indent=2)}"
            break

    # physical_data 指令：contrast 不锁定（涉及两种度规），其余由程序填充
    pd_instruction = ""
    if rewrite_type != "contrast":
        pd_instruction = "\n\nphysical_data 中的度规数据由程序自动填充（使用原题度规），你只需指定 target。\n"

    prompt = (
        f"以下是该度规的完整几何属性数据，以及一道原题目。\n\n"
        f"=== 几何属性数据 ===\n{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"=== 原题目 ===\n{json.dumps(asdict(problem), ensure_ascii=False, indent=2)}\n"
        f"{extra_context}\n\n"
        f"请将原题目改写为{rewrite_type}类型的软改写题。"
        f"{pd_instruction}"
    )

    print(f"    [soft-{seq}] 软改写 ({rewrite_type})...")
    response = ask_ai(prompt, system=system_prompt, model=model)
    data = _parse_llm_json(response)

    # 诊断
    missing_keys = [k for k in ("metadata", "physical_data", "origin") if k not in data or not isinstance(data.get(k), dict)]
    if missing_keys:
        print(f"    [soft-{seq}] ⚠ LLM 输出缺少键: {missing_keys}")
        print(f"    [soft-{seq}] 解析后的顶层键: {list(data.keys())}")
        print(f"    [soft-{seq}] LLM 原始输出 (前2000字):\n{response[:2000]}")

    # seed_dict 从原始 problem 的 metadata 构造
    seed_dict_from_problem = {
        "metadata": {
            "id": problem.metadata.id,
            "source_id": problem.metadata.source_id or problem.metadata.source or "",
            "source_type": problem.metadata.source_type or "problem_set",
            "lineage": problem.metadata.lineage or [problem.metadata.source_id or problem.metadata.source or ""],
            "tags": {k: v for k, v in problem.metadata.tags.items()} if isinstance(problem.metadata.tags, dict) else {},
            "physics_env": problem.metadata.physics_env or "",
        },
        "physical_data": {
            "dimension": problem.physical_data.dimension,
            "variables": problem.physical_data.variables,
            "metric": problem.physical_data.metric,
            "metric_sympy": problem.physical_data.metric_sympy,
        },
    }

    # soft rewrite 的 type 由 rewrite_type 决定（除 reduce 保持原题类型）
    if rewrite_type == "reduce":
        data["metadata"]["type"] = problem.metadata.type
    else:
        data["metadata"]["type"] = COGNITIVE_TO_TYPE.get(data["metadata"].get("cognitive_form", "conceptual"), "concept")

    # contrast 使用对比度规，其余使用原题度规
    if rewrite_type == "contrast":
        metric_data_for_fill = seed_dict_from_problem["physical_data"]
        target_metric_name_for_fill = contrast_metric_name or problem.metadata.physics_env or problem.metadata.tags.get("metric", "")
    else:
        metric_data_for_fill = seed_dict_from_problem["physical_data"]
        target_metric_name_for_fill = problem.metadata.physics_env or problem.metadata.tags.get("metric", "")

    _fill_programmatic_fields(
        data, seed_dict_from_problem, seq=seq,
        stage="scale:soft_rewrite",
        metric_data=metric_data_for_fill,
        soft_variant=rewrite_type,
        target_metric_name=target_metric_name_for_fill,
    )
    _ensure_tags_dict(data)

    return _build_problem_from_llm_data(data)


def phase_soft_rewrite(problems: list[Problem],
                       labels: list[str],
                       fact_sheets: dict,
                       num_soft: int = 1,
                       soft_rewrite_types: list = None,
                       output_dir: str = None,
                       stem: str = None) -> tuple[list[Problem], list[str], dict]:
    """Phase 3: 对每道基础题做软改写（对照/校验/设计/归约）。

    Args:
        problems: Phase 1+2 产出的 Problem 列表
        fact_sheets: Phase 1+2 产出的 fact_sheets dict
        num_soft: 每道基础题的软改写数量（只对 Phase 1 的基础题做）
        soft_rewrite_types: 软改写类型列表（默认全部四种）
        output_dir: 输出目录
        stem: 文件名前缀

    Returns: (problems_list, fact_sheets_dict) — 包含 Phase 1+2+3 的所有题目
    """
    if soft_rewrite_types is None:
        soft_rewrite_types = list(SOFT_REWRITE_TYPES.keys())

    if num_soft <= 0 or not soft_rewrite_types:
        print(f"\n=== Phase 3: soft_rewrite — 跳过 (num_soft=0) ===")
        return problems, labels, fact_sheets

    # 只对前 len(base) 道题（Phase 1 的基础题）做软改写
    n_base = min(len(problems), max(fact_sheets.keys()) + 1 if fact_sheets else len(problems))
    print(f"\n=== Phase 3: soft_rewrite — {n_base} × {num_soft} = {n_base * num_soft} 道 ===")

    rw_tasks = []
    rw_seq = 0
    for i in range(n_base):
        selected_types = []
        for j in range(num_soft):
            type_idx = (i + j) % len(soft_rewrite_types)
            selected_types.append(soft_rewrite_types[type_idx])
        for rw_type in selected_types:
            rw_seq += 1
            rw_tasks.append((problems[i], fact_sheets.get(i, {}), rw_type, rw_seq))

    def do_rw(task):
        problem, fs, rw_type, rw_seq = task
        try:
            new_problem = _soft_rewrite_one(problem, fs, rw_type, rw_seq)
            label = f"{stem or 'seed'}_rw_{rw_seq}_{rw_type}"
            _save_raw(new_problem, label, output_dir)
            return (rw_seq, rw_type, new_problem, label)
        except Exception as e:
            import traceback
            print(f"    [rw-{rw_seq}] 软改写 → {rw_type} 失败: {e}")
            traceback.print_exc(limit=5)
            return None

    rw_problems = []
    rw_labels = []
    with ThreadPoolExecutor(max_workers=min(len(rw_tasks), 6)) as pool:
        futures = {pool.submit(do_rw, t): t for t in rw_tasks}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                rw_seq, rw_type, new_problem, label = result
                rw_problems.append(new_problem)
                rw_labels.append(label)

    all_problems = problems + rw_problems
    all_labels = labels + rw_labels
    all_fact_sheets = {**fact_sheets}
    for i, p in enumerate(rw_problems):
        all_fact_sheets[len(problems) + i] = fact_sheets.get(0, {})

    print(f"  Phase 3 完成: {len(rw_problems)} 道软改写题，总计 {len(all_problems)} 道")
    return all_problems, all_labels, all_fact_sheets


# ==================== Phase 3.5: batch_validate ====================


def phase_batch_validate(problems: list[Problem],
                         labels: list[str],
                         output_dir: str = None,
                         max_workers: int = 6,
                         base_temperature: float = 0.7) -> list[Problem]:
    """Phase 3.5: 批量并行验证所有题目。

    生成阶段已将原始 JSON 保存到文件，此处逐题读取并验证修正，
    验证后的文件原地覆盖写入。

    Args:
        problems: 所有 Phase 产出的 Problem 列表
        labels: 对应的文件名标签列表
        output_dir: 输出目录
        max_workers: 并行验证线程数
        base_temperature: 验证修正的基础温度

    Returns: 验证后的 Problem 列表（从文件重新读取）
    """
    if not output_dir:
        print(f"\n=== Phase 3.5: batch_validate — 跳过（无输出目录） ===")
        return problems

    print(f"\n=== Phase 3.5: batch_validate — 并行验证 {len(problems)} 道题 ===")

    def do_validate(task):
        i, problem, label = task
        out = Path(output_dir)
        path = out / f"{label}.json"
        if not path.exists():
            # 文件不存在（可能生成阶段没保存），从 Problem 对象构造
            problem_dict = clean_problem(problem)
        else:
            problem_dict = json.loads(path.read_text(encoding="utf-8"))
        validated_dict = _validate_and_save(problem_dict, label, output_dir, base_temperature)
        # 从验证后的 dict 重建 Problem 对象
        return (i, validated_dict)

    validated_dicts = {}
    with ThreadPoolExecutor(max_workers=min(len(problems), max_workers)) as pool:
        futures = {pool.submit(do_validate, (i, p, labels[i])): i for i, p in enumerate(problems)}
        for future in as_completed(futures):
            i, validated_dict = future.result()
            validated_dicts[i] = validated_dict

    # 按原始顺序重建
    result = []
    for i in range(len(problems)):
        validated_dict = validated_dicts.get(i)
        if validated_dict:
            result.append(_build_problem_from_llm_data(validated_dict))
        else:
            result.append(problems[i])

    n_validated = sum(1 for d in validated_dicts.values() if d.get("metadata", {}).get("validated", False))
    n_degraded = sum(1 for d in validated_dicts.values() if d.get("metadata", {}).get("degraded", False))
    print(f"  Phase 3.5 完成: {n_validated}/{len(problems)} 通过, {n_degraded} degraded")
    return result


def phase_ngram_dedup(problems: list[Problem],
                      threshold: float = 0.7) -> list[Problem]:
    """Phase 4: n-gram 相似度去重。

    Args:
        problems: 所有 Phase 产出的 Problem 列表
        threshold: 相似度阈值（超过则判定为重复）

    Returns: 去重后的 Problem 列表
    """
    deduped = []
    seen_statements = []

    for problem in problems:
        statement = problem.origin.question or ""
        is_dup = False
        for prev_stmt in seen_statements:
            sim = _ngram_similarity(statement, prev_stmt)
            if sim > threshold:
                is_dup = True
                print(f"  ngram去重: 相似度 {sim:.2f} > {threshold}，剔除")
                break
        if not is_dup:
            deduped.append(problem)
            seen_statements.append(statement)

    dedup_count = len(problems) - len(deduped)
    print(f"\n=== Phase 4: ngram去重 — 去掉 {dedup_count} 道，保留 {len(deduped)} 道 ===")
    return deduped


# ==================== 一键拼装：fan_through ====================


def fan_through(json_path: str,
                cognitive_forms: list = None,
                generalization_axes: list = None,
                num: int = 3,
                num_subs: int = 2,
                num_soft: int = 1,
                soft_rewrite_types: list = None,
                form_changes: list = None,
                cross_metric: bool = False,
                num_cross_metrics: int = 2,
                output_dir: str = None,
                stem: str = None) -> tuple[list[Problem], PipelineResult]:
    """一键运行全部 Phase：fanout → substitute → form_change → soft_rewrite → dedup。

    Args:
        json_path: 种子题目 JSON 文件路径
        cognitive_forms: 认知形式列表（指定时覆盖 num）
        generalization_axes: 泛化轴列表（指定时沿特定轴泛化；None 时自动分配）
        num: LLM 自选方向的生成数量
        num_subs: 度规替换数量
        num_soft: 软改写数量
        soft_rewrite_types: 软改写类型列表
        form_changes: 形式变换目标列表（默认 ["multiple_choice", "code", "conceptual"]）
        cross_metric: True 时 Phase 1 增加跨度规泛化
        num_cross_metrics: 跨度规模式下挑选的目标度规数量
        output_dir: 输出目录
        stem: 文件名前缀

    Returns: (去重后的 Problem 列表, PipelineResult)
    """
    from core.common.api_client import reset_llm_stats
    reset_llm_stats()

    wall_start = time.time()

    with open(json_path, "r", encoding="utf-8") as f:
        seed_dict = json.load(f)

    seed_id = seed_dict["metadata"]["id"]

    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
    if not stem:
        stem = Path(json_path).stem

    phase_stats_list = []

    # 检测种子题是否有度规，决定泛化策略
    seed_has_metric = seed_dict.get("physical_data", {}).get("metric") is not None

    if not seed_has_metric:
        # 无度规种子题：自动开启跨度规以补偿缺少的度规替换阶段
        if not cross_metric:
            cross_metric = True
            num_cross_metrics = num_subs  # 用相同数量跨度规题补偿 Phase 2 的缺失
        print(f"  [无度规种子题] 自动开启跨度规 (num_cross_metrics={num_cross_metrics})，Phase 2 将跳过")

    # Phase 1: cognitive_fanout
    t = Timer(); t.start()
    llm_before = get_llm_stats()["calls"]
    problems, labels, fact_sheets = phase_cognitive_fanout(
        seed_dict, cognitive_forms=cognitive_forms, generalization_axes=generalization_axes, num=num,
        cross_metric=cross_metric, num_cross_metrics=num_cross_metrics,
        output_dir=output_dir, stem=stem)
    t.stop()
    phase_stats_list.append(PhaseStats(
        name="cognitive_fanout",
        input_count=1,
        output_count=len(problems),
        skipped_count=0,
        failed_count=0,
        wall_seconds=t.elapsed,
        llm_calls=get_llm_stats()["calls"] - llm_before,
        errors=[]))

    # Phase 2: metric_substitute（无度规种子题跳过）
    seed_tags = seed_dict["metadata"]["tags"]
    if seed_has_metric:
        t = Timer(); t.start()
        llm_before = get_llm_stats()["calls"]
        n_before = len(problems)
        problems, labels, fact_sheets = phase_metric_substitute(
            problems, labels, fact_sheets, seed_tags, num_subs=num_subs,
            output_dir=output_dir, stem=stem)
        t.stop()
        phase_stats_list.append(PhaseStats(
            name="metric_substitute",
            input_count=n_before,
            output_count=len(problems) - n_before,
            skipped_count=0,
            failed_count=0,
            wall_seconds=t.elapsed,
            llm_calls=get_llm_stats()["calls"] - llm_before,
            errors=[]))
    else:
        print("  Phase 2: 跳过度规替换（种子题无度规）")
        phase_stats_list.append(PhaseStats(
            name="metric_substitute",
            input_count=len(problems),
            output_count=0,
            skipped_count=len(problems),
            failed_count=0,
            wall_seconds=0,
            llm_calls=0,
            errors=[]))

    # Phase 3: soft_rewrite（先软改写改物理内容，再形式变换改认知形式）
    t = Timer(); t.start()
    llm_before = get_llm_stats()["calls"]
    n_before = len(problems)
    problems, labels, fact_sheets = phase_soft_rewrite(
        problems, labels, fact_sheets, num_soft=num_soft,
        soft_rewrite_types=soft_rewrite_types,
        output_dir=output_dir, stem=stem)
    t.stop()
    phase_stats_list.append(PhaseStats(
        name="soft_rewrite",
        input_count=n_before,
        output_count=len(problems) - n_before,
        skipped_count=0,
        failed_count=0,
        wall_seconds=t.elapsed,
        llm_calls=get_llm_stats()["calls"] - llm_before,
        errors=[]))

    # Phase 3.5: form_change（对 derivation/numerical 题做形式变换）
    t = Timer(); t.start()
    llm_before = get_llm_stats()["calls"]
    n_before = len(problems)
    problems, labels, fact_sheets = phase_form_change(
        problems, labels, fact_sheets, target_forms=form_changes,
        output_dir=output_dir, stem=stem)
    t.stop()
    skipped_fc = max(0, len(problems) - n_before)  # 如果 phase 跳过则 0
    phase_stats_list.append(PhaseStats(
        name="form_change",
        input_count=n_before,
        output_count=len(problems) - n_before,
        skipped_count=0 if len(problems) > n_before else n_before,  # 全跳过时记录
        failed_count=0,
        wall_seconds=t.elapsed,
        llm_calls=get_llm_stats()["calls"] - llm_before,
        errors=[]))

    # Phase 3.5: batch_validate（并行验证所有题目）
    t = Timer(); t.start()
    llm_before = get_llm_stats()["calls"]
    n_before = len(problems)
    problems = phase_batch_validate(problems, labels, output_dir=output_dir)
    t.stop()
    validated = sum(1 for p in problems if p.metadata.validated)
    degraded = sum(1 for p in problems if p.metadata.degraded)
    phase_stats_list.append(PhaseStats(
        name="batch_validate",
        input_count=len(problems),
        output_count=len(problems),
        skipped_count=0,
        failed_count=degraded,
        wall_seconds=t.elapsed,
        llm_calls=get_llm_stats()["calls"] - llm_before,
        errors=[]))

    # Phase 4: ngram_dedup
    t = Timer(); t.start()
    n_before = len(problems)
    problems = phase_ngram_dedup(problems)
    t.stop()
    dedup_removed = n_before - len(problems)
    phase_stats_list.append(PhaseStats(
        name="ngram_dedup",
        input_count=n_before,
        output_count=len(problems),
        skipped_count=dedup_removed,
        failed_count=0,
        wall_seconds=t.elapsed,
        llm_calls=0,
        errors=[]))

    # 构造 PipelineResult
    diversity = compute_diversity_from_problems(problems)
    result = PipelineResult(
        seed_id=seed_id,
        phases=phase_stats_list,
        total_problems=len(problems),
        validated_count=validated,
        degraded_count=degraded,
        diversity=diversity,
        total_llm_calls=get_llm_stats()["calls"],
        total_wall_seconds=time.time() - wall_start,
        output_labels=labels,
    )

    print(f"\n完成！共 {len(problems)} 道题目入库 (validated={validated}, degraded={degraded})")
    print(f"  LLM 调用: {result.total_llm_calls} 次, 耗时: {result.total_wall_seconds:.1f}s")
    return problems, result


# ==================== 旧接口兼容 ====================


def generate_from_seed(json_path: str, num: int = 3, num_subs: int = 2,
                       num_soft_rewrites: int = 1, soft_rewrite_types: list = None,
                       cognitive_forms: list = None, generalization_axes: list = None,
                       form_changes: list = None,
                       cross_metric: bool = False, num_cross_metrics: int = 2,
                       output_dir: str = None, stem: str = None):
    """旧接口兼容：内部调用 fan_through。返回 (problems, PipelineResult)。"""
    return fan_through(
        json_path, cognitive_forms=cognitive_forms, generalization_axes=generalization_axes, num=num,
        num_subs=num_subs, num_soft=num_soft_rewrites,
        soft_rewrite_types=soft_rewrite_types, form_changes=form_changes,
        cross_metric=cross_metric, num_cross_metrics=num_cross_metrics,
        output_dir=output_dir, stem=stem)