"""度规生成模块：让 LLM 根据 tags 生成新度规"""

import json
import re

from core.api_client import ask_ai
from core.config import MODEL_COMPOSE
from core.system_prompts import SYSTEM_PROMPT_METRIC


def generate_metric(tags: dict) -> dict:
    """根据 tags 让 LLM 生成一个新度规。

    Args:
        tags: 结构化 tags dict，如 {"metric": "Schwarzschild", "scenario": "black hole", ...}

    Returns:
        dict 包含 dimension, variables, metric (SymPy 表达式), description
    """
    tags_desc = ", ".join(f"{k}: {v}" for k, v in tags.items())
    prompt = (
        f"请根据以下物理场景和坐标系统信息，生成一个合理的度规张量：\n"
        f"{tags_desc}\n\n"
        f"生成的度规应与上述 tags 中的场景和坐标系统一致，"
        f"但不必与原度规相同——可以是同一场景下的不同度规变体。"
    )
    response = ask_ai(prompt, system=SYSTEM_PROMPT_METRIC, model=MODEL_COMPOSE)

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

    return data