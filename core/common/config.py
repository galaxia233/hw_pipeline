"""
配置文件

所有配置通过 .env 文件或环境变量设置，参考 .env.example。
"""

import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_URL = "https://dashscope.aliyuncs.com/apps/anthropic/v1/messages"
API_KEY: str = os.environ.get("DASHSCOPE_API_KEY") or ""

DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL") or "glm-5.1"

# 各阶段使用的模型
MODEL_ABSTRACT = os.environ.get("MODEL_ABSTRACT") or DEFAULT_MODEL
MODEL_COMPOSE = os.environ.get("MODEL_COMPOSE") or DEFAULT_MODEL
MODEL_SUBSTITUTE = os.environ.get("MODEL_SUBSTITUTE") or DEFAULT_MODEL
MODEL_PICK_METRIC = os.environ.get("MODEL_PICK_METRIC") or DEFAULT_MODEL
MODEL_VALIDATE = os.environ.get("MODEL_VALIDATE") or DEFAULT_MODEL
MODEL_JUDGE = os.environ.get("MODEL_JUDGE") or MODEL_VALIDATE
MODEL_RED_TEAM = os.environ.get("MODEL_RED_TEAM") or MODEL_VALIDATE
MODEL_FIX = os.environ.get("MODEL_FIX") or DEFAULT_MODEL
MODEL_EXTRACT = os.environ.get("MODEL_EXTRACT") or "qwen3.6-flash"

DEFAULT_MAX_RETRIES = int(os.environ.get("DEFAULT_MAX_RETRIES") or "3")
DEFAULT_TIMEOUT = int(os.environ.get("DEFAULT_TIMEOUT") or "600")
DEFAULT_MAX_TOKENS = int(os.environ.get("DEFAULT_MAX_TOKENS") or "16384")
PDF_DPI = int(os.environ.get("PDF_DPI") or "1")


def check_api_key():
    if not API_KEY:
        raise ValueError("未设置环境变量 DASHSCOPE_API_KEY，请设置后再运行")
    return API_KEY