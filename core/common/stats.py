"""Pipeline run statistics: per-phase counts, diversity metrics, timing, and LLM call tracking."""

import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class PhaseStats:
    """单个 Phase 的运行统计。

    Attributes:
        name: Phase 名称（如 "cognitive_fanout", "metric_substitute" 等）
        input_count: 进入该 phase 的题目/种子数
        output_count: 该 phase 产出的题目数
        skipped_count: 被跳过的题目数（如 form_change 对 conceptual 题）
        failed_count: 生成失败的题目数（LLM 报错、JSON 解析失败等）
        wall_seconds: 该 phase 实际耗时（秒）
        llm_calls: 该 phase 的 LLM API 调用次数
        errors: 具体错误信息列表（每条≤200字符）
    """
    name: str
    input_count: int = 0
    output_count: int = 0
    skipped_count: int = 0
    failed_count: int = 0
    wall_seconds: float = 0.0
    llm_calls: int = 0
    errors: List[str] = field(default_factory=list)


@dataclass
class PipelineResult:
    """单个种子的完整 Pipeline 运行结果。

    Attributes:
        seed_id: 种子题 ID
        phases: 各 Phase 的统计列表
        total_problems: 最终产出题目总数（去重后）
        validated_count: 验证通过的题目数
        degraded_count: 验证失败标记 degraded 的题目数
        diversity: 多样性覆盖 {cognitive_forms: set, physics_envs: set, soft_variants: set}
        total_llm_calls: 该种子所有 phase 的 LLM 调用总数
        total_wall_seconds: 该种子端到端耗时
        output_labels: 各题目文件名标签列表
    """
    seed_id: str
    phases: List[PhaseStats] = field(default_factory=list)
    total_problems: int = 0
    validated_count: int = 0
    degraded_count: int = 0
    diversity: Dict = field(default_factory=dict)
    total_llm_calls: int = 0
    total_wall_seconds: float = 0.0
    output_labels: List[str] = field(default_factory=list)

    def compute_totals(self):
        """从 phases 列表计算汇总值。"""
        self.total_llm_calls = sum(p.llm_calls for p in self.phases)
        self.total_wall_seconds = sum(p.wall_seconds for p in self.phases)

    def funnel_table(self) -> str:
        """生成该种子的 Funnel 表（markdown 格式）。"""
        lines = [
            "| stage | input | output | skipped | failed |",
            "|---|---|---|---|---|",
        ]
        for p in self.phases:
            lines.append(f"| {p.name} | {p.input_count} | {p.output_count} | {p.skipped_count} | {p.failed_count} |")
        lines.append(f"| **final** | — | **{self.total_problems}** | — | — |")
        return "\n".join(lines)


@dataclass
class BatchResult:
    """批量运行（多个种子）的汇总结果。

    Attributes:
        seeds: 每个种子的 PipelineResult
        total_llm_calls: 全局 LLM 调用总数
        total_wall_seconds: 全局端到端耗时
        diversity: 全局多样性覆盖 {cognitive_forms: set, physics_envs: set, soft_variants: set}
        failed_sources: 失败的种子列表 [{source_id, reason}]
        source_count: 种子总数
        total_problems: 全局产出题目总数
    """
    seeds: List[PipelineResult] = field(default_factory=list)
    total_llm_calls: int = 0
    total_wall_seconds: float = 0.0
    diversity: Dict = field(default_factory=dict)
    failed_sources: List[Dict] = field(default_factory=list)
    source_count: int = 0
    total_problems: int = 0

    def compute_totals(self):
        """从 seeds 列表计算全局汇总值。"""
        self.total_llm_calls = sum(s.total_llm_calls for s in self.seeds)
        self.total_wall_seconds = sum(s.total_wall_seconds for s in self.seeds)
        self.total_problems = sum(s.total_problems for s in self.seeds)
        self.source_count = len(self.seeds) + len(self.failed_sources)

        # 全局 diversity 合并
        all_cf = set()
        all_pe = set()
        all_sv = set()
        for s in self.seeds:
            if "cognitive_forms" in s.diversity:
                all_cf.update(s.diversity["cognitive_forms"])
            if "physics_envs" in s.diversity:
                all_pe.update(s.diversity["physics_envs"])
            if "soft_variants" in s.diversity:
                all_sv.update(s.diversity["soft_variants"])
        self.diversity = {
            "cognitive_forms": all_cf,
            "physics_envs": all_pe,
            "soft_variants": all_sv,
        }


class Timer:
    """简单的计时器，用于 Phase 耗时测量。"""

    def __init__(self):
        self._start = None
        self._elapsed = 0.0

    def start(self):
        self._start = time.time()

    def stop(self) -> float:
        if self._start is not None:
            self._elapsed = time.time() - self._start
            self._start = None
        return self._elapsed

    @property
    def elapsed(self) -> float:
        if self._start is not None:
            return time.time() - self._start
        return self._elapsed


def compute_diversity_from_problems(problems) -> dict:
    """从 Problem 列表计算多样性覆盖。

    Returns: {cognitive_forms: set, physics_envs: set, soft_variants: set}
    """
    from schema import TYPE_TO_COGNITIVE

    cognitive_forms = set()
    physics_envs = set()
    soft_variants = set()

    for p in problems:
        cf = p.metadata.cognitive_form or TYPE_TO_COGNITIVE.get(p.metadata.type, "")
        pe = p.metadata.physics_env or p.metadata.tags.get("metric", "")
        sv = p.metadata.soft_variant or ""
        if cf:
            cognitive_forms.add(cf)
        if pe:
            physics_envs.add(pe)
        if sv:
            soft_variants.add(sv)

    return {
        "cognitive_forms": cognitive_forms,
        "physics_envs": physics_envs,
        "soft_variants": soft_variants,
    }