"""
文件转换器模块

将 PDF 和 Word 文件转换为图片，以便 AI 模型处理
"""

import os
import tempfile
from pathlib import Path
from typing import List, Tuple

from core.common.config import PDF_DPI


def convert_pdf_to_images(path: str) -> List[Tuple[bytes, str]]:
    try:
        import fitz
        doc = fitz.open(path)
        images = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            mat = fitz.Matrix(PDF_DPI, PDF_DPI)
            pix = page.get_pixmap(matrix=mat)
            img_bytes = pix.tobytes("png")
            images.append((img_bytes, f"{Path(path).stem}_p{page_num + 1}"))
        doc.close()
        return images
    except ImportError:
        raise ImportError("读取 PDF 需要安装 PyMuPDF: pip install PyMuPDF PyMuPDFb")
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF 文件不存在：{path}")
    except Exception as e:
        raise IOError(f"转换 PDF 文件失败：{path}, 错误：{e}")


def convert_word_to_images(path: str) -> List[Tuple[bytes, str]]:
    try:
        import comtypes.client
        word = comtypes.client.CreateObject("Word.Application")
        word.Visible = False
        doc_path = os.path.abspath(path)
        doc = word.Documents.Open(doc_path)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            doc.SaveAs2(tmp_path, FileFormat=17)
            doc.Close()
            word.Quit()
            return convert_pdf_to_images(tmp_path)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    except (ImportError, OSError, AttributeError):
        try:
            from docx2pdf import convert
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp_path = tmp.name
            try:
                convert(path, tmp_path)
                return convert_pdf_to_images(tmp_path)
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
        except ImportError:
            raise ImportError("读取 Word 文件需要安装依赖：pip install docx2pdf PyMuPDF PyMuPDFb")
        except Exception as e:
            raise IOError(f"转换 Word 文件失败：{path}, 错误：{e}")
    except Exception as e:
        raise IOError(f"转换 Word 文件失败：{path}, 错误：{e}")


IMAGE_MEDIA_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


def is_supported_image(suffix: str) -> bool:
    return suffix.lower() in IMAGE_MEDIA_MAP


def get_media_type(suffix: str) -> str:
    return IMAGE_MEDIA_MAP.get(suffix.lower(), "image/jpeg")