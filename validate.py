"""validate.py — 数据集合规与覆盖度自检。

用法: python validate.py dataset.jsonl
"""

import json
import sys
import random
from collections import Counter

REQUIRED_TOP = ["id", "statement", "answer", "meta", "verification"]
REQUIRED_META = ["source_id", "source_type", "stage", "lineage"]


def main(path):
    items, errs = [], []
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        try:
            p = json.loads(line)
        except Exception as e:
            errs.append(f"line {ln}: not JSON: {e}")
            continue

        for k in REQUIRED_TOP:
            if k not in p:
                errs.append(f"line {ln}: missing top-level '{k}'")
        for k in REQUIRED_META:
            if k not in p.get("meta", {}):
                errs.append(f"line {ln}: missing meta.'{k}'")
        if not p.get("answer"):
            errs.append(f"line {ln}: empty answer (use NO_ANSWER if open)")
        if not p.get("verification", {}).get("judge"):
            errs.append(f"line {ln}: no judge verification record")
        if not p.get("meta", {}).get("lineage"):
            errs.append(f"line {ln}: empty lineage (hard reject)")
        items.append(p)

    print(f"== validate {path} ==")
    print(f"total: {len(items)}, errors: {len(errs)}")
    if errs[:5]:
        print("first errors:\n  " + "\n  ".join(errs[:5]))

    by_src = Counter(p["meta"].get("source_id", "?") for p in items)
    by_type = Counter(p["meta"].get("source_type", "?") for p in items)
    by_stage = Counter(p["meta"].get("stage", "?") for p in items)
    by_form = Counter(p["meta"].get("cognitive_form", "?") for p in items)
    by_env = Counter(p["meta"].get("physics_env", "?") for p in items)
    by_soft = Counter(p["meta"].get("soft_variant", "?") for p in items)

    print(f"\nsources covered: {len(by_src)}; by type: {dict(by_type)}")
    print(f"by stage: {dict(by_stage)}")
    print(f"cognitive_form distinct: {len(by_form)}; values: {dict(by_form.most_common(8))}")
    print(f"physics_env distinct: {len(by_env)}; values: {dict(by_env.most_common(8))}")
    print(f"soft_variant distinct: {len(by_soft)}; values: {dict(by_soft.most_common(8))}")

    # 验证通过率
    has_judge = sum(1 for p in items if p.get("verification", {}).get("judge"))
    judge_correct = sum(1 for p in items if p.get("verification", {}).get("judge", {}).get("correct"))
    has_red_team = sum(1 for p in items if p.get("verification", {}).get("red_team"))
    red_survives = sum(1 for p in items if p.get("verification", {}).get("red_team", {}).get("survives"))

    print(f"\nverification stats:")
    print(f"  judge: {has_judge}/{len(items)} ({judge_correct}/{has_judge} correct)")
    print(f"  red_team: {has_red_team}/{len(items)} ({red_survives}/{has_red_team} survives)")

    # schema 校验通过率
    schema_ok = sum(1 for p in items if all(
        k in p for k in REQUIRED_TOP
    ) and all(
        k in p.get("meta", {}) for k in REQUIRED_META
    ) and p.get("answer") and p.get("meta", {}).get("lineage"))
    print(f"  schema pass: {schema_ok}/{len(items)} ({schema_ok/len(items)*100:.1f}%)")

    # 多样性覆盖度检查（三轴各≥5）
    print(f"\ndiversity coverage (target: each axis ≥ 5):")
    print(f"  cognitive_form: {len(by_form)} distinct  {'✓' if len(by_form) >= 5 else '✗ (need more)'}")
    print(f"  physics_env:    {len(by_env)} distinct  {'✓' if len(by_env) >= 5 else '✗ (need more)'}")
    print(f"  soft_variant:   {len(by_soft)} distinct  {'✓' if len(by_soft) >= 5 else '✗ (need more)'}")

    # 随机 10 条样例
    print("\n== random 10 sample ids ==")
    for p in random.sample(items, min(10, len(items))):
        meta = p.get("meta", {})
        print(f"  {p['id']}  "
              f"src={meta.get('source_id', '?')}  "
              f"stage={meta.get('stage', '?')}  "
              f"form={meta.get('cognitive_form', '?')}  "
              f"env={meta.get('physics_env', '?')}  "
              f"TV={meta.get('training_value', '?')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python validate.py dataset.jsonl")
        sys.exit(1)
    main(sys.argv[1])