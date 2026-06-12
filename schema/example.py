"""Example problem: Schwarzschild metric Christoffel symbols — 新 schema 格式"""

from schema import (
    Problem, Metadata, PhysicalData, Origin,
    StructuralCheck, MetricCheck, JudgeCheck, Verification,
    generate_id,
)

# 生成 hash ID
example_id = generate_id("example", "Schwarzschild", "Christoffel_symbols")

example = Problem(
    metadata=Metadata(
        id=example_id,
        type="prove",
        tags={
            "metric": "Schwarzschild",
            "target_object": "Christoffel symbols",
            "coordinate": "spherical coordinates",
            "scenario": "black hole",
            "method": "tensor calculus",
        },
        tools_used=["llm_reasoning", "sympy_verify"],
        validated=True,
        source="example",
        # 新增字段
        source_id="example",
        source_type="problem_set",
        stage="seed",
        lineage=["example"],
        topic="Schwarzschild Christoffel symbols",
        concepts=["Christoffel symbols", "Schwarzschild metric", "geodesic equation"],
        cognitive_form="derivation",
        physics_env="Schwarzschild",
        soft_variant="",
        training_value=0.7,
    ),
    physical_data=PhysicalData(
        dimension=4,
        variables=["$t$", "$r$", "$\\theta$", "$\\phi$"],
        metric=[
            ["$-(1 - \\frac{2M}{r})$", "$0$",            "$0$",            "$0$"            ],
            ["$0$",           "$(1 - \\frac{2M}{r})^{-1}$", "$0$",            "$0$"            ],
            ["$0$",           "$0$",             "$r^{2}$",           "$0$"            ],
            ["$0$",           "$0$",             "$0$",            "$r^{2} \\sin^{2}\\theta$"     ],
        ],
        target=["$\\Gamma_{01}^{1}$", "$\\Gamma_{22}^{1}$", "$\\Gamma_{33}^{1}$"],
    ),
    origin=Origin(
        question="计算 Schwarzschild 度规的所有克里斯托弗符号 $\\Gamma_{ij}^{k}$。",
        answer=None,
        solution=None,
    ),
    verification=Verification(
        structural=StructuralCheck(ok=True),
        metric_check=MetricCheck(
            checker="sympy_verify.schwarzschild_christoffel",
            status="ok",
            details={"vacuum": True, "ricci_scalar": "0"},
        ),
        judge=JudgeCheck(
            correct=True,
            self_contained=True,
            training_value=0.7,
            issue="",
        ),
    ),
)

# 展示转换为 dataset.jsonl 格式
if __name__ == "__main__":
    import json
    from schema import problem_to_dataset_record

    print("=== 内部 Problem 格式 (asdict) ===")
    print(json.dumps({
        "metadata": example.metadata,
        "physical_data": example.physical_data,
        "origin": example.origin,
        "verification": example.verification,
    }, ensure_ascii=False, indent=2, default=str))

    print("\n=== dataset.jsonl 格式 ===")
    record = problem_to_dataset_record(example)
    print(json.dumps(record, ensure_ascii=False, indent=2))

    print(f"\nID: {example_id}")
    print(f"cognitive_form: {example.metadata.cognitive_form}")
    print(f"physics_env: {example.metadata.physics_env}")