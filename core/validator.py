"""验证与修正模块：用 EinsteinPy 重算 Fact Sheet + LLM 验证/修正答案"""

import json
import re

from core.api_client import ask_ai
from core.cleaner import _clean_value
from core.config import MODEL_VALIDATE, MODEL_FIX
from core.metric_library import METRIC_LIBRARY
from core.sympy_engine import compute_fact_sheet
from core.system_prompts import SYSTEM_PROMPT_VALIDATE, SYSTEM_PROMPT_FIX


def _latex_to_sympy(latex_str: str) -> str:
    """将 LaTeX 度规分量转换为 SymPy 格式字符串。"""

    import sympy
    from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

    s = latex_str.strip()
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1]
    # First try: parse LaTeX directly with sympy's latex parser
    try:
        from sympy.parsing.latex import parse_latex
        expr = parse_latex(s)
        return str(expr)
    except Exception:
        pass
    # Second try: regex conversion then implicit-multiplication parse
    s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', s)
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
    """从题目数据中获取 SymPy 格式度规矩阵和变量列表。"""
    pd = problem_dict["physical_data"]

    if pd.get("metric_sympy"):
        return pd["metric_sympy"], pd["variables"]

    metric_name = problem_dict["metadata"]["tags"].get("metric", "")
    if metric_name in METRIC_LIBRARY:
        data = METRIC_LIBRARY[metric_name]
        return data["metric"], data["variables"]

    if pd.get("metric"):
        try:
            metric_latex = pd["metric"]
            metric_sympy = []
            for row in metric_latex:
                sympy_row = []
                for cell in row:
                    if cell in ["$0$", "$0$"]:
                        sympy_row.append("0")
                    else:
                        sympy_row.append(_latex_to_sympy(cell))
                metric_sympy.append(sympy_row)

            vars_clean = [v.strip("$").strip() for v in pd["variables"]]
            pd["metric_sympy"] = metric_sympy
            return metric_sympy, vars_clean
        except ValueError as e:
            raise ValueError(f"LaTeX 度规转 SymPy 失败，且 '{metric_name}' 不在度规库中: {e}")

    raise ValueError(f"无法获取 SymPy 格式度规")


def _compute_fact_sheet_for_problem(problem_dict: dict) -> dict:
    """为题目计算 Fact Sheet，用于验证。"""
    try:
        metric_sympy, variables = _get_metric_sympy(problem_dict)
    except ValueError as e:
        return {"error": str(e)}

    vars_clean = [v.strip("$").strip() for v in variables]
    try:
        return compute_fact_sheet(metric_sympy, vars_clean)
    except Exception as e:
        return {"error": f"Fact Sheet 计算失败: {e}"}


def validate_problem(problem_dict: dict, fact_sheet: dict = None) -> dict:
    """验证一道题目的答案正确性。

    Args:
        problem_dict: 题目的 dict 表示
        fact_sheet: 可选，已计算的 Fact Sheet。如果传入则跳过计算。

    Returns dict with verified: bool, issues: list, fact_sheet: dict.
    """
    # Step 1: 获取 Fact Sheet
    if fact_sheet is None:
        fact_sheet = _compute_fact_sheet_for_problem(problem_dict)
    if "error" in fact_sheet:
        return {"verified": False, "issues": [fact_sheet["error"]], "fact_sheet": None}

    # Step 2: 如果 answer 是"无答案"，标记为不可解（validated=false）
    answer = problem_dict["origin"].get("answer", "")
    if answer and "无答案" in answer:
        return {"verified": False, "issues": ["题目 answer 为无答案，问题本身不可解"], "fact_sheet": fact_sheet}

    # Step 3: LLM 验证
    print(f"    验证中 (模型: {MODEL_VALIDATE})...")
    prompt = (
        f"以下是该度规的 Fact Sheet（绝对正确的几何属性数据）：\n"
        f"{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"以下是该题目的完整内容：\n"
        f"question: {problem_dict['origin'].get('question', '')}\n"
        f"answer: {answer}\n"
        f"solution: {problem_dict['origin'].get('solution', 'null')}\n"
        f"hint: {json.dumps(problem_dict['origin'].get('hint'), ensure_ascii=False)}\n\n"
        f"请验证该题目的可解性和自洽性。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_VALIDATE, model=MODEL_VALIDATE)

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
        verified_match = re.search(r'"verified"\s*:\s*(true|false)', text)
        issues_match = re.search(r'"issues"\s*:\s*\[(.*?)\]', text, re.DOTALL)
        issues = []
        if issues_match:
            raw = issues_match.group(1)
            issues = [s.strip().strip('"') for s in raw.split(",") if s.strip().strip('"')]
        if verified_match:
            result = {"verified": verified_match.group(1) == "true", "issues": issues}
        else:
            result = {"verified": False, "issues": [f"LLM 返回无法解析: {text[:100]}"]}

    result["fact_sheet"] = fact_sheet
    return result


def _parse_llm_json(text: str) -> dict:
    """解析 LLM 返回的 JSON，处理 markdown 代码块和转义。"""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        text = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            raise


def fix_problem(problem_dict: dict, fact_sheet: dict, issues: list) -> dict:
    """根据 issues 修正题目的 answer/solution/hint。

    Returns the fixed dict (metadata and physical_data.metric_sympy are preserved).
    """
    print(f"    修正中 (模型: {MODEL_FIX}, issues: {len(issues)} 条)...")
    prompt = (
        f"以下是该度规的 Fact Sheet（绝对正确的几何属性数据）：\n"
        f"{json.dumps(fact_sheet, ensure_ascii=False, indent=2)}\n\n"
        f"以下是当前题目的完整内容：\n"
        f"{json.dumps(problem_dict, ensure_ascii=False, indent=2)}\n\n"
        f"以下是验证者发现的具体问题：\n"
        f"{json.dumps(issues, ensure_ascii=False, indent=2)}\n\n"
        f"请根据 Fact Sheet 修正上述问题。只修正 answer、solution、hint，不改度规和设问方向。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_FIX, model=MODEL_FIX)

    data = _parse_llm_json(response)

    # Preserve fields that must not be changed
    data["metadata"]["id"] = problem_dict["metadata"]["id"]
    data["metadata"]["source"] = problem_dict["metadata"]["source"]
    data["metadata"]["validated"] = problem_dict["metadata"]["validated"]
    data["physical_data"]["metric_sympy"] = problem_dict["physical_data"].get("metric_sympy")

    # Ensure tags is a dict
    if isinstance(data["metadata"]["tags"], list):
        from core.system_prompts import TAG_KEYS
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    return data


def validate_and_fix_loop(problem_dict: dict, max_attempts: int = 2) -> dict:
    """验证题目，如果失败则修正并重新验证，循环直到通过或达到最大次数。

    Returns the final dict (may be modified from fix attempts).
    """
    # Compute Fact Sheet once (reuse in all iterations)
    fact_sheet = _compute_fact_sheet_for_problem(problem_dict)
    if "error" in fact_sheet:
        problem_dict["metadata"]["validated"] = False
        return problem_dict

    for attempt in range(max_attempts + 1):
        result = validate_problem(problem_dict, fact_sheet=fact_sheet)

        if result["verified"]:
            problem_dict["metadata"]["validated"] = True
            if "EinsteinPy" not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append("EinsteinPy")
            validate_model_tag = f"validate:{MODEL_VALIDATE}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            print(f"  验证通过 (attempt {attempt})")
            return problem_dict

        issues = result.get("issues", [])
        print(f"  验证失败 (attempt {attempt}): {issues[:3]}...")

        # If no specific issues, can't fix — stop
        if not issues:
            problem_dict["metadata"]["validated"] = False
            validate_model_tag = f"validate:{MODEL_VALIDATE}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            return problem_dict

        # If we've exhausted attempts, stop
        if attempt >= max_attempts:
            problem_dict["metadata"]["validated"] = False
            if "EinsteinPy" not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append("EinsteinPy")
            validate_model_tag = f"validate:{MODEL_VALIDATE}"
            if validate_model_tag not in problem_dict["metadata"]["tools_used"]:
                problem_dict["metadata"]["tools_used"].append(validate_model_tag)
            print(f"  达到最大修正次数 {max_attempts}，停止")
            return problem_dict

        # Fix the problem
        print(f"  修正中 (attempt {attempt + 1})...")
        try:
            fixed = fix_problem(problem_dict, fact_sheet, issues)
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


def validate_json_file(path: str) -> dict:
    """读取 JSON 文件，验证+修正，更新 validated 和 tools_used，保存回文件。"""
    from pathlib import Path

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    result = validate_and_fix_loop(raw)

    Path(path).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result