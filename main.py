"""hw_pipeline: abstract & generate GR problems"""

from pathlib import Path
import json

from core.common.cleaner import clean_json_file
from core.common.config import MODEL_ABSTRACT, MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC, MODEL_VALIDATE, MODEL_FIX
from core.common.report import generate_report
from core.common.stats import BatchResult
from core.seed.formatter import abstract_question_to_json
from core.scale.pipeline import generate_from_seed
from core.verify.validator import validate_json_file, _compute_fact_sheet_for_problem
from book_pipeline import abstract_problem_files
from schema import problem_to_dataset_record, problem_to_flat_record, dict_to_flat_record, write_dataset_parquet, write_json_dir_to_parquet


def _dict_to_dataset_record(problem_dict: dict) -> dict:
    """将 pipeline 内部格式的 dict 转为 dataset.jsonl 格式。

    pipeline 内部格式: {metadata, physical_data, origin, verification}
    dataset.jsonl 格式: {id, statement, answer, solution, meta, verification}
    """
    from schema import TYPE_TO_COGNITIVE
    md = problem_dict.get("metadata", {})
    pd = problem_dict.get("physical_data", {})
    og = problem_dict.get("origin", {})
    vf = problem_dict.get("verification") or {}

    # answer 处理
    answer = og.get("answer")
    if answer is None or (answer and "无答案" in answer):
        answer = "NO_ANSWER"

    # cognitive_form 处理
    cognitive_form = md.get("cognitive_form") or TYPE_TO_COGNITIVE.get(md.get("type", ""), md.get("type", ""))

    # physics_env 处理
    physics_env = md.get("physics_env") or md.get("tags", {}).get("metric", "")

    # source_id 处理
    source_id = md.get("source_id") or md.get("source", "")

    # lineage 处理
    lineage = md.get("lineage") or [source_id]

    # topic 处理
    topic = md.get("topic") or md.get("tags", {}).get("scenario", "")

    # training_value 处理
    training_value = md.get("training_value")
    if training_value is None:
        judge = vf.get("judge", {})
        if judge:
            training_value = judge.get("training_value")

    return {
        "id": md.get("id", ""),
        "statement": og.get("question", ""),
        "answer": answer,
        "solution": og.get("solution") or "",
        "meta": {
            "source_id": source_id,
            "source_type": md.get("source_type", "problem_set"),
            "stage": md.get("stage", "seed"),
            "lineage": lineage,
            "topic": topic,
            "concepts": md.get("concepts", []),
            "tools_used": md.get("tools_used", []),
            "cognitive_form": cognitive_form,
            "physics_env": physics_env,
            "soft_variant": md.get("soft_variant") or "",
            "training_value": training_value,
            "degraded": md.get("degraded", False),
        },
        "verification": vf if vf else {},
    }


def _write_dataset(records_or_problems, path: str, format: str,
                    from_problem: bool = True, from_dict: bool = False):
    """统一写入 dataset 文件，根据 format 选择 jsonl 或 parquet

    Args:
        records_or_problems: Problem 对象列表 或 dict 列表
        path: 输出文件路径
        format: "jsonl" 或 "parquet"
        from_problem: True 时输入为 Problem 对象列表
        from_dict: True 时输入为 pipeline 内部 dict 列表（需先转为 flat/record）
    """
    from pathlib import Path

    if format == "parquet":
        if from_problem:
            flat_records = [problem_to_flat_record(p) for p in records_or_problems]
        elif from_dict:
            flat_records = [dict_to_flat_record(d) for d in records_or_problems]
        else:
            flat_records = records_or_problems
        write_dataset_parquet(flat_records, path, from_dict=True)
    else:
        # jsonl 格式
        if from_problem:
            dataset_records = [problem_to_dataset_record(p) for p in records_or_problems]
        elif from_dict:
            dataset_records = [_dict_to_dataset_record(d) for d in records_or_problems]
        else:
            dataset_records = records_or_problems
        Path(path).write_text(
            "\n".join(json.dumps(rec, ensure_ascii=False) for rec in dataset_records),
            encoding="utf-8",
        )


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    import argparse

    parser = argparse.ArgumentParser(description="GR problem pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # abstract 子命令
    p_abstract = subparsers.add_parser("abstract", help="格式化题目为 JSON")
    p_abstract.add_argument("files", nargs="+", help="题目文件或文件夹路径 (md/pdf/image，文件夹时自动扫描所有 md)")
    p_abstract.add_argument("--source", default="generated", help="来源标签")
    p_abstract.add_argument("-o", "--output", default=None, help="输出目录（文件夹模式时）或 JSON 文件路径（单文件时）")

    # generate 子命令
    p_gen = subparsers.add_parser("generate", help="基于种子题目生成新度规+新题目")
    p_gen.add_argument("seed_json", help="种子题目 JSON 文件路径")
    p_gen.add_argument("--num", type=int, default=3, help="生成题目数量 (默认 3)")
    p_gen.add_argument("--subs", type=int, default=2, help="每道题的度规替换数量 (默认 2)")
    p_gen.add_argument("--axes", nargs="*", default=None, help="泛化轴列表 (apply/extend/limit/compare/invert/verify)，不指定时自动分配")
    p_gen.add_argument("--form-changes", nargs="*", default=None, help="形式变换目标列表 (multiple_choice/code/conceptual)，不指定时使用默认三种")
    p_gen.add_argument("--cross-metric", action="store_true", help="Phase 1 增加跨度规泛化（为每种认知形式在不同目标度规下额外生成题目）")
    p_gen.add_argument("--num-cross-metrics", type=int, default=2, help="跨度规模式下挑选的目标度规数量 (默认 2)")
    p_gen.add_argument("-o", "--output-dir", default=None, help="输出目录")
    p_gen.add_argument("--dataset", default=None, help="输出 dataset 文件路径（汇总所有生成的题目）")
    p_gen.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")
    p_gen.add_argument("--report", default=None, help="输出运行报告 markdown 文件路径")

    # run 子命令：一步完成 abstract → generate
    p_run = subparsers.add_parser("run", help="一步完成：抽象化 + 泛化生成")
    p_run.add_argument("input", help="输入文件或文件夹 (md/json，文件夹时批量处理所有 md)")
    p_run.add_argument("--num", type=int, default=3, help="生成题目数量 (默认 3)")
    p_run.add_argument("--subs", type=int, default=2, help="每道题的度规替换数量 (默认 2)")
    p_run.add_argument("--soft", type=int, default=1, help="每道题的软改写数量 (默认 1)")
    p_run.add_argument("--axes", nargs="*", default=None, help="泛化轴列表 (apply/extend/limit/compare/invert/verify)，不指定时自动分配")
    p_run.add_argument("--form-changes", nargs="*", default=None, help="形式变换目标列表 (multiple_choice/code/conceptual)，不指定时使用默认三种")
    p_run.add_argument("--cross-metric", action="store_true", help="Phase 1 增加跨度规泛化")
    p_run.add_argument("--num-cross-metrics", type=int, default=2, help="跨度规模式下挑选的目标度规数量 (默认 2)")
    p_run.add_argument("-o", "--output-dir", default=None, help="输出目录")
    p_run.add_argument("--dataset", default=None, help="输出 dataset 文件路径（汇总所有生成的题目）")
    p_run.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")
    p_run.add_argument("--report", default=None, help="输出运行报告 markdown 文件路径")
    p_run.add_argument("--gen-workers", type=int, default=3, help="文件夹模式下的并行种子数 (默认 3)")

    # batch 子命令：批量处理整个文件夹
    p_batch = subparsers.add_parser("batch", help="批量处理文件夹中所有种子 JSON")
    p_batch.add_argument("input_dir", help="包含种子 JSON 文件的目录")
    p_batch.add_argument("--num", type=int, default=3, help="每道种子生成的题目数量 (默认 3)")
    p_batch.add_argument("--subs", type=int, default=2, help="每道题的度规替换数量 (默认 2)")
    p_batch.add_argument("--form-changes", nargs="*", default=None, help="形式变换目标列表")
    p_batch.add_argument("--num-soft", type=int, default=1, help="每道题的软改写数量 (默认 1)")
    p_batch.add_argument("--cross-metric", action="store_true", help="Phase 1 增加跨度规泛化")
    p_batch.add_argument("--num-cross-metrics", type=int, default=2, help="跨度规模式下挑选的目标度规数量 (默认 2)")
    p_batch.add_argument("-o", "--output-dir", default=None, help="输出目录")
    p_batch.add_argument("--dataset", default=None, help="输出 dataset 文件路径")
    p_batch.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")
    p_batch.add_argument("--report", default=None, help="输出运行报告 markdown 文件路径")
    p_batch.add_argument("--parallel", type=int, default=3, help="并行种子数 (默认 3)")

    # clean 子命令
    p_clean = subparsers.add_parser("clean", help="清理 JSON 文件中的排版符号")
    p_clean.add_argument("files", nargs="+", help="需要清理的 JSON 文件路径")
    p_clean.add_argument("-o", "--output-dir", default=None, help="输出目录 (默认原地覆盖)")

    # validate 子命令
    p_validate = subparsers.add_parser("validate", help="用 EinsteinPy 验证题目答案正确性")
    p_validate.add_argument("files", nargs="*", help="需要验证的 JSON 文件路径")
    p_validate.add_argument("--dir", default=None, help="批量验证整个目录中的 JSON 文件")
    p_validate.add_argument("--workers", type=int, default=6, help="并行验证线程数 (默认 6)")
    p_validate.add_argument("--skip-validated", action="store_true", help="跳过已经 validated=true 的文件")
    p_validate.add_argument("--max-attempts", type=int, default=1, help="每道题最大验证/修正尝试次数 (默认 1)")

    # precompute 子命令
    p_precompute = subparsers.add_parser("precompute", help="预计算度规库中所有度规的 Fact Sheet 并缓存")
    p_precompute.add_argument("--force", action="store_true", help="强制重新计算所有度规（覆盖已有缓存）")
    p_precompute.add_argument("--include-heavy", action="store_true", help="也预计算 heavy 度规（耗时较长）")

    # aggregate 子命令（增强版）
    p_aggregate = subparsers.add_parser("aggregate", help="扫描目录中的 JSON 文件，汇总为 dataset")
    p_aggregate.add_argument("input_dir", help="包含题目 JSON 文件的目录")
    p_aggregate.add_argument("-o", "--output", default=None, help="输出 dataset 文件路径（默认在 input_dir 下）")
    p_aggregate.add_argument("--format", choices=["jsonl", "parquet"], default="jsonl", dest="dataset_format", help="dataset 输出格式 (默认 jsonl)")
    p_aggregate.add_argument("--skip-degraded", action="store_true", help="跳过 degraded 的题目")
    p_aggregate.add_argument("--skip-seeds", action="store_true", help="跳过 stage=seed 的种子题")
    p_aggregate.add_argument("--min-training-value", type=float, default=0.0, help="最低训练价值过滤 (默认 0.0)")
    p_aggregate.add_argument("--report", default=None, help="输出运行报告 markdown 文件路径")
    p_aggregate.add_argument("--papers", default=None, help="输出 papers.json 文件路径")

    args = parser.parse_args()

    if args.command == "abstract":
        # 检查是否有文件夹输入
        input_paths = [Path(f) for f in args.files]
        dirs = [p for p in input_paths if p.is_dir()]
        files = [p for p in input_paths if not p.is_dir()]

        if dirs:
            # Folder mode: 扫描目录中的 md 文件，批量抽象化
            md_files = sorted([f for d in dirs for f in d.glob("*.md")])
            if not md_files:
                print("指定目录中没有 md 文件")
                sys.exit(1)
            output_dir = Path(args.output) if args.output else dirs[0] / "abstracted"
            output_dir.mkdir(parents=True, exist_ok=True)
            seed_paths = abstract_problem_files(md_files, output_dir)
            print(f"抽象化完成: {len(seed_paths)}/{len(md_files)} 道题目 → {output_dir}")
        else:
            # Single/multi file mode (原有行为)
            result = abstract_question_to_json(files=args.files, source=args.source)
            output_path = args.output or str(Path(args.files[0]).with_suffix(".json"))
            Path(output_path).write_text(result, encoding="utf-8")
            print(f"已保存到 {output_path}")

    elif args.command == "generate":
        stem = Path(args.seed_json).stem
        output_dir = args.output_dir or str(Path(args.seed_json).parent)

        total = args.num + args.num * args.subs
        if args.cross_metric:
            total += args.num * args.num_cross_metrics
        axes_str = ", axes=" + str(args.axes) if args.axes else ""
        print(f"正在生成 {args.num} 道基础题 + {args.num * args.subs} 道度规替换题"
              f"{' + ' + str(args.num * args.num_cross_metrics) + ' 道跨度规题' if args.cross_metric else ''}"
              f" (共约 {total} 道){axes_str}...")
        problems, pipeline_result = generate_from_seed(
            args.seed_json, num=args.num, num_subs=args.subs,
            generalization_axes=args.axes, form_changes=args.form_changes,
            cross_metric=args.cross_metric, num_cross_metrics=args.num_cross_metrics,
            output_dir=output_dir, stem=stem)

        # 汇总 dataset
        if args.dataset or problems:
            fmt = args.dataset_format
            ext = ".parquet" if fmt == "parquet" else ".jsonl"
            dataset_path = args.dataset or str(Path(output_dir) / f"dataset{ext}")
            _write_dataset(problems, dataset_path, fmt, from_problem=True)
            print(f"已汇总 {len(problems)} 道题到 {dataset_path}")

        # 运行报告
        if args.report:
            report_text = generate_report(pipeline_result, mode="B")
            Path(args.report).write_text(report_text, encoding="utf-8")
            print(f"运行报告已保存到 {args.report}")

    elif args.command == "run":
        input_path = Path(args.input)

        if input_path.is_dir():
            # === Folder mode: 批量抽象化 + 泛化 ===
            output_dir = Path(args.output_dir) if args.output_dir else input_path / "output"
            output_dir.mkdir(parents=True, exist_ok=True)

            md_files = sorted(input_path.glob("*.md"))
            _skip = {"papers.json", "dataset.jsonl"}
            json_files = sorted(f for f in input_path.glob("*.json") if f.name not in _skip)

            seed_paths = []

            if md_files:
                # Step 1: 抽象化所有 md 文件
                print(f"步骤 1: 抽象化 {len(md_files)} 个题目 (模型: {MODEL_ABSTRACT})...")
                abstracted_dir = output_dir / "abstracted"
                seed_paths = abstract_problem_files(md_files, abstracted_dir)

                if not seed_paths:
                    print("所有题目抽象化失败，终止")
                    sys.exit(1)
                print(f"步骤 1 完成: {len(seed_paths)}/{len(md_files)} 道题目成功")
            elif json_files:
                print(f"使用已有的 {len(json_files)} 个 seed JSON")
                seed_paths = json_files
            else:
                print(f"{input_path} 中没有 md 或 json 文件")
                sys.exit(1)

            # Step 2: 泛化生成所有 seed JSON
            total_per_seed = args.num + args.num * args.subs + args.num * args.soft
            total = total_per_seed * len(seed_paths)
            if args.cross_metric:
                total += args.num * args.num_cross_metrics * len(seed_paths)
            axes_str = ", axes=" + str(args.axes) if args.axes else ""
            print(f"\n步骤 2: 泛化生成 {len(seed_paths)} 道种子题"
                  f" (每道 {args.num} 基础 + {args.num * args.subs} 度规替换 + {args.num * args.soft} 软改写"
                  f"{' + ' + str(args.num * args.num_cross_metrics) + ' 跨度规' if args.cross_metric else ''}"
                  f", 共约 {total} 道){axes_str}...")
            print(f"模型配置: compose={MODEL_COMPOSE}, substitute={MODEL_SUBSTITUTE}, "
                  f"pick={MODEL_PICK_METRIC}, validate={MODEL_VALIDATE}, fix={MODEL_FIX}")

            variants_dir = output_dir / "variants"
            variants_dir.mkdir(parents=True, exist_ok=True)

            all_problems = []
            pipeline_results = []
            failed = []
            skipped = 0

            for i, seed_path in enumerate(seed_paths):
                stem = seed_path.stem

                # 断点续跑：已有变体输出则跳过该种子题
                # 检查 _gen_ 文件是否存在（Phase 1 的基础题文件名）
                # 只检查 _gen_ 即可判断是否已处理过该种子题
                existing_gen = list(variants_dir.glob(f"{stem}_gen_*.json"))
                if existing_gen:
                    skipped += 1
                    continue

                try:
                    print(f"\n  --- [{i+1}/{len(seed_paths)}] {stem} ---")
                    problems, pipeline_result = generate_from_seed(
                        str(seed_path), num=args.num, num_subs=args.subs,
                        num_soft_rewrites=args.soft,
                        generalization_axes=args.axes, form_changes=args.form_changes,
                        cross_metric=args.cross_metric, num_cross_metrics=args.num_cross_metrics,
                        output_dir=str(variants_dir), stem=stem)
                    all_problems.extend(problems)
                    pipeline_results.append(pipeline_result)
                except Exception as e:
                    print(f"  生成失败: {stem}: {e}")
                    failed.append({"source_id": stem, "reason": str(e)[:200]})

            # 汇总 dataset
            if all_problems or args.dataset:
                fmt = args.dataset_format
                ext = ".parquet" if fmt == "parquet" else ".jsonl"
                dataset_path = args.dataset or str(output_dir / f"dataset{ext}")
                _write_dataset(all_problems, dataset_path, fmt, from_problem=True)
                print(f"\n已汇总 {len(all_problems)} 道题到 {dataset_path}")

            # 运行报告
            if args.report:
                from core.common.stats import BatchResult
                batch_result = BatchResult(seeds=pipeline_results, failed_sources=failed)
                batch_result.compute_totals()
                report_text = generate_report(batch_result, mode="B")
                Path(args.report).write_text(report_text, encoding="utf-8")
                print(f"运行报告已保存到 {args.report}")

            # 汇总
            print(f"\n=== 运行完成 ===")
            print(f"  种子题: {len(seed_paths)} 道 (跳过已有 {skipped}, 待处理 {len(seed_paths) - skipped})")
            print(f"  变体题: {len(all_problems)} 道 (成功 {len(pipeline_results)}, 失败 {len(failed)})")
            print(f"  输出目录: {output_dir}")

        else:
            # === Single file mode ===
            output_dir = args.output_dir or str(input_path.parent)
            stem = input_path.stem

            # Step 1: 如果输入不是 JSON，先抽象化（断点续跑：已有则跳过）
            seed_json_path = str(input_path.with_suffix(".json"))
            if input_path.suffix.lower() != ".json":
                if Path(seed_json_path).exists():
                    try:
                        existing = json.loads(Path(seed_json_path).read_text(encoding="utf-8"))
                        if "metadata" in existing and "origin" in existing:
                            print(f"  跳过已有种子 JSON: {seed_json_path}")
                        else:
                            raise ValueError("文件不完整")
                    except Exception:
                        print(f"步骤 1: 抽象化 {input_path.name} (已有文件损坏，重新生成)")
                        result = abstract_question_to_json(files=[str(input_path)], source=stem)
                        Path(seed_json_path).write_text(result, encoding="utf-8")
                        print(f"  已保存种子 JSON: {seed_json_path}")
                else:
                    print(f"步骤 1: 抽象化 {input_path.name} (模型: {MODEL_ABSTRACT})...")
                    result = abstract_question_to_json(files=[str(input_path)], source=stem)
                    Path(seed_json_path).write_text(result, encoding="utf-8")
                    print(f"  已保存种子 JSON: {seed_json_path}")
            else:
                seed_json_path = str(input_path)
                print(f"使用已有种子 JSON: {seed_json_path}")

            # Step 1.5: 缓存 Fact Sheet
            seed_data = json.loads(Path(seed_json_path).read_text(encoding="utf-8"))
            if "cached_fact_sheet" not in seed_data:
                print(f"  计算 Fact Sheet 并缓存...")
                fs = _compute_fact_sheet_for_problem(seed_data)
                if "error" in fs:
                    print(f"  Fact Sheet 计算失败: {fs['error']}")
                    print(f"  将在泛化时重新尝试计算")
                else:
                    seed_data["cached_fact_sheet"] = fs
                    Path(seed_json_path).write_text(json.dumps(seed_data, ensure_ascii=False, indent=2), encoding="utf-8")
                    print(f"  Fact Sheet 已缓存到 {seed_json_path}")
            else:
                print(f"  使用已缓存的 Fact Sheet")

            # Step 2: 泛化生成
            total = args.num + args.num * args.subs
            if args.cross_metric:
                total += args.num * args.num_cross_metrics
            axes_str = ", axes=" + str(args.axes) if args.axes else ""
            print(f"模型配置: compose={MODEL_COMPOSE}, substitute={MODEL_SUBSTITUTE}, pick={MODEL_PICK_METRIC}, validate={MODEL_VALIDATE}, fix={MODEL_FIX}")
            print(f"步骤 2: 正在生成 {args.num} 道基础题 + {args.num * args.subs} 道度规替换题"
                  f"{' + ' + str(args.num * args.num_cross_metrics) + ' 道跨度规题' if args.cross_metric else ''}"
                  f" (共约 {total} 道){axes_str}...")
            problems, pipeline_result = generate_from_seed(
                seed_json_path, num=args.num, num_subs=args.subs,
                num_soft_rewrites=args.soft,
                generalization_axes=args.axes, form_changes=args.form_changes,
                cross_metric=args.cross_metric, num_cross_metrics=args.num_cross_metrics,
                output_dir=output_dir, stem=stem)

            # 汇总 dataset.jsonl
            if args.dataset or problems:
                fmt = args.dataset_format
                ext = ".parquet" if fmt == "parquet" else ".jsonl"
                dataset_path = args.dataset or str(Path(output_dir) / f"dataset{ext}")
                _write_dataset(problems, dataset_path, fmt, from_problem=True)
                print(f"已汇总 {len(problems)} 道题到 {dataset_path}")

            # 运行报告
            if args.report:
                report_text = generate_report(pipeline_result, mode="B")
                Path(args.report).write_text(report_text, encoding="utf-8")
                print(f"运行报告已保存到 {args.report}")

    elif args.command == "batch":
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from core.common.api_client import reset_llm_stats

        input_dir = Path(args.input_dir)
        output_dir = args.output_dir or str(input_dir)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        json_files = sorted(input_dir.glob("*.json"))
        if not json_files:
            print(f"{input_dir} 中没有 JSON 文件")
            sys.exit(1)

        print(f"批量处理 {len(json_files)} 个种子 JSON (并行={args.parallel})")

        all_problems = []
        pipeline_results = []
        failed_sources = []

        # 串行处理（避免 API 并发过高），但每个种子内部已是并行
        for i, jf in enumerate(json_files):
            try:
                print(f"\n--- [{i+1}/{len(json_files)}] 处理 {jf.name} ---")
                problems, pipeline_result = generate_from_seed(
                    str(jf), num=args.num, num_subs=args.subs,
                    form_changes=args.form_changes,
                    cross_metric=args.cross_metric, num_cross_metrics=args.num_cross_metrics,
                    output_dir=output_dir, stem=jf.stem)
                all_problems.extend(problems)
                pipeline_results.append(pipeline_result)
            except Exception as e:
                print(f"  处理 {jf.name} 失败: {e}")
                failed_sources.append({
                    "source_id": jf.stem,
                    "type": "problem_set",
                    "status": "failed",
                    "reason": str(e)[:200],
                })

        # 构造 BatchResult
        batch_result = BatchResult(
            seeds=pipeline_results,
            failed_sources=failed_sources,
        )
        batch_result.compute_totals()

        # 汇总 dataset.jsonl
        if all_problems:
            fmt = args.dataset_format
            ext = ".parquet" if fmt == "parquet" else ".jsonl"
            dataset_path = args.dataset or str(Path(output_dir) / f"dataset{ext}")
            _write_dataset(all_problems, dataset_path, fmt, from_problem=True)
            print(f"\n已汇总 {len(all_problems)} 道题到 {dataset_path}")

        # papers.json
        papers_path = str(Path(output_dir) / "papers.json")
        papers = []
        for r in pipeline_results:
            papers.append({
                "source_id": r.seed_id,
                "source_type": "problem_set",
                "status": "completed",
                "seed_count": 1,
                "output_count": r.total_problems,
                "notes": f"validated={r.validated_count}, degraded={r.degraded_count}",
            })
        for fs in failed_sources:
            papers.append({
                "source_id": fs["source_id"],
                "source_type": fs.get("type", "problem_set"),
                "status": "failed",
                "seed_count": 1,
                "output_count": 0,
                "notes": fs.get("reason", ""),
            })
        Path(papers_path).write_text(
            json.dumps(papers, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"papers.json 已保存到 {papers_path}")

        # 运行报告
        if args.report:
            report_text = generate_report(batch_result, mode="B")
            Path(args.report).write_text(report_text, encoding="utf-8")
            print(f"运行报告已保存到 {args.report}")

        # 打印汇总
        print(f"\n=== 批量运行汇总 ===")
        print(f"种子: {len(json_files)} 个 (成功 {len(pipeline_results)}, 失败 {len(failed_sources)})")
        print(f"题目: {batch_result.total_problems} 道")
        print(f"多样性: {len(batch_result.diversity.get('cognitive_forms', set()))} 种认知形式, "
              f"{len(batch_result.diversity.get('physics_envs', set()))} 种度规, "
              f"{len(batch_result.diversity.get('soft_variants', set()))} 种软变体")
        print(f"LLM 调用: {batch_result.total_llm_calls} 次")
        print(f"耗时: {batch_result.total_wall_seconds:.1f}s ({batch_result.total_wall_seconds/3600:.1f}h)")

    elif args.command == "clean":
        out_dir = Path(args.output_dir) if args.output_dir else None
        for fpath in args.files:
            cleaned = clean_json_file(fpath)
            if out_dir:
                out_dir.mkdir(parents=True, exist_ok=True)
                dest = out_dir / Path(fpath).name
            else:
                dest = Path(fpath)
            dest.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"已清理 {dest}")

    elif args.command == "validate":
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from core.verify.validator import validate_and_fix_loop

        # 收集需要验证的文件列表
        validate_files = []
        if args.dir:
            dir_path = Path(args.dir)
            validate_files = sorted(dir_path.glob("*.json"))
            print(f"扫描目录 {args.dir}: 找到 {len(validate_files)} 个 JSON 文件")
        if args.files:
            for f in args.files:
                p = Path(f)
                if p.is_file():
                    validate_files.append(p)
                elif p.is_dir():
                    validate_files.extend(sorted(p.glob("*.json")))

        if not validate_files:
            print("没有找到需要验证的文件")
            sys.exit(1)

        # 如果 --skip-validated，过滤掉已验证的文件
        if args.skip_validated:
            to_validate = []
            for f in validate_files:
                try:
                    d = json.loads(f.read_text(encoding="utf-8"))
                    if not d.get("metadata", {}).get("validated", False):
                        to_validate.append(f)
                except Exception:
                    to_validate.append(f)  # 解析失败也验证
            skipped_count = len(validate_files) - len(to_validate)
            validate_files = to_validate
            print(f"跳过已验证文件 {skipped_count} 个，待验证 {len(validate_files)} 个")

        print(f"开始验证 {len(validate_files)} 个文件 (workers={args.workers}, max_attempts={args.max_attempts})")

        validated_ok = 0
        validated_fail = 0
        errors = 0

        def _do_validate(fpath):
            try:
                raw = json.loads(Path(fpath).read_text(encoding="utf-8"))
                result = validate_and_fix_loop(raw, max_attempts=args.max_attempts)
                Path(fpath).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
                is_ok = result.get("metadata", {}).get("validated", False)
                is_degraded = result.get("metadata", {}).get("degraded", False)
                return (str(fpath), is_ok, is_degraded, None)
            except Exception as e:
                return (str(fpath), False, False, str(e)[:200])

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(_do_validate, f): f for f in validate_files}
            for future in as_completed(futures):
                fpath, is_ok, is_degraded, err = future.result()
                name = Path(fpath).name
                if err:
                    errors += 1
                    print(f"  ❌ {name}: 错误 - {err}")
                elif is_ok:
                    validated_ok += 1
                    print(f"  ✅ {name}: 验证通过")
                elif is_degraded:
                    validated_fail += 1
                    print(f"  ⚠️ {name}: 验证失败 (degraded)")
                else:
                    validated_fail += 1
                    print(f"  ❌ {name}: 验证失败")

        print(f"\n=== 验证完成 ===")
        print(f"  通过: {validated_ok}/{len(validate_files)}")
        print(f"  失败: {validated_fail}/{len(validate_files)}")
        print(f"  错误: {errors}/{len(validate_files)}")

    elif args.command == "precompute":
        from core.common.fact_sheet_cache import build_cache
        build_cache(force=args.force, include_heavy=args.include_heavy)

    elif args.command == "aggregate":
        input_dir = Path(args.input_dir)
        fmt = args.dataset_format
        ext = ".parquet" if fmt == "parquet" else ".jsonl"
        output_path = args.output or str(input_dir / f"dataset{ext}")

        json_files = sorted(input_dir.glob("*.json"))
        if not json_files:
            print(f"{input_dir} 中没有 JSON 文件")
        else:
            records = []
            flat_records = []
            source_ids = set()
            skipped_degraded = 0
            skipped_seeds = 0
            skipped_tv = 0
            cognitive_forms = set()
            physics_envs = set()
            soft_variants = set()

            for jf in json_files:
                try:
                    data = json.loads(jf.read_text(encoding="utf-8"))
                    if "metadata" not in data or "origin" not in data:
                        continue

                    md = data["metadata"]

                    # 过滤
                    if args.skip_degraded and md.get("degraded", False):
                        skipped_degraded += 1
                        continue
                    if args.skip_seeds and md.get("stage", "") == "seed":
                        skipped_seeds += 1
                        continue
                    tv = md.get("training_value")
                    vf = data.get("verification") or {}
                    if tv is None:
                        judge = vf.get("judge") or {}
                        if judge.get("training_value") is not None:
                            tv = judge["training_value"]
                    if args.min_training_value > 0 and (tv is None or tv < args.min_training_value):
                        skipped_tv += 1
                        continue

                    if fmt == "parquet":
                        flat_rec = dict_to_flat_record(data)
                        flat_records.append(flat_rec)
                        # 仍用 flat record 的顶层字段做统计
                        cognitive_forms.add(flat_rec["cognitive_form"])
                        physics_envs.add(flat_rec["physics_env"])
                        soft_variants.add(flat_rec["soft_variant"])
                    else:
                        rec = _dict_to_dataset_record(data)
                        records.append(rec)
                        cognitive_forms.add(rec["meta"].get("cognitive_form", ""))
                        physics_envs.add(rec["meta"].get("physics_env", ""))
                        soft_variants.add(rec["meta"].get("soft_variant", ""))

                    source_ids.add(md.get("source_id") or md.get("source", ""))
                except Exception as e:
                    print(f"  跳过 {jf.name}: {e}")

            if fmt == "parquet":
                write_dataset_parquet(flat_records, output_path, from_dict=True)
            else:
                Path(output_path).write_text(
                    "\n".join(json.dumps(rec, ensure_ascii=False) for rec in records),
                    encoding="utf-8",
                )
            total_count = len(flat_records) if fmt == "parquet" else len(records)
            print(f"已汇总 {total_count} 道题到 {output_path} (扫描了 {len(json_files)} 个 JSON 文件)")
            if skipped_degraded:
                print(f"  跳过 {skipped_degraded} 道 degraded 题 (--skip-degraded)")
            if skipped_seeds:
                print(f"  跳过 {skipped_seeds} 道 seed 题 (--skip-seeds)")
            if skipped_tv:
                print(f"  跳过 {skipped_tv} 道 training_value < {args.min_training_value} 题")

            # papers.json
            if args.papers or total_count > 0:
                papers_path = args.papers or str(Path(input_dir) / "papers.json")
                papers = []
                for sid in sorted(source_ids):
                    if fmt == "parquet":
                        sid_count = sum(1 for r in flat_records if r["source_id"] == sid)
                    else:
                        sid_count = sum(1 for r in records if r["meta"]["source_id"] == sid)
                    papers.append({
                        "source_id": sid,
                        "source_type": "problem_set",
                        "status": "completed",
                        "seed_count": 1,
                        "output_count": sid_count,
                        "notes": "",
                    })
                Path(papers_path).write_text(
                    json.dumps(papers, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                print(f"papers.json 已保存到 {papers_path} ({len(papers)} 个来源)")

            # diversity 统计
            print(f"\n=== Diversity ===")
            print(f"cognitive_form: {len(cognitive_forms)} distinct — {sorted(cognitive_forms)}")
            print(f"physics_env: {len(physics_envs)} distinct — {sorted(physics_envs)}")
            print(f"soft_variant: {len(soft_variants)} distinct — {sorted(soft_variants)}")

            # 运行报告
            if args.report:
                # 从目录中的题目构造简单的 BatchResult
                from core.common.stats import PipelineResult
                from core.common.api_client import get_llm_stats
                diversity = {
                    "cognitive_forms": cognitive_forms,
                    "physics_envs": physics_envs,
                    "soft_variants": soft_variants,
                }
                if fmt == "parquet":
                    validated = sum(1 for r in flat_records if r.get("structural_ok", False))
                    degraded = sum(1 for r in flat_records if r.get("degraded", False))
                else:
                    validated = sum(1 for r in records if r.get("verification", {}).get("structural", {}).get("ok", False))
                    degraded = sum(1 for r in records if r["meta"].get("degraded", False))

                fake_result = PipelineResult(
                    seed_id="aggregate",
                    total_problems=total_count,
                    validated_count=validated,
                    degraded_count=degraded,
                    diversity=diversity,
                )
                report_text = generate_report(fake_result, mode="B", group_name="aggregate")
                Path(args.report).write_text(report_text, encoding="utf-8")
                print(f"运行报告已保存到 {args.report}")