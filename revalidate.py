"""批量重新验证+修正已有的题目 JSON 文件。

用法：
  python revalidate.py <目录> [--max-attempts 1] [--workers 6] [--skip-validated]

默认给每道题 1 次修正机会（max_attempts=1），即验证失败后自动 fix 再验证一次。
--skip-validated: 跳过已通过验证的题目，只处理 degraded 的。
"""

import json
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from core.common.config import MODEL_VALIDATE, MODEL_JUDGE, MODEL_RED_TEAM, MODEL_FIX
from core.verify.validator import validate_and_fix_loop


def revalidate_file(path: Path, max_attempts: int = 1) -> dict:
    """重新验证+修正一个 JSON 文件。"""
    problem_dict = json.loads(path.read_text(encoding="utf-8"))
    md = problem_dict.get("metadata", {})

    old_validated = md.get("validated", False)
    old_degraded = md.get("degraded", False)

    result = validate_and_fix_loop(problem_dict, max_attempts=max_attempts, base_temperature=0.7)

    new_validated = result["metadata"].get("validated", False)
    new_degraded = result["metadata"].get("degraded", False)

    # 写回文件
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "file": path.name,
        "old_validated": old_validated,
        "old_degraded": old_degraded,
        "new_validated": new_validated,
        "new_degraded": new_degraded,
        "changed": old_validated != new_validated,
    }


def main():
    parser = argparse.ArgumentParser(description="批量重新验证+修正题目")
    parser.add_argument("input_dir", help="包含题目 JSON 的目录")
    parser.add_argument("--max-attempts", type=int, default=1, help="修正次数 (默认1)")
    parser.add_argument("--workers", type=int, default=6, help="并行线程数 (默认6)")
    parser.add_argument("--skip-validated", action="store_true", help="跳过已通过验证的题目")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    files = sorted(input_dir.glob("*.json"))
    if not files:
        print(f"{input_dir} 中没有 JSON 文件")
        sys.exit(1)

    if args.skip_validated:
        # 只处理 degraded 的
        to_process = []
        for f in files:
            d = json.loads(f.read_text(encoding="utf-8"))
            if d.get("metadata", {}).get("degraded", False):
                to_process.append(f)
        print(f"跳过已验证，只处理 {len(to_process)}/{len(files)} 道 degraded 题")
        files = to_process
    else:
        print(f"处理全部 {len(files)} 道题")

    print(f"模型: judge={MODEL_JUDGE}, red_team={MODEL_RED_TEAM}, fix={MODEL_FIX}")
    print(f"修正次数: {args.max_attempts}, 并行: {args.workers}")

    results = []
    recovered = 0

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(revalidate_file, f, args.max_attempts): f for f in files}
        for future in as_completed(futures):
            try:
                r = future.result()
                results.append(r)
                if r["old_degraded"] and r["new_validated"]:
                    recovered += 1
                    print(f"  ✓ 恢复: {r['file']}")
                elif r["old_validated"] and r["new_validated"]:
                    pass  # 仍然通过，无需报告
                elif not r["old_validated"] and not r["new_validated"]:
                    print(f"  ✗ 仍然失败: {r['file']}")
            except Exception as e:
                print(f"  ✗ 处理失败: {e}")

    # 汇总
    total = len(results)
    new_validated = sum(1 for r in results if r["new_validated"])
    new_degraded = sum(1 for r in results if r["new_degraded"])
    old_validated = sum(1 for r in results if r["old_validated"])

    print(f"\n=== 汇总 ===")
    print(f"处理: {total} 道")
    print(f"之前: validated={old_validated}, degraded={total - old_validated}")
    print(f"之后: validated={new_validated}, degraded={new_degraded}")
    print(f"恢复: {recovered} 道 (从 degraded → validated)")
    print(f"通过率: {old_validated}/{total} → {new_validated}/{total} "
          f"({old_validated/total*100:.1f}% → {new_validated/total*100:.1f}%)")


if __name__ == "__main__":
    main()