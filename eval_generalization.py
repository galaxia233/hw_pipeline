"""评估泛化程度"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

files = sorted(Path(".").glob("test3*.json"))
metrics = set()
cognitive_forms = set()
soft_variants = set()
stages = set()
validated_count = 0
degraded_count = 0
judge_pass = 0
red_team_pass = 0

for f in files:
    data = json.loads(f.read_text(encoding="utf-8"))
    md = data["metadata"]
    vf = data.get("verification", {})
    tags = md.get("tags", {})
    if isinstance(tags, dict):
        metrics.add(tags.get("metric", ""))
    cognitive_forms.add(md.get("cognitive_form") or "unknown")
    soft_variants.add(md.get("soft_variant") or "unknown")
    stages.add(md.get("stage", ""))
    if md.get("validated"):
        validated_count += 1
    if md.get("degraded"):
        degraded_count += 1
    if isinstance(vf, dict):
        judge = vf.get("judge", {})
        if judge.get("correct") and judge.get("self_contained"):
            judge_pass += 1
        red_team = vf.get("red_team", {})
        if red_team.get("survives"):
            red_team_pass += 1

print("=== 泛化度评估 ===")
print(f"总文件数: {len(files)}")
print(f"度规覆盖: {sorted(metrics)} ({len(metrics)} 种)")
print(f"认知形式: {sorted(cognitive_forms)} ({len(cognitive_forms)} 种)")
print(f"软变体类型: {sorted(soft_variants)} ({len(soft_variants)} 种)")
print(f"Stage: {sorted(stages)} ({len(stages)} 种)")
print(f"validated: {validated_count}")
print(f"degraded: {degraded_count}")
print(f"judge 通过: {judge_pass}")
print(f"red_team 通过: {red_team_pass}")

all_forms = ["derivation", "numerical", "conceptual", "code", "multiple_choice", "open"]
missing = [f for f in all_forms if f not in cognitive_forms]
print(f"缺失认知形式: {missing}")

from core.common.metric_library import METRIC_LIBRARY
all_metrics = list(METRIC_LIBRARY.keys())
unused_light = [m for m in all_metrics if m not in metrics and not METRIC_LIBRARY[m].get("heavy", False)]
print(f"度规库可用(light): {len([m for m in all_metrics if not METRIC_LIBRARY[m].get('heavy', False)])} 种")
print(f"未使用(light): {unused_light}")

has_soft = any("soft" in s for s in stages)
print(f"Phase 3 (soft_rewrite): {'已执行' if has_soft else '未执行'}")