"""题目格式化模块：将自然语言 GR 题目抽象化为结构化 JSON"""

import json
import re
from dataclasses import asdict

from core.common.cleaner import clean_problem
from core.common.api_client import ask_ai
from core.common.config import MODEL_ABSTRACT
from core.scale.pipeline import _parse_llm_json
from schema import Problem
from core.seed.prompts import SYSTEM_PROMPT_ABSTRACT


def _compute_quality_overall(metadata_data: dict) -> None:
    """自动计算 quality.overall = 各子分数的平均值"""
    quality = metadata_data.get("quality")
    if not quality or not isinstance(quality, dict):
        return
    sub_keys = ["physical_depth", "generalizability", "completeness", "realism"]
    scores = [quality[k] for k in sub_keys if k in quality and isinstance(quality[k], (int, float))]
    if scores:
        quality["overall"] = round(sum(scores) / len(scores), 2)


def _fill_seed_metadata(metadata_data: dict, source: str) -> dict:
    """为种子题填充程序化 metadata 字段。

    这些字段不由 LLM 生成，而是由程序根据 source 标签自动确定。
    """
    metadata_data["source"] = source
    metadata_data["source_id"] = source
    metadata_data["source_type"] = "problem_set"
    metadata_data["stage"] = "seed"
    metadata_data["lineage"] = [source]
    metadata_data["tools_used"] = []
    metadata_data["validated"] = False
    if "id" not in metadata_data:
        metadata_data["id"] = source
    return metadata_data


def abstract_question(files, source="generated") -> Problem:
    """Convert a natural language question file into a Problem object via AI."""
    prompt = "请将附件中的题目抽象化为 schema JSON 格式"
    response = ask_ai(prompt, files=files, system=SYSTEM_PROMPT_ABSTRACT, model=MODEL_ABSTRACT)

    data = _parse_llm_json(response)

    # Ensure tags is a dict (LLM may output a list), and clean "key:value" pollution
    if isinstance(data["metadata"]["tags"], list):
        from core.common.constants import TAG_KEYS
        tags_list = data["metadata"]["tags"]
        data["metadata"]["tags"] = {k: v for k, v in zip(TAG_KEYS[:len(tags_list)], tags_list)}

    tags = data["metadata"]["tags"]
    if isinstance(tags, dict):
        from core.common.constants import TAG_KEYS as _TK
        for key in list(tags.keys()):
            val = tags[key]
            if isinstance(val, str) and ":" in val:
                prefix = val.split(":")[0]
                if prefix in _TK:
                    tags[key] = val[len(prefix) + 1:].strip()

    # 填充程序化 metadata 字段（不依赖 LLM）
    _fill_seed_metadata(data["metadata"], source)

    # 自动计算 quality.overall（各项子分数的平均）
    _compute_quality_overall(data["metadata"])

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