"""运行报告生成器：从 PipelineResult / BatchResult 填充 run_report_template.md。"""

from core.common.stats import PipelineResult, BatchResult


def generate_report(result: PipelineResult | BatchResult,
                    mode: str = "B",
                    group_name: str = "") -> str:
    """从运行结果生成 run_report markdown。

    Args:
        result: 单种子 PipelineResult 或批量 BatchResult
        mode: 工作模式描述（"B" / "textbook" / "problem_set" 等）
        group_name: 组名（填入标题）

    Returns: 完整的 markdown 报告文本
    """
    if isinstance(result, PipelineResult):
        return _report_from_single(result, mode, group_name)
    elif isinstance(result, BatchResult):
        return _report_from_batch(result, mode, group_name)
    else:
        raise TypeError(f"不支持的结果类型: {type(result)}")


def _report_from_single(r: PipelineResult, mode: str, group_name: str) -> str:
    """从单个 PipelineResult 生成报告。"""
    seed_count = 1
    total = r.total_problems
    validated = r.validated_count
    degraded = r.degraded_count
    failed = total - validated - degraded

    diversity = r.diversity
    n_cf = len(diversity.get("cognitive_forms", set()))
    n_pe = len(diversity.get("physics_envs", set()))
    n_sv = len(diversity.get("soft_variants", set()))

    cf_list = sorted(diversity.get("cognitive_forms", set()))
    pe_list = sorted(diversity.get("physics_envs", set()))
    sv_list = sorted(diversity.get("soft_variants", set()))

    llm_calls = r.total_llm_calls
    est_tokens = llm_calls * 2000  # 粗估：每次调用约 2000 output tokens
    wall_hours = r.total_wall_seconds / 3600

    funnel = _build_funnel(r.phases, total, validated, degraded)

    return f"""# Run Report — {group_name or r.seed_id}

## 工作模式
- mode: {mode}
- sources count: 1 种子 → {total} 道生成题

## Funnel

{funnel}

## Diversity coverage
- cognitive_form: {n_cf} distinct ({', '.join(cf_list)})
- physics_env: {n_pe} distinct ({', '.join(pe_list)})
- soft_variant: {n_sv} distinct ({', '.join(sv_list)})

## Failed sources (skip / partial)

| source_id | type | status | reason |
|---|---|---|---|
| _(none)_ | — | — | — |

## What worked / didn't
- 工作得很好的事: _(待填写)_
- 没工作好但尝试过的事: _(待填写)_
- 完全没尝试的事(并解释原因): _(待填写)_

## Token / wall-clock estimate
- 总 LLM 调用: ~{llm_calls} 次
- 估计 output token: ~{est_tokens}
- 端到端 wall-clock: ~{wall_hours:.1f} 小时"""


def _report_from_batch(r: BatchResult, mode: str, group_name: str) -> str:
    """从批量 BatchResult 生成报告。"""
    source_count = r.source_count
    total = r.total_problems
    validated = sum(s.validated_count for s in r.seeds)
    degraded = sum(s.degraded_count for s in r.seeds)
    failed = total - validated - degraded

    diversity = r.diversity
    n_cf = len(diversity.get("cognitive_forms", set()))
    n_pe = len(diversity.get("physics_envs", set()))
    n_sv = len(diversity.get("soft_variants", set()))

    cf_list = sorted(diversity.get("cognitive_forms", set()))
    pe_list = sorted(diversity.get("physics_envs", set()))
    sv_list = sorted(diversity.get("soft_variants", set()))

    llm_calls = r.total_llm_calls
    est_tokens = llm_calls * 2000
    wall_hours = r.total_wall_seconds / 3600

    # 合并所有 phases 的 funnel
    all_phases = []
    for s in r.seeds:
        all_phases.extend(s.phases)
    funnel = _build_funnel(all_phases, total, validated, degraded)

    # 失败种子列表
    failed_rows = ""
    if r.failed_sources:
        rows = []
        for fs in r.failed_sources:
            rows.append(f"| {fs['source_id']} | {fs.get('type', '')} | {fs.get('status', 'failed')} | {fs.get('reason', '')} |")
        failed_rows = "\n".join(rows)
    else:
        failed_rows = "| _(none)_ | — | — | — |"

    return f"""# Run Report — {group_name}

## 工作模式
- mode: {mode}
- sources count: {source_count} 种子 → {total} 道生成题

## Funnel

{funnel}

## Diversity coverage
- cognitive_form: {n_cf} distinct ({', '.join(cf_list)})
- physics_env: {n_pe} distinct ({', '.join(pe_list)})
- soft_variant: {n_sv} distinct ({', '.join(sv_list)})

## Failed sources (skip / partial)

| source_id | type | status | reason |
|---|---|---|---|
{failed_rows}

## What worked / didn't
- 工作得很好的事: _(待填写)_
- 没工作好但尝试过的事: _(待填写)_
- 完全没尝试的事(并解释原因): _(待填写)_

## Token / wall-clock estimate
- 总 LLM 调用: ~{llm_calls} 次
- 估计 output token: ~{est_tokens}
- 端到端 wall-clock: ~{wall_hours:.1f} 小时"""


def _build_funnel(phases: list, total: int, validated: int, degraded: int) -> str:
    """从 PhaseStats 列表构建 Funnel 表。

    按 phase 汇总 input/output/skipped/failed，并在末尾加 sources ingested 行。
    """
    # 汇总同名 phase（批量模式下多个种子有同名 phase）
    phase_agg = {}
    for p in phases:
        if p.name not in phase_agg:
            phase_agg[p.name] = {"input": 0, "output": 0, "skipped": 0, "failed": 0}
        phase_agg[p.name]["input"] += p.input_count
        phase_agg[p.name]["output"] += p.output_count
        phase_agg[p.name]["skipped"] += p.skipped_count
        phase_agg[p.name]["failed"] += p.failed_count

    lines = [
        "| stage | total | kept | skipped | failed |",
        "|---|---|---|---|---|",
    ]

    # sources ingested（第一个 phase 的 input_count）
    first_input = next((v["input"] for v in phase_agg.values()), 0)
    lines.append(f"| sources ingested | {first_input} | {first_input} | 0 | 0 |")

    # 各 phase
    for name, agg in phase_agg.items():
        lines.append(
            f"| {name} | {agg['input']} | {agg['output']} | {agg['skipped']} | {agg['failed']} |"
        )

    # final dataset
    failed_final = total - validated - degraded
    lines.append(f"| **final dataset** | **{total}** | **{validated}** | **{degraded}** | **{failed_final}** |")

    return "\n".join(lines)