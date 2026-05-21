"""新泛化 Pipeline：种子题目 → SymPy Fact Sheet → LLM 编题 → 度规替换"""

import json
import re
from dataclasses import asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from core.api_client import ask_ai
from core.cleaner import clean_problem
from core.config import MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC
from core.metric_library import METRIC_LIBRARY
from core.sympy_engine import compute_fact_sheet
from core.system_prompts import SYSTEM_PROMPT_COMPOSE, SYSTEM_PROMPT_SUBSTITUTE, SYSTEM_PROMPT_PICK_METRIC
from core.validator import validate_and_fix_loop
from schema import Problem, Metadata, PhysicalData, Origin

# 度规库描述：供 LLM 挑选时参考（聚焦张量计算与基本应用，不含引力波等高级专题）
_METRIC_DESCRIPTIONS = {
    "Schwarzschild": "静态球对称黑洞度规，真空解，Einstein 张量为零",
    "Minkowski": "平直时空度规（笛卡尔坐标），所有曲率量为零",
    "DeSitter": "de Sitter 度规，正宇宙学常数，Ricci 标量正常数",
    "AntiDeSitter": "anti-de Sitter 度规（球坐标），负宇宙学常数，Ricci 标量负常数",
    "AntiDeSitterStatic": "anti-de Sitter 静态坐标版本，Ricci 标量 R=-12",
    "MinkowskiCartesian": "Minkowski 平直时空（笛卡尔坐标），所有曲率为零",
    "MinkowskiPolar": "Minkowski 平直时空（球坐标），Christoffel 符号非零但曲率为零",
    "FLRW": "Friedmann-Lemaître-Robertson-Walker 宇宙度规，标度因子 a(t)",
}



def _pick_compatible_metrics_llm(problem_tags: dict, num_subs: int) -> list:
    """让 LLM 从度规库中挑选最适合替换的度规。"""
    current_metric = problem_tags.get("metric", "")
    # Build metric catalog (exclude heavy metrics)
    catalog_lines = []
    for name, desc in _METRIC_DESCRIPTIONS.items():
        data = METRIC_LIBRARY[name]
        heavy = data.get("heavy", False)
        if heavy:
            continue
        catalog_lines.append(f"- {name}: {desc}")
    catalog = "\n".join(catalog_lines)

    system = SYSTEM_PROMPT_PICK_METRIC.format(
        metric_catalog=catalog,
        current_metric=current_metric,
    )
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
        # Fallback: extract quoted strings
        names = re.findall(r'"(\w+)"', text)

    # Validate and fetch metric data
    result = []
    for name in names:
        if name in METRIC_LIBRARY and name != current_metric and not METRIC_LIBRARY[name].get("heavy", False):
            result.append(METRIC_LIBRARY[name])
        if len(result) >= num_subs:
            break

    # Fallback: if LLM returned fewer than needed, fill from remaining non-heavy, non-current metrics
    if len(result) < num_subs:
        for name, data in METRIC_LIBRARY.items():
            if name != current_metric and not data.get("heavy", False) and data not in result:
                result.append(data)
                if len(result) >= num_subs:
                    break

    return result


def _generate_one(seed_dict: dict, seq: int):
    """单次生成：用种子题的度规计算 Fact Sheet → LLM 自选方向编题（不改变度规）。

    Returns (Problem, fact_sheet_dict).
    """
    tags = seed_dict["metadata"]["tags"]
    if isinstance(tags, list):
        from core.system_prompts import TAG_KEYS
        tags = {k: v for k, v in zip(TAG_KEYS[:len(tags)], tags)}

    # Step 1: 获取 Fact Sheet（优先用缓存）
    cached_fs = seed_dict.get("cached_fact_sheet")
    if cached_fs and "error" not in cached_fs:
        print(f"  [{seq}] 使用缓存 Fact Sheet")
        fact_sheet = cached_fs
    else:
        print(f"  [{seq}] 计算 Fact Sheet...")
        from core.validator import _compute_fact_sheet_for_problem
        fact_sheet = _compute_fact_sheet_for_problem(seed_dict)
        if "error" in fact_sheet:
            raise ValueError(f"种子题度规 Fact Sheet 计算失败: {fact_sheet['error']}")
    print(f"  [{seq}] Fact Sheet 就绪, 开始编题...")

    # Step 2: LLM 编题（必须使用种子题的度规，自行选择泛化方向）
    seed_question = seed_dict["origin"]["question"]
    seed_target = seed_dict["physical_data"]["target"]
    seed_pd = seed_dict["physical_data"]
    prompt = (
        f"以下是该度规的完整几何属性数据，以及一道种子题目。\n\n"
        f"=== 几何属性数据 ===\n{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"=== 种子题目 ===\n"
        f"设问方向：{tags['target_object']}\n"
        f"求解目标：{seed_target}\n"
        f"题目原文：{seed_question}\n\n"
        f"=== 种子题的度规 ===\n"
        f"dimension: {seed_pd['dimension']}\n"
        f"variables: {seed_pd['variables']}\n"
        f"metric: {json.dumps(seed_pd['metric'], ensure_ascii=False)}\n\n"
        f"请基于这份几何属性数据，围绕种子题目的物理场景自行选择一个有意义的泛化方向，"
        f"编出一道后续延伸题目。\n"
        f"physical_data 必须原样使用种子题的度规（dimension、variables、metric），不要自己生成新度规。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_COMPOSE, model=MODEL_COMPOSE)

    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        text = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)
        data = json.loads(text)

    # Override metadata fields — not from LLM
    original_id = seed_dict["metadata"]["id"]
    data["metadata"]["id"] = f"{original_id}-{seq}"
    data["metadata"]["source"] = "generated"
    data["metadata"]["tools_used"] = ["EinsteinPy"]
    data["metadata"]["validated"] = False

    # Ensure tags is a dict
    if isinstance(data["metadata"]["tags"], list):
        from core.system_prompts import TAG_KEYS
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    # Force physical_data to use seed's metric (LLM may try to change it)
    data["physical_data"]["dimension"] = seed_pd["dimension"]
    data["physical_data"]["variables"] = seed_pd["variables"]
    data["physical_data"]["metric"] = seed_pd["metric"]
    data["physical_data"]["metric_sympy"] = seed_pd.get("metric_sympy")

    return (Problem(
        metadata=Metadata(**{k: v for k, v in data["metadata"].items() if k in Metadata.__dataclass_fields__}),
        physical_data=PhysicalData(**{k: v for k, v in data["physical_data"].items() if k in PhysicalData.__dataclass_fields__}),
        origin=Origin(**{k: v for k, v in data["origin"].items() if k in Origin.__dataclass_fields__}),
    ), fact_sheet)


def _substitute_metric(problem: Problem, original_fact_sheet: dict, new_metric: dict, seq: int) -> Problem:
    """将一道题目的度规替换为新度规，保持题目结构不变。"""
    metric_name = new_metric["name"]
    # Compute new Fact Sheet
    print(f"    [sub-{seq}] 计算 {metric_name} Fact Sheet...")
    new_fact_sheet = compute_fact_sheet(new_metric["metric"], new_metric["variables"])
    print(f"    [sub-{seq}] {metric_name} Fact Sheet 完成, 开始适配题目...")

    # LLM adapts the question
    prompt = (
        f"以下是一道已编写好的题目及其原始 Fact Sheet，以及一份新度规的 Fact Sheet。\n\n"
        f"=== 原题目 ===\n{json.dumps(asdict(problem), ensure_ascii=False, indent=2)}\n\n"
        f"=== 原度规 Fact Sheet ===\n{json.dumps(original_fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"=== 新度规 Fact Sheet ===\n{json.dumps(new_fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"请将原题目适配到新度规上。保持题目类型和结构不变，用新度规的数据替换原度规的数据。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_SUBSTITUTE, model=MODEL_SUBSTITUTE)

    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        text = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)
        data = json.loads(text)

    # Ensure tags is a dict
    if isinstance(data["metadata"]["tags"], list):
        from core.system_prompts import TAG_KEYS
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    # Override metadata fields
    original_id = problem.metadata.id
    data["metadata"]["id"] = f"{original_id}-s{seq}"
    data["metadata"]["source"] = "generated"
    data["metadata"]["tools_used"] = ["EinsteinPy"]
    data["metadata"]["validated"] = False
    # Override metric tag with actual metric library name
    data["metadata"]["tags"]["metric"] = new_metric["name"]

    # Save SymPy-format metric for validation
    data["physical_data"]["metric_sympy"] = new_metric["metric"]

    return Problem(
        metadata=Metadata(**{k: v for k, v in data["metadata"].items() if k in Metadata.__dataclass_fields__}),
        physical_data=PhysicalData(**{k: v for k, v in data["physical_data"].items() if k in PhysicalData.__dataclass_fields__}),
        origin=Origin(**{k: v for k, v in data["origin"].items() if k in Origin.__dataclass_fields__}),
    )


def generate_from_seed(json_path: str, num: int = 3, num_subs: int = 2,
                       output_dir: str = None, stem: str = None):
    """从种子题目生成多道新题，再对每道题用度规库替换度规。

    Args:
        json_path: 种子题目 JSON 文件路径
        num: 生成题目数量（不同方向）
        num_subs: 每道题的度规替换数量
        output_dir: 输出目录
        stem: 文件名前缀

    Returns list of (label, Problem).
    """
    with open(json_path, "r", encoding="utf-8") as f:
        seed_dict = json.load(f)

    if output_dir:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
    if not stem:
        stem = Path(json_path).stem

    # Phase 1: Generate questions (LLM chooses direction)
    print(f"=== Phase 1: 生成 {num} 道基础题 (LLM 自选方向) ===")
    tasks = [(seed_dict, i) for i in range(num)]

    def do_gen(task):
        seed_dict, seq = task
        problem, fact_sheet = _generate_one(seed_dict, seq)
        return (seq, problem, fact_sheet)

    base_problems = []
    base_fact_sheets = {}
    with ThreadPoolExecutor(max_workers=num) as pool:
        futures = {pool.submit(do_gen, t): t for t in tasks}
        for future in as_completed(futures):
            seq, problem, fact_sheet = future.result()
            base_problems.append((seq, problem))
            base_fact_sheets[seq] = fact_sheet
            # Validate-fix loop and save base problem
            label = f"{stem}_gen_{seq}"
            if output_dir:
                problem_dict = clean_problem(problem)
                problem_dict = validate_and_fix_loop(problem_dict, max_attempts=2)
                path = out / f"{label}.json"
                path.write_text(json.dumps(problem_dict, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"  已保存 {label}: {path} (validated={problem_dict['metadata']['validated']})")

    # Phase 2: Pick substitution metrics once, then substitute for each base problem
    print(f"\n=== Phase 2: 度规替换 ({num} × {num_subs} = {num * num_subs} 道) ===")
    total_subs_needed = num_subs  # 每道基础题用相同的度规集合
    seed_tags = seed_dict["metadata"]["tags"]
    if isinstance(seed_tags, list):
        from core.system_prompts import TAG_KEYS
        seed_tags = {k: v for k, v in zip(TAG_KEYS[:len(seed_tags)], seed_tags)}
    sub_metrics = _pick_compatible_metrics_llm(seed_tags, total_subs_needed)
    print(f"  替换度规: {[m['name'] for m in sub_metrics]}")

    sub_tasks = []
    sub_seq = 0
    for seq, problem in base_problems:
        for metric in sub_metrics:
            sub_seq += 1
            sub_tasks.append((problem, base_fact_sheets[seq], metric, sub_seq))

    def do_sub(task):
        problem, fact_sheet, metric, sub_seq = task
        new_problem = _substitute_metric(problem, fact_sheet, metric, sub_seq)
        return (sub_seq, metric["name"], new_problem)

    sub_results = []
    with ThreadPoolExecutor(max_workers=len(sub_tasks)) as pool:
        futures = {pool.submit(do_sub, t): t for t in sub_tasks}
        for future in as_completed(futures):
            sub_seq, metric_name, problem = future.result()
            sub_results.append((sub_seq, metric_name, problem))
            if output_dir:
                label = f"{stem}_sub_{sub_seq}_{metric_name}"
                problem_dict = clean_problem(problem)
                problem_dict = validate_and_fix_loop(problem_dict, max_attempts=2)
                path = out / f"{label}.json"
                path.write_text(json.dumps(problem_dict, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"  已保存 {label}: {path} (validated={problem_dict['metadata']['validated']})")

    print(f"完成！共 {len(base_problems)} 道基础题 + {len(sub_results)} 道度规替换题")
    return base_problems + sub_results