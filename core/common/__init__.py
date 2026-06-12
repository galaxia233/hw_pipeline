"""Common utilities shared across all stages"""
from .constants import TAG_KEYS
from .config import API_URL, API_KEY, DEFAULT_MODEL, check_api_key
from .config import MODEL_ABSTRACT, MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC, MODEL_VALIDATE, MODEL_JUDGE, MODEL_RED_TEAM, MODEL_FIX, MODEL_EXTRACT
from .api_client import ask_ai, get_llm_stats, reset_llm_stats
from .cleaner import clean_problem, clean_json_file, _clean_value, _remove_newlines
from .metric_library import METRIC_LIBRARY
from .sympy_engine import compute_fact_sheet
from .file_converter import convert_pdf_to_images, convert_word_to_images, is_supported_image, get_media_type
from .stats import PhaseStats, PipelineResult, BatchResult, Timer, compute_diversity_from_problems
from .report import generate_report