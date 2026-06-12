"""hw_pipeline core modules, organized by stage"""

# Common (shared across all stages)
from .common.constants import TAG_KEYS
from .common.config import (
    API_URL, API_KEY, DEFAULT_MODEL, check_api_key,
    MODEL_ABSTRACT, MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC,
    MODEL_VALIDATE, MODEL_JUDGE, MODEL_RED_TEAM, MODEL_FIX, MODEL_EXTRACT,
)
from .common.api_client import ask_ai, get_llm_stats
from .common.cleaner import clean_problem, clean_json_file
from .common.metric_library import METRIC_LIBRARY
from .common.sympy_engine import compute_fact_sheet, compute_fact_sheet_heavy
from .common.stats import PhaseStats, PipelineResult, BatchResult
from .common.report import generate_report

# Seed (Stage 0)
from .seed.extractor import run_split_pipeline
from .seed.formatter import abstract_question, abstract_question_to_json

# Scale
from .scale.pipeline import generate_from_seed

# Verify
from .verify.validator import (
    full_validate, is_verification_ok, validate_and_fix_loop, validate_json_file,
    _compute_fact_sheet_for_problem,
)