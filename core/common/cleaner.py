"""Clean formatting artifacts from Problem JSON dicts.

核心修复：
1. LaTeX 命令拼接错误：LLM 输出的 \\thetad → \\theta d, \\piT → \\pi T 等
2. 不去掉 $...$ 数学段内 LaTeX 命令后必需的分隔空格
3. 只去掉不影响 LaTeX 渲染的"格式空格"
"""

import re
from dataclasses import asdict
from schema import Problem


# Common LaTeX commands that frequently get concatenated with following letters.
# After any of these, if a letter immediately follows (no space/brace/sub/sup),
# insert a space to prevent invalid macro parsing.
_LATEX_COMMAND_PATTERN = (
    'alpha|beta|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta'
    '|iota|kappa|lambda|mu|nu|xi|omicron|pi|varpi|rho|varrho|sigma|varsigma'
    '|tau|upsilon|phi|varphi|chi|psi|omega'
    '|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega'
    '|sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|coth|arcsin|arccos|arctan'
    '|log|ln|exp|det|dim|lim|mod|gcd|max|min|sup|inf'
    '|vec|hat|tilde|dot|ddot|bar|partial|nabla|infty'
    '|hbar|ell|wp|Re|Im|Pr'
    '|quad|qquad|text|mathrm|mathbf|mathcal|mathbb|mathfrak|mathit'
)


def _fix_command_concatenation(s: str) -> str:
    """Fix LaTeX command concatenation: \\thetad → \\theta d, \\piT → \\pi T.

    In LaTeX, a command name is \\[a-zA-Z]+ and ends at the first non-letter.
    So \\thetad would be parsed as one (invalid) command. This function detects
    known commands followed directly by a letter and inserts a space.

    Only triggers when a known command is followed by a letter (not {, _, ^, \\, space),
    so \\frac{...}, \\sin^2, \\theta_\\mu etc. are untouched.
    """
    return re.sub(
        r'\\(' + _LATEX_COMMAND_PATTERN + r')(?=[a-zA-Z])',
        r'\\\1 ',
        s,
    )


def _remove_newlines(v):
    """Recursively remove literal \\n from all strings."""
    if isinstance(v, str):
        return v.replace("\n", "")
    if isinstance(v, list):
        return [_remove_newlines(item) for item in v]
    if isinstance(v, dict):
        return {k: _remove_newlines(val) for k, val in v.items()}
    return v


def _clean_math_segment(s: str) -> str:
    """Clean a math segment ($...$ or $$...$$), preserving LaTeX-critical spaces.

    处理步骤：
    1. 修复 LaTeX 命令拼接（\\thetad → \\theta d）
    2. 连续2+空格 → 1空格
    3. {} 内侧开头/结尾空格
    4. ^ 和 _ 前后空格 → 紧凑
    5. \\left / \\right 后空格 → 紧凑
    """
    # Step 0: 修复 LaTeX 命令拼接（最优先，防止后续步骤干扰）
    s = _fix_command_concatenation(s)

    # Step 1: 连续2+空格 → 1空格
    s = re.sub(r' {2,}', ' ', s)

    # Step 2: {} 内侧开头/结尾空格
    s = re.sub(r'\{ +', '{', s)
    s = re.sub(r' +\}', '}', s)

    # Step 3: ^ 和 _ 前后空格 → 紧凑
    s = re.sub(r' *\^ *', '^', s)
    s = re.sub(r' *_ *', '_', s)

    # Step 4: \left / \right 后空格 → 紧凑（单反斜杠，LLM 输出中的 LaTeX）
    s = re.sub(r'\\left\s+', r'\\left', s)
    s = re.sub(r'\s+\\right', r'\\right', s)

    return s


def _clean_string(s: str) -> str:
    """Clean spaces in math segments, preserving LaTeX-critical spaces."""
    if not isinstance(s, str):
        return s

    def _clean_math(match):
        return _clean_math_segment(match.group(0))

    s = re.sub(r'\$\$.*?\$\$', _clean_math, s, flags=re.DOTALL)
    s = re.sub(r'\$[^$].*?\$', _clean_math, s)
    return s


def _clean_value(v):
    """Recursively clean strings in a nested dict/list structure."""
    if isinstance(v, str):
        return _clean_string(v)
    if isinstance(v, list):
        return [_clean_value(item) for item in v]
    if isinstance(v, dict):
        return {k: _clean_value(val) for k, val in v.items()}
    return v


def clean_problem(problem: Problem) -> dict:
    """Clean a Problem object and return its dict representation."""
    d = asdict(problem)
    d = _remove_newlines(d)
    d["origin"] = _clean_value(d["origin"])
    pd = d["physical_data"]
    sympy_backup = pd.get("metric_sympy")
    pd_cleaned = _clean_value(pd)
    if sympy_backup is not None:
        pd_cleaned["metric_sympy"] = sympy_backup
    d["physical_data"] = pd_cleaned
    return d


def clean_json_file(path: str) -> dict:
    """Read a JSON file, clean its contents, and return the cleaned dict."""
    import json
    from pathlib import Path

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    raw = _remove_newlines(raw)
    raw["origin"] = _clean_value(raw["origin"])
    pd = raw["physical_data"]
    sympy_backup = pd.get("metric_sympy")
    pd_cleaned = _clean_value(pd)
    if sympy_backup is not None:
        pd_cleaned["metric_sympy"] = sympy_backup
    raw["physical_data"] = pd_cleaned
    return raw