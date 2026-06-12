"""hw_pipeline book-level pipeline: 从整书 md 提取题目 → 抽象化 → 泛化生成

完整流程：
  Stage 1: 整书 md → 按标题切分 → LLM 提取题目为独立 md 文件 (core/extractor)
  Stage 2: 每道题目 md → 抽象化为 seed JSON (core/formatter)
  Stage 3: 每个 seed JSON → 泛化生成新题目 (core/pipeline)

用法：
  python book_pipeline.py run <book.md> [--num 3] [--subs 3] [-o output_dir]
  python book_pipeline.py extract <book.md> [-o output_dir]
  python book_pipeline.py abstract <split_dir> [-o output_dir]
  python book_pipeline.py generate <abstracted_dir> [--num 3] [--subs 3] [-o output_dir]
"""

from pathlib import Path
import json
import sys

from core.seed.extractor import run_split_pipeline
from core.seed.formatter import abstract_question_to_json
from core.scale.pipeline import generate_from_seed
from core.verify.validator import _compute_fact_sheet_for_problem
from core.common.cleaner import clean_problem
from core.common.config import MODEL_ABSTRACT, MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC, MODEL_EXTRACT
from schema import problem_to_dataset_record, problem_to_flat_record, write_dataset_parquet


# ==================== papers.json 生成 ====================


def _build_papers_json(problem_files: list, seed_paths: list, results: list,
                        input_path: Path) -> list:
    """从 pipeline 各阶段的数据构建 papers.json 语料追踪清单。

    Returns:
        list of dicts: [{source_id, source_type, status, seed_count, output_count, notes}]
    """
    # 按 source_id 聚合
    sources = {}

    # Stage 1: 原始语料
    for pf in problem_files:
        book_num = extract_book_number(pf) or "unk"
        source_id = str(input_path) if input_path.is_file() else book_num
        if source_id not in sources:
            sources[source_id] = {
                "source_id": source_id,
                "source_type": "textbook",
                "status": "extracted",
                "seed_count": 0,
                "output_count": 0,
                "notes": f"从 {input_path.name} 提取",
            }

    # Stage 2: 抽象化
    for sp in seed_paths:
        # 种子题的 source_id 从文件内容或文件名推断
        try:
            seed_data = json.loads(sp.read_text(encoding="utf-8"))
            source_id = seed_data.get("metadata", {}).get("source_id") or seed_data.get("metadata", {}).get("source") or str(input_path)
        except Exception:
            source_id = str(input_path)
        if source_id not in sources:
            sources[source_id] = {
                "source_id": source_id,
                "source_type": "textbook",
                "status": "seeded",
                "seed_count": 0,
                "output_count": 0,
                "notes": "",
            }
        sources[source_id]["seed_count"] += 1
        sources[source_id]["status"] = "seeded"

    # Stage 3: 泛化产出
    for r in results:
        if not r or r[-1] is None:
            continue
        problem = r[-1]
        source_id = problem.metadata.source_id or problem.metadata.source or str(input_path)
        if source_id not in sources:
            sources[source_id] = {
                "source_id": source_id,
                "source_type": problem.metadata.source_type or "textbook",
                "status": "completed",
                "seed_count": 0,
                "output_count": 0,
                "notes": "",
            }
        sources[source_id]["output_count"] += 1

    # 更新最终状态
    for s in sources.values():
        if s["output_count"] > 0:
            s["status"] = "completed"
        elif s["seed_count"] > 0:
            s["status"] = "seeded"
        else:
            s["status"] = "extracted"

    return list(sources.values())


# ==================== Stage 2: 抽象化 ====================


def abstract_problem_files(problem_files: list[Path], output_dir: Path,
                           max_workers: int = 20) -> list[Path]:
    """将每个题目 md 文件抽象化为 seed JSON，缓存 Fact Sheet。

    Args:
        problem_files: 提取出的题目 md 文件列表
        output_dir: seed JSON 输出目录
        max_workers: 并发数

    Returns:
        成功生成的 seed JSON 文件路径列表（按文件名排序）
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from dataclasses import asdict
    from schema import Problem

    output_dir.mkdir(parents=True, exist_ok=True)

    def do_abstract(md_file: Path) -> tuple[Path, Path | None, bool]:
        source = md_file.stem
        seed_path = output_dir / f"{source}.json"

        # 断点续跑：已有 seed JSON 则跳过
        if seed_path.exists():
            try:
                existing = json.loads(seed_path.read_text(encoding="utf-8"))
                if "metadata" in existing and "origin" in existing:
                    return (md_file, seed_path, True)  # skipped
            except Exception:
                print(f"  已有文件损坏，重新生成: {seed_path}")

        try:
            print(f"  抽象化: {md_file.name} (source: {source}, model: {MODEL_ABSTRACT})...")
            print(f"  抽象化: {md_file.name} (source: {source}, model: {MODEL_ABSTRACT})...")
            result = abstract_question_to_json(files=[str(md_file)], source=source)

            seed_path = output_dir / f"{source}.json"
            seed_path.write_text(result, encoding="utf-8")
            print(f"  已保存 seed JSON: {seed_path}")

            # 缓存 Fact Sheet
            seed_data = json.loads(result)
            if "cached_fact_sheet" not in seed_data:
                print(f"    计算 Fact Sheet...")
                fs = _compute_fact_sheet_for_problem(seed_data)
                if "error" not in fs:
                    seed_data["cached_fact_sheet"] = fs
                    seed_path.write_text(
                        json.dumps(seed_data, ensure_ascii=False, indent=2),
                        encoding="utf-8"
                    )
                    print(f"    Fact Sheet 已缓存")
                else:
                    print(f"    Fact Sheet 计算失败: {fs['error']}")
            else:
                print(f"    使用已缓存的 Fact Sheet")

            return (md_file, seed_path, False)  # newly generated

        except Exception as e:
            print(f"  抽象化失败: {md_file.name}: {e}")
            return (md_file, None, False)

    # 并行处理
    seed_paths = []
    skipped = 0
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(do_abstract, f): f for f in problem_files}
        for future in as_completed(futures):
            md_file, seed_path, was_skipped = future.result()
            if seed_path:
                if was_skipped:
                    skipped += 1
                seed_paths.append(seed_path)

    # 按文件名排序，保证顺序稳定
    seed_paths.sort(key=lambda p: p.name)

    print(f"\n[Stage 2] 抽象化完成: {len(seed_paths)}/{len(problem_files)} 道题目成功 (跳过已有 {skipped} 个)")
    return seed_paths


# ==================== Stage 3: 泛化生成 ====================


def generate_from_seeds(seed_paths: list[Path], num: int = 3, num_subs: int = 3,
                        num_soft_rewrites: int = 1, soft_rewrite_types: list = None,
                        cognitive_forms: list = None,
                        cross_metric: bool = False, num_cross_metrics: int = 2,
                        max_workers: int = 3, output_dir: Path = None) -> list:
    """对每个 seed JSON 运行泛化生成（跨种子并行）。

    Args:
        seed_paths: seed JSON 文件路径列表
        num: 每道种子题生成的基础题数量（cognitive_forms 指定时被覆盖）
        num_subs: 每道基础题的度规替换数量
        num_soft_rewrites: 每道基础题的软改写数量
        soft_rewrite_types: 软改写类型列表
        cognitive_forms: 认知形式列表（指定时每种 form 独立生成）
        cross_metric: True 时 Phase 1 增加跨度规泛化
        num_cross_metrics: 跨度规模式下挑选的目标度规数量
        max_workers: 并发种子数
        output_dir: 变体输出目录

    Returns:
        所有生成结果的列表
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = []
    # 估算总产出（不含软改写时）
    per_seed = len(cognitive_forms) if cognitive_forms else num
    total_planned = len(seed_paths) * (per_seed + per_seed * num_subs + per_seed * num_soft_rewrites)
    print(f"  模型配置: compose={MODEL_COMPOSE}, substitute={MODEL_SUBSTITUTE}, "
          f"pick={MODEL_PICK_METRIC}, extract={MODEL_EXTRACT}")
    print(f"  每道种子题: {per_seed} 基础 + {per_seed * num_subs} 度规替换 + {per_seed * num_soft_rewrites} 软改写")
    print(f"  总计划: ~{total_planned} 道 (并发种子数: {max_workers})")

    def do_gen_seed(seed_path: Path) -> list:
        stem = seed_path.stem
        print(f"\n  === 泛化生成: {stem} ===")
        try:
            results = generate_from_seed(
                str(seed_path), num=num, num_subs=num_subs,
                num_soft_rewrites=num_soft_rewrites,
                soft_rewrite_types=soft_rewrite_types,
                cognitive_forms=cognitive_forms,
                cross_metric=cross_metric, num_cross_metrics=num_cross_metrics,
                output_dir=str(output_dir), stem=stem
            )
            return results
        except Exception as e:
            print(f"  泛化生成失败: {stem}: {e}")
            return []

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(do_gen_seed, sp): sp for sp in seed_paths}
        for future in as_completed(futures):
            try:
                results = future.result()
                all_results.extend(results)
            except Exception as e:
                print(f"  种子生成异常: {e}")

    print(f"\n[Stage 3] 泛化生成完成: 共 {len(all_results)} 道题目")
    return all_results


# ==================== 完整 Book Pipeline ====================


def run_book_pipeline(input_file: str, num: int = 3, num_subs: int = 3,
                      num_soft_rewrites: int = 1, cognitive_forms: list = None,
                      cross_metric: bool = False, num_cross_metrics: int = 2,
                      output_dir: str = None, split_workers: int = 8, gen_workers: int = 3,
                      only: str = None, dataset_format: str = "jsonl") -> Path:
    """运行完整 book pipeline: extract → abstract → generate

    Args:
        input_file: 整书 md 文件路径
        num: 每道种子题生成的基础题数量（cognitive_forms 指定时被覆盖）
        num_subs: 每道基础题的度规替换数量
        num_soft_rewrites: 每道基础题的软改写数量
        cognitive_forms: 认知形式列表（指定时每种 form 独立生成）
        cross_metric: True 时 Phase 1 增加跨度规泛化
        num_cross_metrics: 跨度规模式下挑选的目标度规数量
        output_dir: 输出根目录
        split_workers: 题目提取并发数
        gen_workers: 泛化生成并发种子数
        only: 只跑某阶段 ('extract' / 'abstract' / 'generate')

    Returns:
        最终输出目录路径
    """
    input_path = Path(input_file)
    output_root = Path(output_dir) if output_dir else input_path.parent / "book_output"
    output_root.mkdir(parents=True, exist_ok=True)

    # ---- Stage 1: 提取题目 ----
    if only != 'abstract' and only != 'generate':
        print(f"\n{'=' * 60}")
        print("[Stage 1] 从整书 md 提取题目")
        print(f"{'=' * 60}\n")

        split_dir = run_split_pipeline(input_file, max_workers=split_workers)
        problem_files = sorted(split_dir.glob("*.md"))

        print(f"\n  共提取 {len(problem_files)} 道题目")
        print(f"  输出目录: {split_dir}")

        if only == 'extract':
            return split_dir

        if not problem_files:
            print("  未提取到任何题目，终止")
            return output_root
    else:
        # 从已有目录读取
        if only == 'abstract':
            split_dir = Path(input_file) if Path(input_file).is_dir() else output_root / "split"
        else:
            split_dir = output_root / "split"
        problem_files = sorted(split_dir.glob("*.md"))
        if not problem_files:
            print(f"  {split_dir} 中未找到题目 md 文件")
            return output_root

    # ---- Stage 2: 抽象化 ----
    if only != 'generate':
        print(f"\n{'=' * 60}")
        print("[Stage 2] 抽象化题目为 seed JSON")
        print(f"{'=' * 60}\n")

        abstracted_dir = output_root / "abstracted"
        seed_paths = abstract_problem_files(problem_files, abstracted_dir)

        if only == 'abstract':
            return abstracted_dir

        if not seed_paths:
            print("  所有题目抽象化失败，终止")
            return output_root
    else:
        # 从已有目录读取 seed JSON
        abstracted_dir = Path(input_file) if Path(input_file).is_dir() else output_root / "abstracted"
        seed_paths = sorted(abstracted_dir.glob("*.json"))
        if not seed_paths:
            print(f"  {abstracted_dir} 中未找到 seed JSON 文件")
            return output_root

    # ---- Stage 3: 泛化生成 ----
    print(f"\n{'=' * 60}")
    print("[Stage 3] 泛化生成新题目")
    print(f"{'=' * 60}\n")

    variants_dir = output_root / "variants"
    results = generate_from_seeds(seed_paths, num=num, num_subs=num_subs,
                                  num_soft_rewrites=num_soft_rewrites,
                                  cognitive_forms=cognitive_forms,
                                  cross_metric=cross_metric, num_cross_metrics=num_cross_metrics,
                                  max_workers=gen_workers,
                                  output_dir=variants_dir)

    print(f"\n{'=' * 60}")
    print("Book Pipeline 完成！")
    print(f"{'=' * 60}")
    print(f"  题目提取: {len(problem_files)} 道")
    print(f"  抽象化成功: {len(seed_paths)} 道")
    print(f"  泛化生成: {len(results)} 道")
    print(f"  输出目录: {output_root}")

    # 汇总 dataset
    problems = [r[-1] for r in results if r and r[-1] is not None]
    if problems:
        ext = ".parquet" if dataset_format == "parquet" else ".jsonl"
        dataset_path = output_root / f"dataset{ext}"
        if dataset_format == "parquet":
            flat_records = [problem_to_flat_record(p) for p in problems]
            write_dataset_parquet(flat_records, str(dataset_path), from_dict=True)
        else:
            records = [problem_to_dataset_record(p) for p in problems]
            dataset_path.write_text(
                "\n".join(json.dumps(rec, ensure_ascii=False) for rec in records),
                encoding="utf-8",
            )
        print(f"  dataset{ext}: {len(problems)} 道题 → {dataset_path}")

    # 生成 papers.json（语料追踪）
    papers = _build_papers_json(problem_files, seed_paths, results, input_path)
    papers_path = output_root / "papers.json"
    papers_path.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  papers.json: {len(papers)} 条语料 → {papers_path}")

    print(f"{'=' * 60}")

    return output_root


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    import argparse

    parser = argparse.ArgumentParser(description="Book-level GR problem pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # run 子命令：一步完成 extract → abstract → generate
    p_run = subparsers.add_parser("run", help="完整流程：提取 → 抽象化 → 泛化生成")
    p_run.add_argument("input", help="整书 md 文件路径")
    p_run.add_argument("--num", type=int, default=3, help="每道种子题生成的基础题数量 (默认 3)")
    p_run.add_argument("--subs", type=int, default=2, help="每道基础题的度规替换数量 (默认 2)")
    p_run.add_argument("--soft", type=int, default=1, help="每道基础题的软改写数量 (默认 1)")
    p_run.add_argument("--forms", nargs="+", default=None,
                       choices=["derivation", "numerical", "conceptual", "code", "multiple_choice", "open"],
                       help="指定认知形式列表（覆盖 --num，每种 form 独立生成一道题）")
    p_run.add_argument("--cross-metric", action="store_true", help="Phase 1 增加跨度规泛化")
    p_run.add_argument("--num-cross-metrics", type=int, default=2, help="跨度规模式下挑选的目标度规数量 (默认 2)")
    p_run.add_argument("-o", "--output-dir", default=None, help="输出根目录")
    p_run.add_argument("-w", "--split-workers", type=int, default=8, help="题目提取并发数")
    p_run.add_argument("--gen-workers", type=int, default=3, help="泛化生成并发种子数")
    p_run.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")

    # extract 子命令：只提取题目
    p_extract = subparsers.add_parser("extract", help="只提取题目为 md 文件")
    p_extract.add_argument("input", help="整书 md 文件路径")
    p_extract.add_argument("-o", "--output-dir", default=None, help="输出目录")
    p_extract.add_argument("-w", "--split-workers", type=int, default=8, help="并发数")

    # abstract 子命令：只抽象化
    p_abstract = subparsers.add_parser("abstract", help="只抽象化题目为 JSON")
    p_abstract.add_argument("input", help="题目 md 文件目录（extract 输出）")
    p_abstract.add_argument("-o", "--output-dir", default=None, help="输出目录")

    # generate 子命令：只泛化生成
    p_gen = subparsers.add_parser("generate", help="只泛化生成新题目")
    p_gen.add_argument("input", help="seed JSON 目录（abstract 输出）")
    p_gen.add_argument("--num", type=int, default=3, help="基础题数量 (默认 3)")
    p_gen.add_argument("--subs", type=int, default=2, help="度规替换数量 (默认 2)")
    p_gen.add_argument("--soft", type=int, default=1, help="软改写数量 (默认 1)")
    p_gen.add_argument("--forms", nargs="+", default=None,
                       choices=["derivation", "numerical", "conceptual", "code", "multiple_choice", "open"],
                       help="指定认知形式列表")
    p_gen.add_argument("--cross-metric", action="store_true", help="Phase 1 增加跨度规泛化")
    p_gen.add_argument("--num-cross-metrics", type=int, default=2, help="跨度规模式下挑选的目标度规数量 (默认 2)")
    p_gen.add_argument("--gen-workers", type=int, default=3, help="并发种子数")
    p_gen.add_argument("-o", "--output-dir", default=None, help="输出目录")
    p_gen.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")

    args = parser.parse_args()

    if args.command == "run":
        run_book_pipeline(
            input_file=args.input,
            num=args.num,
            num_subs=args.subs,
            num_soft_rewrites=args.soft,
            cognitive_forms=args.forms,
            cross_metric=args.cross_metric,
            num_cross_metrics=args.num_cross_metrics,
            output_dir=args.output_dir,
            split_workers=args.split_workers,
            gen_workers=args.gen_workers,
            dataset_format=args.dataset_format,
        )

    elif args.command == "extract":
        run_book_pipeline(
            input_file=args.input,
            output_dir=args.output_dir,
            split_workers=args.split_workers,
            only="extract",
        )

    elif args.command == "abstract":
        run_book_pipeline(
            input_file=args.input,
            output_dir=args.output_dir,
            only="abstract",
        )

    elif args.command == "generate":
        run_book_pipeline(
            input_file=args.input,
            num=args.num,
            num_subs=args.subs,
            num_soft_rewrites=args.soft,
            cognitive_forms=args.forms,
            cross_metric=args.cross_metric,
            num_cross_metrics=args.num_cross_metrics,
            output_dir=args.output_dir,
            gen_workers=args.gen_workers,
            only="generate",
            dataset_format=args.dataset_format,
        )