"""Scale stage: generate variants from seed (compose, substitute, form_change, soft rewrite, validate, dedup)"""
from .pipeline import (
    fan_through, generate_from_seed,
    phase_cognitive_fanout, phase_metric_substitute,
    phase_form_change, phase_soft_rewrite,
    phase_batch_validate, phase_ngram_dedup,
)