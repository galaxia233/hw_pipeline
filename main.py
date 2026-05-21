"""hw_pipeline: abstract & generate GR problems"""

from pathlib import Path
import json

from core.cleaner import clean_json_file
from core.formatter import abstract_question_to_json
from core.pipeline import generate_from_seed
from core.validator import validate_json_file
from core.config import MODEL_ABSTRACT, MODEL_COMPOSE, MODEL_SUBSTITUTE, MODEL_PICK_METRIC, MODEL_VALIDATE, MODEL_FIX

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    import argparse

    parser = argparse.ArgumentParser(description="GR problem pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # abstract 子命令
    p_abstract = subparsers.add_parser("abstract", help="格式化题目为 JSON")
    p_abstract.add_argument("files", nargs="+", help="题目文件路径 (md, pdf, image)")
    p_abstract.add_argument("--source", default="generated", help="来源标签")
    p_abstract.add_argument("-o", "--output", default=None, help="输出 JSON 文件路径")

    # generate 子命令
    p_gen = subparsers.add_parser("generate", help="基于种子题目生成新度规+新题目")
    p_gen.add_argument("seed_json", help="种子题目 JSON 文件路径")
    p_gen.add_argument("--num", type=int, default=3, help="生成题目数量 (默认 3)")
    p_gen.add_argument("--subs", type=int, default=3, help="每道题的度规替换数量 (默认 3)")
    p_gen.add_argument("-o", "--output-dir", default=None, help="输出目录")

    # run 子命令：一步完成 abstract → generate
    p_run = subparsers.add_parser("run", help="一步完成：抽象化 + 泛化生成")
    p_run.add_argument("input", help="输入文件 (md, pdf, image, 或已有的 JSON)")
    p_run.add_argument("--num", type=int, default=3, help="生成题目数量 (默认 3)")
    p_run.add_argument("--subs", type=int, default=3, help="每道题的度规替换数量 (默认 3)")
    p_run.add_argument("-o", "--output-dir", default=None, help="输出目录")

    # clean 子命令
    p_clean = subparsers.add_parser("clean", help="清理 JSON 文件中的排版符号")
    p_clean.add_argument("files", nargs="+", help="需要清理的 JSON 文件路径")
    p_clean.add_argument("-o", "--output-dir", default=None, help="输出目录 (默认原地覆盖)")

    # validate 子命令
    p_validate = subparsers.add_parser("validate", help="用 EinsteinPy 验证题目答案正确性")
    p_validate.add_argument("files", nargs="+", help="需要验证的 JSON 文件路径")

    args = parser.parse_args()

    if args.command == "abstract":
        result = abstract_question_to_json(files=args.files, source=args.source)
        output_path = args.output or str(Path(args.files[0]).with_suffix(".json"))
        Path(output_path).write_text(result, encoding="utf-8")
        print(f"已保存到 {output_path}")

    elif args.command == "generate":
        stem = Path(args.seed_json).stem
        output_dir = args.output_dir or str(Path(args.seed_json).parent)

        total = args.num + args.num * args.subs
        print(f"正在生成 {args.num} 道基础题 + {args.num * args.subs} 道度规替换题 (共 {total} 道)...")
        generate_from_seed(args.seed_json, num=args.num, num_subs=args.subs, output_dir=output_dir, stem=stem)

    elif args.command == "run":
        input_path = Path(args.input)
        output_dir = args.output_dir or str(input_path.parent)
        stem = input_path.stem

        # Step 1: 如果输入不是 JSON，先抽象化
        if input_path.suffix.lower() != ".json":
            print(f"步骤 1: 抽象化 {input_path.name} (模型: {MODEL_ABSTRACT})...")
            result = abstract_question_to_json(files=[str(input_path)], source=stem)
            seed_json_path = str(input_path.with_suffix(".json"))
            Path(seed_json_path).write_text(result, encoding="utf-8")
            print(f"  已保存种子 JSON: {seed_json_path}")
        else:
            seed_json_path = str(input_path)
            print(f"使用已有种子 JSON: {seed_json_path}")

        # Step 1.5: 缓存 Fact Sheet（算一次，后续直接读取）
        from core.validator import _compute_fact_sheet_for_problem
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
        print(f"模型配置: compose={MODEL_COMPOSE}, substitute={MODEL_SUBSTITUTE}, pick={MODEL_PICK_METRIC}, validate={MODEL_VALIDATE}, fix={MODEL_FIX}")
        print(f"步骤 2: 正在生成 {args.num} 道基础题 + {args.num * args.subs} 道度规替换题 (共 {total} 道)...")
        generate_from_seed(seed_json_path, num=args.num, num_subs=args.subs, output_dir=output_dir, stem=stem)

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
        for fpath in args.files:
            validate_json_file(fpath)