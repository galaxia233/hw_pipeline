"""Clean formatting artifacts from Problem JSON dicts."""

import re
from dataclasses import asdict
from schema import Problem


def _remove_newlines(v):
    """Recursively remove literal \n from all strings (including metadata)."""
    if isinstance(v, str):
        return v.replace("\n", "")
    if isinstance(v, list):
        return [_remove_newlines(item) for item in v]
    if isinstance(v, dict):
        return {k: _remove_newlines(val) for k, val in v.items()}
    return v


def _clean_string(s: str) -> str:
    """Remove spaces only inside $$...$$ and $...$ LaTeX segments; keep spaces elsewhere. \n is handled separately."""
    if not isinstance(s, str):
        return s
    # Remove spaces only inside math segments
    def _strip_spaces_in_math(match):
        return match.group(0).replace(" ", "")
    s = re.sub(r'\$\$.*?\$\$', _strip_spaces_in_math, s, flags=re.DOTALL)
    s = re.sub(r'\$[^$].*?\$', _strip_spaces_in_math, s)
    return s


def _clean_value(v):
    """Recursively clean strings in a nested dict/list structure."""
    if isinstance(v, str):
        return _clean_string(v)
    if isinstance(v, list):
        return [_clean_value(item) for item in v]
    if isinstance(v, dict):
        return {k: _clean_value(val) for k, val in v.items()}
    return v  # int, float, None, bool — leave unchanged


def clean_problem(problem: Problem) -> dict:
    """Clean a Problem object and return its dict representation.
    Removes \n everywhere (including metadata).
    Removes spaces only inside $...$ math segments (in origin and physical_data, except metric_sympy).
    """
    d = asdict(problem)
    # Remove \n everywhere first
    d = _remove_newlines(d)
    # Then remove spaces in math segments (origin + physical_data, but preserve metric_sympy)
    d["origin"] = _clean_value(d["origin"])
    pd = d["physical_data"]
    sympy_backup = pd.get("metric_sympy")
    pd_cleaned = _clean_value(pd)
    if sympy_backup is not None:
        pd_cleaned["metric_sympy"] = sympy_backup
    d["physical_data"] = pd_cleaned
    return d


def clean_json_file(path: str) -> dict:
    """Read a JSON file, clean its contents, and return the cleaned dict.
    Removes \n everywhere (including metadata).
    Removes spaces only inside $...$ math segments (origin + physical_data, except metric_sympy).
    """
    import json
    from pathlib import Path

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    # Remove \n everywhere first
    raw = _remove_newlines(raw)
    # Then remove spaces in math segments
    raw["origin"] = _clean_value(raw["origin"])
    pd = raw["physical_data"]
    sympy_backup = pd.get("metric_sympy")
    pd_cleaned = _clean_value(pd)
    if sympy_backup is not None:
        pd_cleaned["metric_sympy"] = sympy_backup
    raw["physical_data"] = pd_cleaned
    return raw