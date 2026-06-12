"""Seed stage: extract problems from book → abstract to structured JSON"""
from .extractor import run_split_pipeline
from .formatter import abstract_question, abstract_question_to_json
from .metric_generator import generate_metric