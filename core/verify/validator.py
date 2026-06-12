"""验证与修正模块：SymPy metric_check + LLM judge(red-team找错) + LLM fix"""

import json
import re

from core.common.api_client import ask_ai
from core.common.cleaner import _clean_value
from core.common.config import MODEL_VALIDATE, MODEL_JUDGE, MODEL_RED_TEAM, MODEL_FIX
from core.common.constants import TAG_KEYS
from core.common.metric_library import METRIC_LIBRARY
from core.common.sympy_engine import compute_fact_sheet
from core.verify.prompts import SYSTEM_PROMPT_JUDGE, SYSTEM_PROMPT_RED_TEAM, SYSTEM_PROMPT_FIX
from schema import StructuralCheck, MetricCheck, JudgeCheck, RedTeamCheck, Verification


def _latex_to_sympy(latex_str: str) -> str:
    """将 LaTeX 度规分量转换为 SymPy 格式字符串。"""

    import sympy
    from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

    s = latex_str.strip()
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1]

    # 处理 JSON 双重转义：\\frac → \frac, \\theta → \theta
    s = s.replace("\\\\frac", "\\frac")
    s = s.replace("\\\\sin", "\\sin")
    s = s.replace("\\\\cos", "\\cos")
    s = s.replace("\\\\tan", "\\tan")
    s = s.replace("\\\\theta", "\\theta")
    s = s.replace("\\\\phi", "\\phi")
    s = s.replace("\\\\left", "\\left")
    s = s.replace("\\\\right", "\\right")

    # First try: parse LaTeX directly with sympy's latex parser
    try:
        from sympy.parsing.latex import parse_latex
        expr = parse_latex(s)
        return str(expr)
    except Exception:
        pass
    # Second try: regex conversion then implicit-multiplication parse
    s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', s)
    s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', s)  # 嵌套 \frac 的第二次处理
    s = re.sub(r'\\sin', 'sin', s)
    s = re.sub(r'\\cos', 'cos', s)
    s = re.sub(r'\\tan', 'tan', s)
    s = re.sub(r'\\cot', 'cot', s)
    s = re.sub(r'\\theta', 'theta', s)
    s = re.sub(r'\\phi', 'phi', s)
    s = re.sub(r'\\left', '', s)
    s = re.sub(r'\\right', '', s)
    s = s.replace("^", "**")
    try:
        transformations = standard_transformations + (implicit_multiplication_application,)
        expr = parse_expr(s, transformations=transformations)
        return str(expr)
    except Exception:
        raise ValueError(f"无法将 LaTeX 转为 SymPy: {latex_str[:60]}")


def _get_metric_sympy(problem_dict: dict) -> tuple:
    """从题目数据中获取 SymPy 格式度规矩阵和变量列表。

    优先级：
    1. 题目已有 metric_sympy 字段（直接使用）
    2. tags.metric 在度规库中（从库取）
    3. _match_metric_name 匹配到度规库（从库取）
    4. 从 LaTeX metric 转换（最不可靠，可能失败）
    """
    pd = problem_dict["physical_data"]

    # 1. 已有 metric_sympy
    if pd.get("metric_sympy"):
        return pd["metric_sympy"], pd["variables"]

    # 2+3. 从度规库取（先查 tags.metric，再查 _match_metric_name）
    metric_name = problem_dict["metadata"]["tags"].get("metric", "")
    if metric_name not in METRIC_LIBRARY or metric_name == "metric":
        metric_name = _match_metric_name(problem_dict)
    if metric_name and metric_name in METRIC_LIBRARY:
        data = METRIC_LIBRARY[metric_name]
        return data["metric"], data["variables"]

    # 4. 从 LaTeX 转换（可能失败）
    if pd.get("metric"):
        try:
            metric_latex = pd["metric"]
            metric_sympy = []
            for row in metric_latex:
                sympy_row = []
                for cell in row:
                    if cell in ("$0$", "$0$"):
                        sympy_row.append("0")
                    else:
                        sympy_row.append(_latex_to_sympy(cell))
                metric_sympy.append(sympy_row)

            vars_clean = [v.strip("$").strip() for v in pd["variables"]]
            pd["metric_sympy"] = metric_sympy
            return metric_sympy, vars_clean
        except ValueError as e:
            raise ValueError(f"LaTeX 度规转 SymPy 失败，且无法匹配度规库: {e}")

    raise ValueError(f"无法获取 SymPy 格式度规")


def _match_metric_name(problem_dict: dict) -> str:
    """尝试识别题目对应的度规库名称。

    优先级：
    1. tags.metric 如果是有效的度规库名（非占位符）
    2. physics_env 如果是有效的度规库名
    3. 根据 metric_sympy 对角分量精确匹配度规库
    4. 将 LaTeX 对角分量转为 SymPy 后匹配度规库
    5. 返回空字符串（无法识别）
    """
    # 来源 1: tags.metric
    tags_metric = problem_dict["metadata"]["tags"].get("metric", "")
    if tags_metric and tags_metric in METRIC_LIBRARY and tags_metric != "metric":
        return tags_metric

    # 来源 2: physics_env
    physics_env = problem_dict["metadata"].get("physics_env", "")
    if physics_env and physics_env in METRIC_LIBRARY:
        return physics_env

    pd = problem_dict["physical_data"]
    dim = pd.get("dimension", 4)

    # 来源 3: 根据 metric_sympy 对角分量匹配
    metric_sympy = pd.get("metric_sympy")
    if metric_sympy:
        diag_strings = [str(metric_sympy[i][i]).strip() for i in range(dim)]
        match = _match_diag_against_library(diag_strings, dim)
        if match:
            return match

    # 来源 4: 将 LaTeX 对角分量转为 SymPy 后匹配
    metric_latex = pd.get("metric")
    if metric_latex:
        try:
            diag_strings = []
            for i in range(dim):
                cell = metric_latex[i][i].strip()
                if cell in ("$0$", "$0$"):
                    diag_strings.append("0")
                else:
                    diag_strings.append(_latex_to_sympy(cell))
            match = _match_diag_against_library(diag_strings, dim)
            if match:
                return match
        except ValueError:
            pass  # 转换失败 → 无法通过此途径匹配

    return ""


def _match_diag_against_library(diag_strings: list, dim: int) -> str:
    """将一组对角分量字符串与度规库匹配，返回最佳匹配的度规名。"""
    best_match = ""
    best_score = 0

    for name, data in METRIC_LIBRARY.items():
        lib_vars = data["variables"]
        lib_metric = data["metric"]

        if dim != len(lib_vars):
            continue

        diag_matches = 0
        for i in range(dim):
            val_a = diag_strings[i]
            val_b = str(lib_metric[i][i]).strip()
            if val_a == val_b:
                diag_matches += 1

        score = diag_matches / dim
        if score > best_score and score >= 0.5:
            best_score = score
            best_match = name

    return best_match


def _compute_fact_sheet_for_problem(problem_dict: dict) -> dict:
    """为题目计算 Fact Sheet，用于验证。

    优先从度规库缓存读取；缓存不可用时回退到实时计算。
    会自动尝试从度规矩阵匹配度规库名称（LLM 可能给出错误的 tags.metric）。
    """
    # 识别度规名（可能需要从矩阵内容推断）
    metric_name = _match_metric_name(problem_dict)

    # 尝试从缓存读取（度规名在库中时）
    if metric_name and metric_name in METRIC_LIBRARY:
        from core.common.fact_sheet_cache import get_cached_fact_sheet
        cached = get_cached_fact_sheet(metric_name)
        if cached is not None and "error" not in cached:
            if metric_name != problem_dict["metadata"]["tags"].get("metric", ""):
                print(f"  度规名识别: tags.metric='{problem_dict['metadata']['tags'].get('metric', '')}' → 实际匹配='{metric_name}'")
            return cached

    # 缓存不可用 → 实时计算（传入匹配到的 metric_name）
    try:
        metric_sympy, variables = _get_metric_sympy(problem_dict)
    except ValueError as e:
        return {"error": str(e)}

    vars_clean = [v.strip("$").strip() for v in variables]
    try:
        if metric_name:
            print(f"  度规名识别: tags.metric='{problem_dict['metadata']['tags'].get('metric', '')}' → 实际匹配='{metric_name}'")
        return compute_fact_sheet(metric_sympy, vars_clean, metric_name=metric_name)
    except Exception as e:
        return {"error": f"Fact Sheet 计算失败: {e}"}


# ==================== 结构检查 ====================


def structural_check(problem_dict: dict) -> StructuralCheck:
    """结构完整性检查：字段齐全、answer非空、度规完整"""
    issues = []

    # 必须有 question
    q = problem_dict["origin"].get("question", "")
    if not q or len(q) < 10:
        issues.append("question 为空或过短")

    # answer 不能是空字符串（可以是 NO_ANSWER / "无答案"，但不能是 ""）
    a = problem_dict["origin"].get("answer", "")
    if a == "":
        issues.append("answer 为空字符串（应使用 NO_ANSWER）")

    # 度规：有度规数据或度规库名则 OK；抽象题（无度规概念题）允许缺度规
    pd = problem_dict["physical_data"]
    if not pd.get("metric") and not pd.get("metric_sympy"):
        metric_name = problem_dict["metadata"]["tags"].get("metric", "")
        if metric_name not in METRIC_LIBRARY:
            # 某些标签（如 killing_vector, metric）代表抽象概念而非具体度规
            abstract_tags = {"killing_vector", "metric", "general"}
            problem_type = problem_dict["metadata"].get("type", "")
            cognitive_form = problem_dict["metadata"].get("cognitive_form", "")
            if metric_name not in abstract_tags and problem_type not in ("prove", "concept"):
                issues.append("度规缺失且不在度规库中")

    # target 必须有
    if not pd.get("target"):
        issues.append("target 为空")

    # dimension 必须有
    if not pd.get("dimension"):
        issues.append("dimension 为空")

    return StructuralCheck(ok=len(issues) == 0, issues=issues)


# ==================== SymPy 度规检查 ====================


def metric_check(problem_dict: dict, fact_sheet: dict) -> MetricCheck:
    """SymPy 度规几何量验证

    检查 Fact Sheet 中关键几何量是否符合物理预期：
    - 真空度规：Ricci 张量=0, Einstein 张量=0
    - de Sitter / anti-de Sitter：Ricci 标量为常数
    - Schwarzschild：真空但有非零 Kretschmann 标量
    """
    metric_name = problem_dict["metadata"]["tags"].get("metric", "")
    checker_name = f"sympy_verify.{metric_name.lower()}_check"

    details = {}

    # 从 Fact Sheet 提取关键量
    ricci_scalar = fact_sheet.get("ricci_scalar")
    kretschmann = fact_sheet.get("kretschmann")

    # 预期值检查
    expected_checks = _get_expected_checks(metric_name)

    all_ok = True
    for key, expected in expected_checks.items():
        actual = fact_sheet.get(key)
        # 空 dict 表示"所有分量为零（没有非零分量需要报告）"
        # 这对真空度规的 ricci_tensor / einstein_tensor 是正确结果
        if actual is not None:
            if isinstance(actual, dict) and expected == 0:
                is_ok = (len(actual) == 0)  # 空 dict = 所有分量为零
                details[key] = is_ok
                if not is_ok:
                    all_ok = False
            else:
                try:
                    if expected == 0:
                        is_ok = _is_zero(actual)
                    elif isinstance(expected, str):
                        is_ok = str(actual) == expected
                    else:
                        is_ok = abs(float(actual) - float(expected)) < 1e-10
                    details[key] = is_ok
                    if not is_ok:
                        all_ok = False
                except (ValueError, TypeError):
                    details[key] = False
                    all_ok = False

    return MetricCheck(
        checker=checker_name,
        status="ok" if all_ok else "fail",
        details=details,
    )


def _get_expected_checks(metric_name: str) -> dict:
    """返回度规名称对应的预期几何量"""
    # 真空度规
    vacuum_metrics = ["Schwarzschild", "Minkowski", "MinkowskiCartesian", "MinkowskiPolar"]
    # de Sitter 族
    desitter_metrics = {"DeSitter": "12", "AntiDeSitter": "-12", "AntiDeSitterStatic": "-12"}

    expected = {}

    if metric_name in vacuum_metrics:
        expected["ricci_scalar"] = 0
        expected["ricci_tensor"] = 0  # 所有分量应为零
        expected["einstein_tensor"] = 0  # 所有分量应为零
    elif metric_name in desitter_metrics:
        expected["ricci_scalar"] = desitter_metrics[metric_name]
    elif metric_name == "FLRW":
        # FLRW 的 Ricci 标量取决于 a(t)，无法固定预期
        pass
    # 其他度规不做自动预期检查

    return expected


def _build_metric_summary(problem_dict: dict, fact_sheet: dict) -> str:
    """从 Fact Sheet 中提取简短的度规摘要（含 Christoffel 符号对照表），替代完整 Fact Sheet 发给 judge/red_team/fix。

    完整 Fact Sheet 包含 christoffel 3×4×4、riemann 4×4×4×4 等巨量数据，
    LLM 实际只会利用度规的分类信息、关键标量和题目中涉及的 Christoffel 符号。
    摘要保留这些关键信息，并筛选题目 solution 中引用的 Christoffel 分量，
    大幅减少 prompt token，降低 504 超时风险。
    """
    metric_name = _match_metric_name(problem_dict)
    tags_metric = problem_dict["metadata"]["tags"].get("metric", "")
    actual_name = metric_name or tags_metric or "未知"

    lines = [f"度规: {actual_name}"]

    # 从 Fact Sheet 提取关键标量
    if fact_sheet:
        # Convention note
        cn = fact_sheet.get("convention_note")
        if cn:
            lines.append(f"约定: {cn}")

        # Ricci 标量（简短形式）
        rs = fact_sheet.get("ricci_scalar")
        if rs is not None:
            rs_str = str(rs).strip()
            # 如果太长，只写描述而非完整表达式
            if len(rs_str) > 30:
                # 判断是否是简单的数值
                try:
                    float(rs_str)
                    lines.append(f"Ricci 标量: {rs_str}")
                except (ValueError, TypeError):
                    lines.append(f"Ricci 标量: 依赖度规参数（非常数）")
            else:
                lines.append(f"Ricci 标量: {rs_str}")

        # 真空/非真空信息
        # ricci_tensor 在 Fact Sheet 中是 flat dict {"R_00": "...", ...}，
        # 真空度规时为空 dict {}（所有分量=0 不记录）
        ricci_tensor = fact_sheet.get("ricci_tensor")
        einstein_tensor = fact_sheet.get("einstein_tensor")
        if ricci_tensor is not None:
            # 空 dict → 真空（所有分量为零，没有非零分量需要记录）
            if not ricci_tensor:  # {} 表示所有 Ricci 分量为零
                lines.append("真空度规: Ricci 张量全为零")
                if einstein_tensor is not None and not einstein_tensor:
                    lines.append("真空度规: Einstein 张量全为零")
            else:
                lines.append("非真空度规: Ricci 张量非零")

        # Killing 矢量数量
        kv = fact_sheet.get("killing_vectors")
        if kv:
            n_kv = len(kv)
            lines.append(f"Killing 矢量: {n_kv} 个")

        # Kretschmann 标量（简短形式）
        # 注意：sympy_engine.py 中 key 是 "kretschmann"，不是 "kretschmann_scalar"
        ks = fact_sheet.get("kretschmann")
        if ks is not None:
            ks_str = str(ks).strip()
            if len(ks_str) > 30:
                lines.append(f"Kretschmann 标量: 依赖度规参数")
            else:
                lines.append(f"Kretschmann 标量: {ks_str}")

        # Christoffel 符号对照表（筛选题目中引用的分量 + 常用分量）
        christoffel = fact_sheet.get("christoffel")
        if christoffel:
            # 收集题目 solution 中引用的 Christoffel 分量
            solution = problem_dict["origin"].get("solution", "") or ""
            question = problem_dict["origin"].get("question", "") or ""
            combined = question + solution

            # 提取 solution 中出现的 Gamma 指标模式（如 Gamma^1_{00}, Γ^0_{01} 等）
            # 也包含常用分量（Gamma^1_{00} 对 Schwarzschild 静态观察者、Gamma^0_{01} 等）
            referenced_keys = set()

            # 从 solution 中提取引用的 Christoffel 分量
            # 匹配多种格式：Gamma^1_{00}, Gamma^{1}_{00}, \Gamma^1_{00}, Γ^1_{00}
            # 在 JSON 中 LaTeX 反斜杠是双写的，所以也匹配 \\Gamma
            # 格式A: Gamma^i_{jk} 或 Gamma^{i}_{jk}（带花括号的下标）— 最常见 LaTeX 格式
            for match in re.finditer(r'Gamma\^?(\d)_{(\d)(\d)}', combined):
                referenced_keys.add(f"Gamma^{match.group(1)}_{match.group(2)}{match.group(3)}")
            # 格式B: Gamma^i_jk 或 Gamma^{i}_jk（不带花括号的下标）
            for match in re.finditer(r'Gamma\^?(\d)_(\d)(\d)', combined):
                referenced_keys.add(f"Gamma^{match.group(1)}_{match.group(2)}{match.group(3)}")
            # 格式C: Unicode Γ^i_{jk}
            for match in re.finditer(r'Γ\^?(\d)_{(\d)(\d)}', combined):
                referenced_keys.add(f"Gamma^{match.group(1)}_{match.group(2)}{match.group(3)}")
            for match in re.finditer(r'Γ\^?(\d)_(\d)(\d)', combined):
                referenced_keys.add(f"Gamma^{match.group(1)}_{match.group(2)}{match.group(3)}")

            # 常用分量（不论 solution 是否引用）
            common_keys = {"Gamma^1_{00}", "Gamma^0_{01}", "Gamma^1_{11}",
                           "Gamma^1_{22}", "Gamma^1_{33}", "Gamma^2_{12}",
                           "Gamma^3_{13}", "Gamma^3_{23}", "Gamma^2_{33}"}
            relevant_keys = referenced_keys | common_keys

            # 筛选出 Fact Sheet 中有值的分量
            christoffel_lines = []
            for key in sorted(relevant_keys):
                if key in christoffel:
                    christoffel_lines.append(f"  {key} = {christoffel[key]}")

            if christoffel_lines:
                lines.append("Christoffel 符号对照表（SymPy 精确计算，具有最高可信度）：")
                lines.extend(christoffel_lines)

    return "\n".join(lines)


def _is_zero(value) -> bool:
    """判断一个值是否为零（允许浮点误差和表达式形式）"""
    if value is None:
        return True
    s = str(value).strip()
    if s == "0" or s == "0.0" or s == "-0":
        return True
    try:
        return abs(float(s)) < 1e-10
    except (ValueError, TypeError):
        # 表达式形式（如 SymPy 表达式），尝试解析
        return "0" == s


# ==================== LLM Judge（找错） ====================


def judge_problem(problem_dict: dict, fact_sheet: dict) -> JudgeCheck:
    """LLM judge：adversarial 找错验证

    Args:
        problem_dict: 题目的 dict 表示
        fact_sheet: 已计算的 Fact Sheet（用于生成摘要）

    Returns: JudgeCheck (correct, self_contained, training_value, issue)
    """
    summary = _build_metric_summary(problem_dict, fact_sheet)
    print(f"    Judge 找错 (模型: {MODEL_JUDGE})...")
    prompt = (
        f"以下是该度规的关键信息摘要：\n{summary}\n\n"
        f"以下是该题目的完整内容：\n"
        f"question: {problem_dict['origin'].get('question', '')}\n"
        f"answer: {problem_dict['origin'].get('answer', '')}\n"
        f"solution: {problem_dict['origin'].get('solution', 'null')}\n\n"
        f"请审查该题目，找出所有错误和缺陷。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_JUDGE, model=MODEL_JUDGE)

    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        # Fallback: extract key fields with regex
        correct_match = re.search(r'"correct"\s*:\s*(true|false)', text)
        self_contained_match = re.search(r'"self_contained"\s*:\s*(true|false)', text)
        tv_match = re.search(r'"training_value"\s*:\s*([\d.]+)', text)
        issue_match = re.search(r'"issue"\s*:\s*"([^"]*)"', text)

        result = {
            "correct": correct_match.group(1) == "true" if correct_match else False,
            "self_contained": self_contained_match.group(1) == "true" if self_contained_match else False,
            "training_value": float(tv_match.group(1)) if tv_match else 0.0,
            "issue": issue_match.group(1) if issue_match else f"LLM 返回无法解析: {text[:100]}",
        }

    return JudgeCheck(
        correct=result.get("correct", False),
        self_contained=result.get("self_contained", False),
        training_value=result.get("training_value", 0.0),
        issue=result.get("issue", ""),
    )


# ==================== LLM Red-Team（极端找错） ====================


def red_team_problem(problem_dict: dict, fact_sheet: dict) -> RedTeamCheck:
    """LLM red-team：adversarial 攻击，尝试推翻题目

    Args:
        problem_dict: 题目的 dict 表示
        fact_sheet: 已计算的 Fact Sheet（用于生成摘要）

    Returns: RedTeamCheck (survives, flaw)
    """
    summary = _build_metric_summary(problem_dict, fact_sheet)
    print(f"    Red-team 攻击 (模型: {MODEL_RED_TEAM})...")
    prompt = (
        f"以下是该度规的关键信息摘要：\n{summary}\n\n"
        f"以下是该题目：\n"
        f"question: {problem_dict['origin'].get('question', '')}\n"
        f"answer: {problem_dict['origin'].get('answer', '')}\n"
        f"solution: {problem_dict['origin'].get('solution', 'null')}\n\n"
        f"请对这道题目发起最严厉的质疑，尝试找出任何缺陷来推翻它。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_RED_TEAM, model=MODEL_RED_TEAM)

    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        survives_match = re.search(r'"survives"\s*:\s*(true|false)', text)
        flaw_match = re.search(r'"flaw"\s*:\s*"([^"]*)"', text)

        result = {
            "survives": survives_match.group(1) == "true" if survives_match else False,
            "flaw": flaw_match.group(1) if flaw_match else f"LLM 返回无法解析: {text[:100]}",
        }

    return RedTeamCheck(
        survives=result.get("survives", False),
        flaw=result.get("flaw", ""),
    )


# ==================== 综合验证 ====================


def full_validate(problem_dict: dict, fact_sheet: dict = None) -> Verification:
    """对题目执行完整验证流程：structural → metric_check → judge → red_team

    Args:
        problem_dict: 题目 dict
        fact_sheet: 外部传入的 Fact Sheet（None 时自动计算；空 dict {} 时跳过 metric_check）
    """
    # Step 0: Fact Sheet
    if fact_sheet is not None:
        # 外部传入（空 dict {} = 无度规题，跳过 metric_check）
        fs = fact_sheet
    else:
        fs = _compute_fact_sheet_for_problem(problem_dict)
        if "error" in fs:
            return Verification(
                structural=StructuralCheck(ok=False, issues=[fs["error"]]),
                metric_check=MetricCheck(checker="none", status="skip"),
            )

    # Step 1: 结构检查
    structural = structural_check(problem_dict)
    if not structural.ok:
        print(f"    结构检查失败: {structural.issues}")
        return Verification(structural=structural)

    # Step 2: SymPy 度规检查（空 fact_sheet 时跳过）
    if fs:
        metric = metric_check(problem_dict, fs)
    else:
        metric = MetricCheck(checker="none", status="skip")
        print("    [无度规题] 跳过 metric_check")

    # Step 3: LLM judge（找错）
    judge = judge_problem(problem_dict, fs)

    # Step 4: LLM red-team（如果 judge 通过才做，否则跳过）
    red_team = None
    if judge.correct and judge.self_contained:
        red_team = red_team_problem(problem_dict, fs)

    return Verification(
        structural=structural,
        metric_check=metric,
        judge=judge,
        red_team=red_team,
    )


def is_verification_ok(verification: Verification) -> bool:
    """判断验证是否全部通过

    通过条件：structural.ok=True AND metric_check.status=ok AND judge.correct=True AND (red_team.survives=True 或 red_team=None)
    """
    if verification is None:
        return False

    if verification.structural and not verification.structural.ok:
        return False

    if verification.metric_check and verification.metric_check.status == "fail":
        return False

    if verification.judge and not verification.judge.correct:
        return False

    if verification.red_team and verification.red_team.survives is False:
        return False

    return True


# ==================== Fix ====================


def _parse_llm_json_lazy(text: str) -> dict:
    """延迟导入 _parse_llm_json（避免 core.scale.pipeline ↔ core.verify.validator 循环导入）。"""
    from core.scale.pipeline import _parse_llm_json
    return _parse_llm_json(text)


def fix_problem(problem_dict: dict, fact_sheet: dict, issues: list,
                temperature: float = None) -> dict:
    """根据 issues 修正题目的 answer/solution。

    Returns the fixed dict (metadata and physical_data.metric_sympy are preserved).
    """
    summary = _build_metric_summary(problem_dict, fact_sheet)
    print(f"    修正中 (模型: {MODEL_FIX}, issues: {len(issues)} 条)...")
    prompt = (
        f"以下是该度规的关键信息摘要：\n{summary}\n\n"
        f"以下是当前题目的完整内容：\n"
        f"{json.dumps(problem_dict, ensure_ascii=False, indent=2)}\n\n"
        f"以下是审查者发现的具体错误：\n"
        f"{json.dumps(issues, ensure_ascii=False, indent=2)}\n\n"
        f"请根据上述信息修正错误。只修正 answer、solution，不改度规和设问方向。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_FIX, model=MODEL_FIX, temperature=temperature)

    data = _parse_llm_json_lazy(response)

    # Preserve fields that must not be changed
    data["metadata"]["id"] = problem_dict["metadata"]["id"]
    data["metadata"]["source"] = problem_dict["metadata"]["source"]
    data["metadata"]["validated"] = problem_dict["metadata"]["validated"]
    # Preserve new schema fields (LLM may not produce them)
    for key in ["source_id", "source_type", "stage", "lineage", "topic",
                "concepts", "cognitive_form", "physics_env", "soft_variant",
                "training_value"]:
        if key in problem_dict["metadata"] and key not in data["metadata"]:
            data["metadata"][key] = problem_dict["metadata"][key]
    data["physical_data"]["metric_sympy"] = problem_dict["physical_data"].get("metric_sympy")

    # Ensure tags is a dict, and clean "key:value" pollution
    if isinstance(data["metadata"]["tags"], list):
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    tags = data["metadata"]["tags"]
    if isinstance(tags, dict):
        for key in list(tags.keys()):
            val = tags[key]
            if isinstance(val, str) and ":" in val:
                prefix = val.split(":")[0]
                if prefix in TAG_KEYS:
                    tags[key] = val[len(prefix) + 1:].strip()

    return data


# ==================== 旧接口兼容 ====================


def validate_problem(problem_dict: dict, fact_sheet: dict = None) -> dict:
    """旧兼容接口：返回 {verified, issues, fact_sheet} 格式

    内部调用 full_validate()，然后转换为旧格式。
    """
    if fact_sheet is None:
        fact_sheet = _compute_fact_sheet_for_problem(problem_dict)
    if "error" in fact_sheet:
        return {"verified": False, "issues": [fact_sheet["error"]], "fact_sheet": None}

    # 如果 answer 是"无答案"，标记为不可解
    answer = problem_dict["origin"].get("answer", "")
    if answer and "无答案" in answer:
        return {"verified": False, "issues": ["题目 answer 为无答案，问题本身不可解"], "fact_sheet": fact_sheet}

    verification = full_validate(problem_dict)

    # 转换为旧格式
    ok = is_verification_ok(verification)
    issues = []
    if verification.judge and not verification.judge.correct:
        issues.append(f"judge: {verification.judge.issue}")
    if verification.metric_check and verification.metric_check.status == "fail":
        issues.append(f"metric_check 失败: {verification.metric_check.details}")
    if verification.red_team and verification.red_team.survives is False:
        issues.append(f"red_team: {verification.red_team.flaw}")
    if verification.structural and not verification.structural.ok:
        issues.extend(verification.structural.issues)

    return {"verified": ok, "issues": issues, "fact_sheet": fact_sheet}


def validate_and_fix_loop(problem_dict: dict, max_attempts: int = 1,
                          base_temperature: float = None) -> dict:
    """验证题目，如果失败则修正并重新验证，循环直到通过或达到最大次数。

    每次修正时温度逐步升高：attempt 0 用 base_temperature，attempt 1 用 base_temperature+0.2，
    attempt 2 用 base_temperature+0.4，以此类推。通过更高温度引入随机性来跳出相同错误。

    Returns the final dict (may be modified from fix attempts).
    """
    # Compute Fact Sheet once (reuse in all iterations)
    # 无度规题目：Fact Sheet 为空 dict（跳过 metric_check），但仍执行 judge/red_team
    pd = problem_dict.get("physical_data", {})
    has_metric = pd.get("metric") is not None or pd.get("metric_sympy") is not None
    metric_tag = problem_dict["metadata"]["tags"].get("metric", "")

    if not has_metric and metric_tag not in METRIC_LIBRARY:
        # 无度规数据且不在度规库中 → 空 Fact Sheet，仅做 judge/red_team
        fact_sheet = {}
        print("  [无度规题] 跳过 metric_check，仅执行 judge + red_team")
    else:
        fact_sheet = _compute_fact_sheet_for_problem(problem_dict)
        if "error" in fact_sheet:
            problem_dict["metadata"]["validated"] = False
            problem_dict["metadata"]["degraded"] = True
            problem_dict["verification"] = {"error": fact_sheet["error"], "attempt": 0}
            return problem_dict

    # 如果 answer 是"无答案"，不尝试修正
    answer = problem_dict["origin"].get("answer", "")
    if answer and "无答案" in answer:
        problem_dict["metadata"]["validated"] = False
        problem_dict["metadata"]["degraded"] = False  # NO_ANSWER 是正常状态，不算 degraded
        return problem_dict

    for attempt in range(max_attempts + 1):
        verification = full_validate(problem_dict, fact_sheet=fact_sheet)

        ok = is_verification_ok(verification)

        # 收集所有 issue 用于修正
        issues = []
        if verification.judge and not verification.judge.correct:
            issues.append(f"judge 发现错误: {verification.judge.issue}")
        if verification.metric_check and verification.metric_check.status == "fail":
            issues.append(f"metric_check 失败: {verification.metric_check.details}")
        if verification.red_team and verification.red_team.survives is False:
            issues.append(f"red_team 发现缺陷: {verification.red_team.flaw}")
        if verification.structural and not verification.structural.ok:
            issues.extend(verification.structural.issues)

        # 记录 verification 到 problem_dict（如实记录哪层跑了/没跑）
        problem_dict["verification"] = _verification_to_flat_dict(verification, attempt=attempt)

        if ok:
            problem_dict["metadata"]["validated"] = True
            problem_dict["metadata"]["degraded"] = False
            if "EinsteinPy" not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append("EinsteinPy")
            validate_model_tag = f"judge:{MODEL_JUDGE}+red_team:{MODEL_RED_TEAM}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            print(f"  验证通过 (attempt {attempt})")
            return problem_dict

        print(f"  验证失败 (attempt {attempt}): {issues[:3]}...")

        # If no specific issues, can't fix — stop (degraded)
        if not issues:
            problem_dict["metadata"]["validated"] = False
            problem_dict["metadata"]["degraded"] = True
            validate_model_tag = f"judge:{MODEL_JUDGE}+red_team:{MODEL_RED_TEAM}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            return problem_dict

        # If we've exhausted attempts, stop (degraded)
        if attempt >= max_attempts:
            problem_dict["metadata"]["validated"] = False
            problem_dict["metadata"]["degraded"] = True
            if "EinsteinPy" not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append("EinsteinPy")
            validate_model_tag = f"judge:{MODEL_JUDGE}+red_team:{MODEL_RED_TEAM}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            print(f"  达到最大修正次数 {max_attempts}，标记为 degraded")
            return problem_dict

        # Fix the problem with escalating temperature
        fix_temp = base_temperature
        if fix_temp is not None:
            fix_temp = fix_temp + 0.2 * attempt  # 每次重跑温度+0.2
        print(f"  修正中 (attempt {attempt + 1}, temp={fix_temp or 'default'})...")
        try:
            fixed = fix_problem(problem_dict, fact_sheet, issues, temperature=fix_temp)
            # Clean the fixed origin (but preserve metric_sympy)
            fixed["origin"] = _clean_value(fixed["origin"])
            # If answer is "无答案", force solution to None
            answer = fixed["origin"].get("answer", "")
            if answer and "无答案" in answer:
                fixed["origin"]["solution"] = None
            problem_dict = fixed
        except Exception as e:
            print(f"  修正失败: {e}")
            problem_dict["metadata"]["validated"] = False
            return problem_dict

    return problem_dict


def _verification_to_flat_dict(verification: Verification, attempt: int = 0) -> dict:
    """将 Verification 对象转为 flat dict，如实记录每层是否跑过。

    每层加 ran=True/False 标记，不默认填 ok=True。
    """
    result = {"attempt": attempt}

    # structural: 始终跑
    if verification.structural:
        result["structural"] = {
            "ok": verification.structural.ok,
            "ran": True,
        }
        if verification.structural.issues:
            result["structural"]["issues"] = verification.structural.issues
    else:
        result["structural"] = {"ok": False, "ran": False}

    # metric_check: 只在 structural.ok=True 时跑
    if verification.metric_check:
        result["metric_check"] = {
            "checker": verification.metric_check.checker or "",
            "status": verification.metric_check.status or "skip",
            "ran": True,
        }
        if verification.metric_check.details:
            for k, v in verification.metric_check.details.items():
                result["metric_check"][k] = v
    else:
        result["metric_check"] = {"checker": "", "status": "skip", "ran": False}

    # judge: 始终跑（如果 structural.ok=True）
    if verification.judge:
        result["judge"] = {
            "correct": verification.judge.correct,
            "self_contained": verification.judge.self_contained,
            "training_value": verification.judge.training_value,
            "issue": verification.judge.issue,
            "ran": True,
        }
    else:
        result["judge"] = {"correct": False, "ran": False, "issue": "structural check failed, judge skipped"}

    # red_team: 只在 judge.correct=True 且 self_contained=True 时跑
    if verification.red_team:
        result["red_team"] = {
            "survives": verification.red_team.survives,
            "flaw": verification.red_team.flaw,
            "ran": True,
        }
    else:
        # judge 没通过 → red_team 没跑，标记为未运行而非不通过
        result["red_team"] = {"survives": None, "ran": False, "flaw": "judge did not pass, red_team skipped"}

    # stage_eval
    if verification.stage_eval:
        result["stage_eval"] = {
            "ok": verification.stage_eval.ok,
            "score": verification.stage_eval.score,
            "ran": True,
        }

    return result


def validate_json_file(path: str) -> dict:
    """读取 JSON 文件，验证+修正，更新 validated 和 tools_used，保存回文件。"""
    from pathlib import Path

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    result = validate_and_fix_loop(raw)

    Path(path).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result