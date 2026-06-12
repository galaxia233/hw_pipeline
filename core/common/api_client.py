"""
API 客户端模块

提供调用 AI API 的函数
"""

import base64
import time
from pathlib import Path
from typing import Union, List, Tuple

import requests

from core.common.config import (
    API_URL,
    API_KEY,
    DEFAULT_MODEL,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    check_api_key,
)
from core.common.file_converter import (
    convert_pdf_to_images,
    convert_word_to_images,
    is_supported_image,
    get_media_type,
)

# ==================== LLM 调用计量 ====================

_llm_call_count = 0
_llm_total_output_chars = 0


def get_llm_stats() -> dict:
    """返回 LLM 调用统计：调用次数和粗估 output token。

    Output token 估算规则：1 token ≈ 4 字符（英文）或 ≈ 2 字符（中文混合）。
    用 //3 做保守估计（混合内容）。
    """
    return {
        "calls": _llm_call_count,
        "estimated_output_tokens": _llm_total_output_chars // 3,
    }


def reset_llm_stats():
    """重置 LLM 调用计数器（每次 pipeline run 开始时调用）。"""
    global _llm_call_count, _llm_total_output_chars
    _llm_call_count = 0
    _llm_total_output_chars = 0


def read_md_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="gbk") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"md 文件不存在：{path}")
    except IOError as e:
        raise IOError(f"读取 md 文件失败：{path}, 错误：{e}")


def ask_ai(
    prompt: str,
    files: Union[str, List[str], None] = None,
    system: str = None,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    max_retries: int = DEFAULT_MAX_RETRIES,
    temperature: float = None,
) -> str:
    global _llm_call_count, _llm_total_output_chars
    _llm_call_count += 1

    check_api_key()

    content = []

    if files is None:
        file_paths = []
    elif isinstance(files, str):
        file_paths = [files]
    else:
        file_paths = list(files)

    all_files: List[Tuple[bytes, str, str, bool]] = []
    md_contents: List[str] = []
    file_counter = 0

    for path in file_paths:
        suffix = Path(path).suffix.lower()

        if is_supported_image(suffix):
            file_counter += 1
            media_type = get_media_type(suffix)
            with open(path, "rb") as f:
                image_data = f.read()
            all_files.append((image_data, media_type, Path(path).name, True))

        elif suffix == ".pdf":
            file_counter += 1
            pdf_images = convert_pdf_to_images(path)
            for i, (img_bytes, name) in enumerate(pdf_images):
                all_files.append((img_bytes, "image/png", f"{Path(path).stem}.pdf", i == 0))

        elif suffix in [".docx", ".doc"]:
            file_counter += 1
            word_images = convert_word_to_images(path)
            for i, (img_bytes, name) in enumerate(word_images):
                all_files.append((img_bytes, "image/png", f"{Path(path).stem}.{suffix[1:]}", i == 0))

        elif suffix == ".md":
            file_counter += 1
            md_content = read_md_file(path)
            md_contents.append(f"[文件 {file_counter}: {Path(path).name}]\n\n{md_content}")

        else:
            raise ValueError(f"不支持的文件类型：{suffix}, 文件：{path}")

    for idx, (img_bytes, media_type, name, add_marker) in enumerate(all_files, start=1):
        image_data = base64.b64encode(img_bytes).decode("utf-8")
        content.append({
            "type": "image",
            "source": {"type": "base64", "media_type": media_type, "data": image_data}
        })
        if add_marker:
            content.append({
                "type": "text",
                "text": f"[文件 {idx}: {name}]"
            })

    for md_content in md_contents:
        content.append({"type": "text", "text": md_content})

    content.append({"type": "text", "text": prompt})

    body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": content}],
    }
    if system:
        body["system"] = system
    if temperature is not None:
        body["temperature"] = temperature

    last_error = None
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                API_URL,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {API_KEY}",
                    "anthropic-version": "2023-06-01",
                },
                json=body,
                timeout=DEFAULT_TIMEOUT,
            )
            response.raise_for_status()
            data = response.json()
            text_block = next(block for block in data["content"] if block["type"] == "text")
            result_text = text_block["text"]
            _llm_total_output_chars += len(result_text)
            return result_text

        except requests.exceptions.Timeout as e:
            last_error = e
            print(f"[attempt {attempt+1}] 超时，重试中...")

        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                # 429 Too Many Requests — 等待后重试
                last_error = e
                wait = 2 ** (attempt + 2)  # 4s, 8s, 16s...
                print(f"[attempt {attempt+1}] 429 限流，等待 {wait}s 后重试...")
                time.sleep(wait)
                continue
            if response.status_code < 500:
                raise
            last_error = e
            print(f"[attempt {attempt+1}] 服务器错误 {response.status_code}，重试中...")

        except Exception as e:
            last_error = e
            print(f"[attempt {attempt+1}] 未知错误：{e}，重试中...")

        if attempt < max_retries:
            wait = 2 ** attempt
            print(f"等待 {wait}s 后重试...")
            time.sleep(wait)

    raise RuntimeError(f"请求失败，已重试 {max_retries} 次，最后错误：{last_error}")