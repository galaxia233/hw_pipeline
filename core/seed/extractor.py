"""
题目提取模块：从整书 md 文件中提取所有题目为独立 md 文件

改编自 int-llm/datagroup/split/pipeline.py，使用 hw_pipeline 自有的 api_client、config、system_prompts。

Pipeline:
  stage1_split — 按一级标题切分整书 md 为章节 md 文件
  chunk_large_sections — 大章节二次切分（超过 MAX_CHUNK_LINES 行）
  stage2_extract — 并行 LLM 提取题目，每个题目保存为独立 md 文件
  run_split_pipeline — 一次性完成上述三步
"""

import json
import re
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from core.common.api_client import ask_ai
from core.seed.prompts import SYSTEM_PROMPT_EXTRACT, SYSTEM_PROMPT_EXTRACT_SOLUTION
from core.common.config import MODEL_EXTRACT


# ==================== 切分工具 ====================


def split_by_heading(md_content: str) -> list[tuple[str, str, str]]:
    """按一级标题切分内容，追踪章节上下文（最近的含数字标题）

    每个 # 标题都切分为独立片段，但只有含数字的标题才更新章节上下文。
    不含数字的标题（如 Solution、Definition）继承前一个含数字标题的上下文。

    Returns: [(heading, content, chapter_context), ...]
        chapter_context: 最近含数字标题的数字前缀（如 "1.1"、"31"），无数字标题时为 ""
    """
    heading_pattern = r'^(#\s+.+)$'
    lines = md_content.split('\n')

    sections = []
    current_heading = None
    current_content = []
    current_context = ""  # 最近含数字标题的数字前缀

    for line in lines:
        match = re.match(heading_pattern, line)
        if match:
            if current_heading is not None and current_content:
                content_str = '\n'.join(current_content).strip()
                sections.append((current_heading, content_str, current_context))

            current_heading = match.group(1).strip()
            current_content = []

            # 如果标题含数字，且与当前上下文兼容，更新章节上下文
            heading_text = current_heading.lstrip('#').strip()
            prefix = extract_section_prefix(heading_text)
            if prefix and _is_context_compatible(current_context, prefix):
                current_context = prefix
        else:
            current_content.append(line)

    if current_heading is not None and current_content:
        content_str = '\n'.join(current_content).strip()
        sections.append((current_heading, content_str, current_context))

    return sections


def sanitize_filename(name: str) -> str:
    """将字符串转换为安全的文件名"""
    name = name.strip()
    name = name.replace('/', '_').replace('\\', '_')
    name = name.replace(':', '_').replace('*', '_')
    name = name.replace('?', '_').replace('"', '_')
    name = name.replace('<', '_').replace('>', '_').replace('|', '_')
    name = name.replace(' ', '_')
    if len(name) > 80:
        name = name[:80]
    return name


def extract_section_prefix(heading: str) -> str:
    """从章节标题中正则提取章节编号前缀

    匹配模式：
    - "Section 1.1 Exercises" → "1.1"
    - "Section_1.1_Exercises" → "1.1"
    - "Chapter 2" → "2"
    - "§ X.Y" → "X.Y"
    - "第一章"/"第2节" → "1"/"2"
    - 纯数字开头 → 取开头数字部分
    - 不匹配 → ""（不加前缀）
    """
    # Section/SECTION X.Y 格式
    m = re.match(r'Section[_\s](\d+[\.\d]*)', heading, re.IGNORECASE)
    if m:
        return m.group(1)
    # Chapter X 格式（大小写不敏感）
    m = re.match(r'Chapter[_\s](\d+)', heading, re.IGNORECASE)
    if m:
        return m.group(1)
    # § X.Y 格式
    m = re.match(r'§[_\s]*(\d+[\.\d]*)', heading)
    if m:
        return m.group(1)
    # 中文章节/节：第一章 → 1，第2节 → 2，第3章.4 → 3.4
    m = re.match(r'第(\d+[\.\d]*)[章节部分]', heading)
    if m:
        return m.group(1)
    # 数字开头 + 后续描述文字 → 章节编号
    m = re.match(r'^(\d+\.\d+[\.\d]*)\s+\w', heading)
    if m:
        return m.group(1)
    m = re.match(r'^(\d+)\.\s+\w', heading)
    if m:
        return m.group(1)
    m = re.match(r'^(\d+)\s+\w', heading)
    if m:
        return m.group(1)
    return ""


def _is_context_compatible(current_ctx: str, new_prefix: str) -> bool:
    """判断新章节前缀是否与当前上下文兼容

    兼容规则：
    - 点号编号（如 "1.1"、"2.7"）总是兼容——它们是明确的节标题
    - 整数编号（如 "5"、"105"）只在正向过渡时兼容：
      当前章号 <= 新章号，防止题号覆盖章节上下文
    """
    if not current_ctx:
        return True
    if '.' in new_prefix:
        return True
    cur_ch = current_ctx.split('.')[0]
    new_ch = new_prefix
    if cur_ch.isdigit() and new_ch.isdigit():
        return int(new_ch) >= int(cur_ch)
    return True


# ==================== _q/_a 配对（先分别提取，再按题号合并） ====================


def _detect_qa_pairs(input_dir: Path) -> list[tuple[Path, Path]]:
    """检测目录中的 _q.md / _a.md 文件对

    匹对规则：stem 相同（去掉 _q / _a 后缀），如
      "problem book_q.md" ↔ "problem book_a.md"

    Returns: [(q_path, a_path), ...] 配对列表
    """
    q_files = {f.stem.rstrip("_q"): f for f in input_dir.glob("*_q.md")}
    a_files = {f.stem.rstrip("_a"): f for f in input_dir.glob("*_a.md")}
    pairs = []
    for stem in q_files:
        if stem in a_files:
            pairs.append((q_files[stem], a_files[stem]))
    return pairs


def _filter_solution_sections(split_dir: Path) -> Path:
    """从 _a 文件的切分目录中，只保留 SOLUTION 章节，删除重复题目章节

    _a 文件切分后同时含重复题目章节（如 # CHAPTER 1）和解答章节（如 # CHAPTER 1: SOLUTIONS）。
    此函数删除不含 SOLUTION/ANSWER 关键词的章节文件，仅保留纯解答章节。

    Returns:
        处理后的目录路径（与输入相同）
    """
    _solution_keywords = re.compile(r'SOLUTION|ANSWER', re.IGNORECASE)
    md_files = list(split_dir.glob("*.md"))
    removed = 0

    for md_file in md_files:
        # 读取标题行（第一个 # 行）判断是否为解答章节
        first_line = md_file.read_text(encoding="utf-8").split("\n")[0].strip()
        heading_text = first_line.lstrip("#").strip()
        if not _solution_keywords.search(heading_text):
            md_file.unlink()
            removed += 1
            print(f"  [过滤] 删除非解答章节: {md_file.name}")

    print(f"[阶段 0.5] 过滤 _a 切分文件：删除 {removed} 个非解答章节，保留 {len(md_files) - removed} 个")
    return split_dir


def _extract_matching_key(file_path: Path) -> str:
    """从提取后的题目/解答文件名中提取匹配键（problem_id + sub_id）

    文件名格式: {book_num}_s{ctx}_{problem_id}_{sub_id}{suffix}.md
    匹配键 = problem_id + sub_id（不含 book_num 和 ctx）

    例如:
      1_s3_3.20.md → "3.20"
      1_s3_3.20_a.md → "3.20_a"
      1_3.20_ans.md → "3.20" (去掉 _ans suffix)
    """
    stem = file_path.stem
    # 去掉已知后缀
    for sfx in ("_ans", "_a", "_q"):
        if stem.endswith(sfx):
            stem = stem[:-len(sfx)]
            break

    parts = stem.split("_")
    # 跳过 book_num (第一个部分)
    idx = 1
    # 跳过 s-prefix (s + 数字)
    if idx < len(parts) and parts[idx].startswith("s") and len(parts[idx]) > 1 and parts[idx][1:].isdigit():
        idx += 1

    # 剩余部分 = problem_id + sub_id
    remaining = parts[idx:]
    return "_".join(remaining) if remaining else stem


def _extract_matching_key_from_content(file_path: Path) -> str:
    """从文件内容前几行提取题号作为匹配键（fallback）

    适用于文件名不含题号的情况。从 "Problem X.Y" 或 "Solution X.Y" 提取。
    """
    content = file_path.read_text(encoding="utf-8")
    for line in content.split("\n")[:3]:
        line = line.strip()
        if not line:
            continue
        # Problem X.Y / Solution X.Y
        m = re.match(r'(?:Problem|Solution)\s+(\d+[\.\d]*)', line, re.IGNORECASE)
        if m:
            pid = m.group(1)
            # 尝试提取小问号
            sm = re.search(r'\(([a-z\d]+)\)', line.split("$")[0] if "$" in line else line)
            if sm:
                return f"{pid}_{sm.group(1)}"
            return pid
    return ""


def merge_qa_results(q_dir: Path, a_dir: Path, output_dir: Path) -> Path:
    """按题号配对合并已提取的题目文件和解答文件

    Args:
        q_dir: 题目 md 文件目录（_q 提取结果）
        a_dir: 解答 md 文件目录（_a 提取结果）
        output_dir: 合并输出目录

    Returns:
        合并后的输出目录
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    # 构建解答文件索引：{matching_key: file_path}
    a_by_key = {}
    for f in a_dir.glob("*.md"):
        key = _extract_matching_key(f)
        if not key or key.startswith("unk"):
            key = _extract_matching_key_from_content(f)
        if key:
            a_by_key[key] = f

    matched = 0
    unmatched_q = 0
    unmatched_a_keys = set(a_by_key.keys())

    # 合并每个题目文件：只输出成功配对的
    for q_file in q_dir.glob("*.md"):
        key = _extract_matching_key(q_file)
        if not key or key.startswith("unk"):
            key = _extract_matching_key_from_content(q_file)

        a_file = a_by_key.get(key) if key else None
        if a_file:
            q_content = q_file.read_text(encoding="utf-8")
            a_content = a_file.read_text(encoding="utf-8")
            merged = f"{q_content}\n\n## Solution\n\n{a_content}"
            unmatched_a_keys.discard(key)
            matched += 1

            output_file = output_dir / q_file.name
            output_file.write_text(merged, encoding="utf-8")

    print(f"[QA合并] 配对 {matched} 组，题目未配对 {unmatched_q}，解答未配对 {len(unmatched_a_keys)}（仅输出配对成功的）")
    return output_dir


def _extract_book_num_from_dirname(file_path: Path) -> str:
    """从文件路径中提取书号（查找最近含纯数字的目录名）

    例如: main/1/xxx_split/file.md → '1'
    直接父目录可能不是数字（如 _split），所以向上查找。
    """
    for parent in [file_path.parent, file_path.parent.parent]:
        if parent.name.isdigit():
            return parent.name
    return ""


MIN_LINES = 0       # 提取的题目最少行数，低于此值的丢弃
MAX_CHUNK_LINES = 500  # 章节文件最大行数，超过则切分
OVERLAP_LINES = 50     # 切分时的重叠行数


def _filter_short_sections(sections: list[tuple]) -> list[tuple]:
    """过滤掉有效行数低于 MIN_LINES 的章节"""
    filtered = []
    skipped = 0
    for section in sections:
        content = section[1]
        lines = [l for l in content.split('\n') if l.strip()]
        if len(lines) < MIN_LINES:
            skipped += 1
            continue
        filtered.append(section)
    if skipped:
        print(f"  过滤掉 {skipped} 个过短章节（< {MIN_LINES} 行）")
    return filtered


def _extract_book_num_from_filename(filename: str) -> str:
    """从书文件名提取书号前缀，如 '003_xxx.md' → '003'"""
    stem = Path(filename).stem
    parts = stem.split('_')
    if parts and parts[0].isdigit():
        return parts[0]
    return ""


def extract_book_number(file_path: Path) -> str:
    """从文件名或目录名中提取书号

    优先级：
      1. 文件名数字前缀（如 003_xxx.md → 003）
      2. 父目录名（如 main/1/ → 1）
      3. 合并文件名中的书号（如 1@book@1@... → 1）
      4. "unk"

    文件名格式: {书号}@{书名}@{章节.md}
    """
    # 尝试从 @ 分隔的文件名提取（stage1/merge 输出格式）
    parts = file_path.stem.split('@')
    if len(parts) >= 2 and parts[0] and parts[0] != "unk":
        return parts[0]
    # 尝试文件名数字前缀
    num = _extract_book_num_from_filename(file_path.name)
    if num:
        return num
    # 尝试父目录名
    dir_num = _extract_book_num_from_dirname(file_path)
    if dir_num:
        return dir_num
    return "unk"


def extract_section_idx(file_path: Path) -> str:
    """从 stage1 文件名中提取章节序号"""
    parts = file_path.stem.split('@')
    if len(parts) >= 4:
        return parts[2]
    return ""


def extract_chapter_context(file_path: Path) -> str:
    """从 stage1 文件名中提取章节上下文（含数字标题的数字前缀）"""
    parts = file_path.stem.split('@')
    if len(parts) >= 5:
        return parts[3]
    return ""


# ==================== Stage 1: 按标题切分 ====================


def stage1_split(input_file: str, output_dir: str = None,
                 heading_split: bool = True) -> Path:
    """按一级标题切分 md 文件或目录，文件名编码书名

    Args:
        input_file: 整书 md 文件路径或包含 md 文件的目录
        output_dir: 切分输出目录（默认在输入文件旁创建 _split 目录）
        heading_split: True 时按一级标题切分，False 时每个文件作为一个整体章节
    """
    input_path = Path(input_file)

    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.name}_split"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # 输入是目录：对每个 md 文件按标题切分，书名编码进文件名
    if input_path.is_dir():
        md_files = list(input_path.glob("*.md"))
        if not md_files:
            print("输入目录中未找到任何 .md 文件")
            return None

        total_sections = 0
        sec_offset = 0
        for md_file in sorted(md_files):
            book_num = _extract_book_num_from_filename(md_file.name)
            book_name = sanitize_filename(md_file.stem)

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            if heading_split:
                sections = split_by_heading(content)
                if not sections:
                    heading = content.split('\n')[0].strip() if content.split('\n') else md_file.stem
                    ctx = extract_section_prefix(heading.lstrip('#').strip()) if heading.startswith('#') else ""
                    sections = [(heading, content, ctx)]

                sections = _filter_short_sections(sections)
            else:
                heading = content.split('\n')[0].strip() if content.split('\n') else md_file.stem
                ctx = extract_section_prefix(heading.lstrip('#').strip()) if heading.startswith('#') else ""
                sections = [(heading, content, ctx)]

            for sec_idx, section in enumerate(sections, 1):
                total_sections += 1
                global_sec_idx = sec_offset + sec_idx
                heading, section_content, ctx = section[0], section[1], section[2] if len(section) >= 3 else ""
                safe_heading = sanitize_filename(heading)
                output_file = output_dir / f"{book_num}@{book_name}@{global_sec_idx}@{ctx}@{safe_heading}.md"

                full_content = f"{heading}\n\n{section_content}"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(full_content)

            sec_offset += len(sections)

        print(f"[阶段 1] 从目录切分 {len(md_files)} 个文件为 {total_sections} 个章节")
        return output_dir

    # 输入是文件：书号和书名从文件名提取
    book_num = _extract_book_num_from_filename(input_path.name)
    book_name = sanitize_filename(input_path.stem)

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if heading_split:
        sections = split_by_heading(content)
        if not sections:
            print("未找到任何一级标题，无法切分")
            return None

        sections = _filter_short_sections(sections)
    else:
        heading = content.split('\n')[0].strip() if content.split('\n') else input_path.stem
        ctx = extract_section_prefix(heading.lstrip('#').strip()) if heading.startswith('#') else ""
        sections = [(heading, content, ctx)]

    for i, section in enumerate(sections, 1):
        heading, section_content, ctx = section[0], section[1], section[2] if len(section) >= 3 else ""
        safe_heading = sanitize_filename(heading)
        output_file = output_dir / f"{book_num}@{book_name}@{i}@{ctx}@{safe_heading}.md"

        full_content = f"{heading}\n\n{section_content}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"  [{book_num}] sec{i} {heading[:50]}... -> {output_file.name}")

    print(f"[阶段 1] 找到 {len(sections)} 个章节")
    return output_dir


# ==================== 大章节二次切分 ====================


def chunk_large_sections(input_dir: Path, max_lines: int = MAX_CHUNK_LINES,
                         overlap: int = OVERLAP_LINES) -> Path:
    """将超过 max_lines 行的章节文件切分为多个块，块之间有 overlap 行重叠

    切分后的块保留原文件的一级标题作为首行，文件名加 _p1/_p2 等后缀。
    原大文件被删除。

    Args:
        input_dir: stage1_split 输出的章节文件目录
        max_lines: 每块最大行数
        overlap: 相邻块的重叠行数

    Returns:
        处理后的目录路径（与输入相同）
    """
    md_files = list(input_dir.glob("*.md"))
    chunked_count = 0

    for md_file in sorted(md_files):
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) <= max_lines:
            continue

        # 提取一级标题（首行），每个块都保留
        heading = lines[0] if lines[0].startswith('#') else ""
        body_start = 1 if heading else 0
        body_lines = lines[body_start:]

        # 计算切分点：步长 = max_lines - overlap
        step = max_lines - overlap
        chunks = []
        start = 0
        while start < len(body_lines):
            end = min(start + max_lines, len(body_lines))
            chunk_body = body_lines[start:end]
            # 跳过尾部过短的块（合并到上一块）
            if len(chunk_body) <= overlap and chunks:
                chunks[-1].extend(chunk_body)
                break
            chunks.append(chunk_body)
            start += step

        # 写入每个块，删除原文件
        for i, chunk_body in enumerate(chunks, 1):
            stem = md_file.stem
            suffix = f"_p{i}" if len(chunks) > 1 else ""
            output_file = input_dir / f"{stem}{suffix}.md"

            content_lines = []
            if heading:
                content_lines.append(heading)
            content_lines.extend(chunk_body)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(content_lines)

        md_file.unlink()
        chunked_count += 1
        print(f"  [{md_file.name}] {len(lines)} 行 → {len(chunks)} 块")

    if chunked_count:
        print(f"[阶段 1.5] 切分了 {chunked_count} 个过大章节")
    else:
        print(f"[阶段 1.5] 无需二次切分")
    return input_dir


# ==================== LLM 提取题目 ====================

file_lock = threading.Lock()
problem_counter = {"count": 0}
fail_counter = {"count": 0}
_active_system_prompt = SYSTEM_PROMPT_EXTRACT  # 可被 stage2_extract 动态替换


def _strip_math(line: str) -> str:
    """去掉 $...$ 和 $$...$$ 中的数学表达式，防止误识别括号内容"""
    return re.sub(r'\$+.*?\$+', '', line)


def _extract_from_line(line: str) -> tuple[str, str]:
    """从单行提取题号和小问号，返回 (problem_id, sub_id)

    大题号从原始行提取；小问号只从小括号内容提取，
    且只扫描 $ 之前的部分，避免数学表达式中的括号被误识别。
    """
    # 小问号：只扫描 $ 之前的部分，匹配小括号里的内容
    pre_math = line.split('$')[0] if '$' in line else line
    sub_id = ""
    m = re.search(r'\(([a-z\d]+)\)', pre_math)
    if m:
        sub_id = m.group(1)

    # 大题号：从去掉 $ 内容后的行提取
    clean_line = _strip_math(line)
    # 匹配 x.xx.xx 格式（如 1.17.35）
    m = re.match(r'^(\d+\.\d+\.\d+)', clean_line)
    if m:
        return m.group(1), sub_id
    # 匹配 x.xx. 格式（如 1.17.、19.1.）
    m = re.match(r'^(\d+\.\d+)', clean_line)
    if m:
        return m.group(1), sub_id
    # 匹配 【数字】格式
    m = re.match(r'^【(\d+)】', clean_line)
    if m:
        return m.group(1), sub_id
    # 匹配 纯数字编号（如 1. 12.、382 . 允许数字和点之间有空格）
    m = re.match(r'^(\d+)\s*\.', clean_line)
    if m:
        return m.group(1), sub_id
    # 匹配 §x.x 格式
    m = re.match(r'^§(\d+[\.\d]*)', clean_line)
    if m:
        return m.group(1), sub_id
    # 匹配 No.xxx 格式
    m = re.match(r'^No\.(\d+)', clean_line, re.IGNORECASE)
    if m:
        return m.group(1), sub_id
    # 匹配 纯数字后跟空格和非数字（如 2 (a)、5 some text）
    m = re.match(r'^(\d+)\s(?!\d)', clean_line)
    if m:
        return m.group(1), sub_id

    return "", sub_id


def extract_problem_id(block: str) -> tuple[str, str]:
    """从题目 md 开头几行提取题号和小问号

    Returns: (problem_id, sub_id)
      - problem_id: 主题号，如 "3.1.15"
      - sub_id: 小问号，如 "a"，或 ""（无小问）
    """
    problem_id = ""
    sub_id = ""
    lines = block.split('\n')[:3]

    for line in lines:
        pid, sid = _extract_from_line(line.strip())
        if pid and not problem_id:
            problem_id = pid
        if sid and not sub_id:
            sub_id = sid

    return problem_id, sub_id


def _parse_id_line(line: str) -> tuple[str, str]:
    """解析 #ID:题号|小问号 标记行，返回 (problem_id, sub_id)

    格式：
    - #ID:1.17.35 → ("1.17.35", "")
    - #ID:1.17.35|a → ("1.17.35", "a")
    - #ID:unk → ("unk", "")
    """
    m = re.match(r'^#ID:(.+?)(?:\|(.+))?$', line.strip())
    if m:
        return m.group(1), m.group(2) or ""
    return "", ""


def process_file(file_path: Path, output_dir: Path, suffix: str = "") -> int:
    """处理单个章节文件：调用 LLM 提取题目，每个题目保存为独立 md 文件

    Args:
        file_path: 章节文件路径
        output_dir: 输出目录
        suffix: 输出文件名后缀

    Returns:
        提取的题目数量
    """
    book_num = extract_book_number(file_path)
    ctx = extract_chapter_context(file_path) or extract_section_idx(file_path)
    print(f"Processing: {file_path.name} (书号: {book_num}, 章节上下文: {ctx or '无'})")

    try:
        result = ask_ai(
            prompt="请从文件中提取所有题目，按指定格式输出。",
            files=str(file_path),
            system=_active_system_prompt,
            model=MODEL_EXTRACT,
        )

        # LLM 返回 NONE 表示没有题目，删除源文件并跳过
        if result.strip().upper() == 'NONE':
            try:
                file_path.unlink()
                print(f"  [{file_path.name}] 无题目，已删除")
            except Exception as e:
                print(f"  [{file_path.name}] 删除失败：{e}")
            return 0

        # 按分割线提取每道题
        blocks = re.split(r'^---$', result, flags=re.MULTILINE)
        count = 0
        for block in blocks:
            block = block.strip()
            if not block or block.upper() == 'NONE':
                continue

            lines = [l for l in block.split('\n') if l.strip()]
            if not lines:
                continue

            # 从 #ID: 标记行提取题号和小问号
            problem_id, sub_id = _parse_id_line(lines[0])
            if not problem_id:
                problem_id, sub_id = extract_problem_id(block)
            if not problem_id and not sub_id:
                problem_id = f"unk{problem_counter['count'] + count + 1}"

            # 命名格式：{书号}_{章节序号}_{题号}_{小问号}_suffix
            name_parts = [book_num, f"s{ctx}", problem_id] if ctx else [book_num, problem_id]
            if sub_id:
                name_parts.append(sub_id)
            output_name = sanitize_filename("_".join(name_parts) + suffix)
            output_file = output_dir / f"{output_name}.md"

            # 防止文件名冲突
            if output_file.exists():
                dup_idx = 1
                while output_file.exists():
                    dup_idx += 1
                    output_file = output_dir / f"{output_name}_{dup_idx}.md"

            # 保存内容时去掉 #ID: 标记行
            content_lines = lines[1:] if lines[0].strip().startswith('#ID:') else lines
            content = '\n'.join(content_lines)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

        # 删除源文件（已处理完成）
        try:
            file_path.unlink()
        except Exception as e:
            print(f"  [{file_path.name}] 删除失败：{e}")

        with file_lock:
            problem_counter["count"] += count
        print(f"  [{file_path.name}] 提取 {count} 道题目并删除")
        return count

    except Exception as e:
        print(f"  [{file_path.name}] 失败：{e}")
        with file_lock:
            fail_counter["count"] += 1
        return 0


def stage2_extract(input_dir: str, output_dir: str = None, max_workers: int = 4,
                   suffix: str = "", skip_stage1: bool = False,
                   system_prompt: str = None) -> tuple[Path, int]:
    """并行提取题目为单独 md 文件，书号从 stage1 文件名自动提取

    Args:
        input_dir: stage1 输出的章节文件目录
        output_dir: 提取后的题目 md 文件目录
        max_workers: 并发数
        suffix: 输出文件名后缀（如 "_ans"）
        skip_stage1: True 时将 input_dir 当作已有文件直接提取
        system_prompt: 自定义 system prompt（默认用 SYSTEM_PROMPT_EXTRACT）

    Returns:
        (output_dir, fail_count)
    """
    global problem_counter, fail_counter, _active_system_prompt
    problem_counter = {"count": 0}
    fail_counter = {"count": 0}
    _active_system_prompt = system_prompt or SYSTEM_PROMPT_EXTRACT

    input_path = Path(input_dir)

    if output_dir is None:
        output_dir = input_path.parent / "question_splited"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    if skip_stage1:
        if not input_path.is_dir():
            files = [input_path]
        else:
            files = list(input_path.glob("*.md"))
    else:
        files = list(input_path.glob("*.md"))

    print(f"[阶段 2] 找到 {len(files)} 个文件，开始提取题目 (并发数：{max_workers})..." +
          (f"，后缀：{suffix}" if suffix else ""))

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_file, f, output_dir, suffix): f for f in files}
        for future in as_completed(futures):
            future.result()

    fc = fail_counter["count"]
    if fc:
        print(f"[阶段 2] 完成！提取 {problem_counter['count']} 道题目，{fc} 个文件失败")
    else:
        print(f"[阶段 2] 完成！共提取 {problem_counter['count']} 道题目")
    print(f"  输出目录：{output_dir}\n")
    return output_dir, fc


# ==================== 主 Pipeline ====================


def run_split_pipeline(input_file: str,
                       stage1_output: str = None,
                       stage2_output: str = None,
                       max_workers: int = 8,
                       suffix: str = "",
                       skip_stage1: bool = False,
                       heading_split: bool = True) -> Path:
    """
    运行拆分流水线：切分 → 大章节二次切分 → LLM提取题目

    Args:
        input_file: 输入文件路径或目录
        stage1_output: 阶段 1 输出目录（可选）
        stage2_output: 阶段 2 输出目录（可选）
        max_workers: LLM 提取并发数
        suffix: 输出文件名后缀（如 "_ans"）
        skip_stage1: 跳过阶段1，直接从 input_file 目录提取题目
        heading_split: 阶段1是否按一级标题切分

    Returns:
        最终输出目录路径（题目 md 文件所在目录）
    """
    input_path = Path(input_file)

    print("=" * 60)
    print("题目拆分 Pipeline")
    print("=" * 60)
    print(f"输入：{input_file} ({'目录' if input_path.is_dir() else '文件'})")
    print(f"并发数：{max_workers}")
    print("=" * 60 + "\n")

    # ---- 检测 _q/_a 配对：先分别提取，再按题号合并 ----
    qa_pairs = None
    if input_path.is_dir():
        qa_pairs = _detect_qa_pairs(input_path)

    if qa_pairs:
        print(f"[阶段 0] 检测到 {len(qa_pairs)} 组 _q/_a 文件对，分别提取后配对\n")

        # 对 _q 文件：正常提取题目
        q_final_dir = None
        a_final_dir = None
        for q_path, a_path in qa_pairs:
            # ---- 提取题目 (_q) ----
            print(f"  === 提取题目: {q_path.name} ===")
            q_split_dir = stage1_split(str(q_path))
            if q_split_dir is None:
                raise RuntimeError("_q 文件切分失败")
            chunk_large_sections(q_split_dir)
            q_result_dir, q_fail = stage2_extract(q_split_dir, stage2_output, max_workers, suffix)
            if q_final_dir is None:
                q_final_dir = q_result_dir
            else:
                # 合并到同一目录
                for f in q_result_dir.glob("*.md"):
                    dest = q_final_dir / f.name
                    if not dest.exists():
                        f.rename(dest)

            # ---- 提取解答 (_a)：只保留 SOLUTION 章节 ----
            print(f"\n  === 提取解答: {a_path.name} ===")
            a_split_dir = stage1_split(str(a_path))
            if a_split_dir is None:
                raise RuntimeError("_a 文件切分失败")
            # 过滤掉非 SOLUTION 章节（_a 含重复题目章节）
            _filter_solution_sections(a_split_dir)
            chunk_large_sections(a_split_dir)
            # 解答提取用专用的 solution prompt，输出到 _a 专用目录
            a_output_dir = q_split_dir.parent / (q_split_dir.name + "_ans")
            a_result_dir, a_fail = stage2_extract(
                a_split_dir,
                output_dir=str(a_output_dir),
                max_workers=max_workers,
                suffix="_ans",
                system_prompt=SYSTEM_PROMPT_EXTRACT_SOLUTION,
            )
            if a_final_dir is None:
                a_final_dir = a_result_dir

        # ---- 按题号配对合并 ----
        print(f"\n  === 按题号配对合并 ===")
        final_dir = merge_qa_results(q_final_dir, a_final_dir,
                                     Path(str(q_final_dir) + "_merged"))
    else:
        # 无 _q/_a 对，走正常 pipeline
        if skip_stage1:
            stage1_dir = input_path
            print(f"[跳过切分] 直接从 {input_file} 提取题目")
        else:
            stage1_dir = stage1_split(input_file, stage1_output, heading_split)
            if stage1_dir is None:
                raise RuntimeError("阶段 1 失败")

            # 阶段 1.5：大章节二次切分
            chunk_large_sections(stage1_dir)

        # 阶段 2：LLM 提取题目
        final_dir, fail_count = stage2_extract(stage1_dir, stage2_output, max_workers, suffix)

        if fail_count:
            print("=" * 60)
            print(f"拆分 Pipeline 部分失败！{fail_count} 个章节未能提取")
            print(f"最终输出：{final_dir}")
            print("=" * 60)
        else:
            print("=" * 60)
            print("拆分 Pipeline 完成！")
            print(f"最终输出：{final_dir}")
            print("=" * 60)

    return final_dir