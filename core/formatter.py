"""题目格式化模块：将自然语言 GR 题目抽象化为结构化 JSON"""

import json
import re
from dataclasses import asdict

from core.cleaner import clean_problem
from core.api_client import ask_ai
from core.config import MODEL_ABSTRACT
from schema import Problem
from core.system_prompts import SYSTEM_PROMPT_ABSTRACT


def abstract_question(files, source="generated") -> Problem:
    """Convert a natural language question file into a Problem object via AI."""
    prompt = "请将附件中的题目抽象化为 schema JSON 格式"
    response = ask_ai(prompt, files=files, system=SYSTEM_PROMPT_ABSTRACT, model=MODEL_ABSTRACT)

    # Strip markdown code block if present
    text = response.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Fix invalid JSON escapes in LLM output: LaTeX uses bare \theta, \Gamma etc.
    # which are invalid JSON escapes. Replace them with double backslashes.
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        text = re.sub(r'\\(?![/"\\bfnrtu])', r'\\\\', text)
        data = json.loads(text)

    # Ensure tags is a dict (LLM may output a list)
    if isinstance(data["metadata"]["tags"], list):
        from core.system_prompts import TAG_KEYS
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    # Override metadata fields — not from LLM
    data["metadata"]["source"] = source
    data["metadata"]["tools_used"] = []
    data["metadata"]["validated"] = False
    if "id" not in data["metadata"]:
        data["metadata"]["id"] = source

    return Problem(
        metadata=_build_metadata(data["metadata"]),
        physical_data=_build_physical_data(data["physical_data"]),
        origin=_build_origin(data["origin"]),
    )


def abstract_question_to_json(files, source="generated") -> str:
    """Convert a natural language question file into JSON string via AI."""
    problem = abstract_question(files=files, source=source)
    return json.dumps(clean_problem(problem), ensure_ascii=False, indent=2)


def _build_metadata(data):
    from schema import Metadata
    return Metadata(**{k: v for k, v in data.items() if k in Metadata.__dataclass_fields__})


def _build_physical_data(data):
    from schema import PhysicalData
    return PhysicalData(**{k: v for k, v in data.items() if k in PhysicalData.__dataclass_fields__})


def _build_origin(data):
    from schema import Origin
    return Origin(**{k: v for k, v in data.items() if k in Origin.__dataclass_fields__})