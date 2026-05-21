"""Example problem: Schwarzschild metric Christoffel symbols"""

from schema import Problem, Metadata, PhysicalData, Origin

example = Problem(
    metadata=Metadata(
        id="example",
        type="calculate",
        tags={"metric": "Schwarzschild", "target_object": "Christoffel symbols", "coordinate": "spherical coordinates"},
        tools_used=[],
        validated=False,
        source="generated",
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
        hint=["利用 $\\Gamma_{ij}^{k} = \\frac{1}{2} g^{kl} (\\partial_i g_{lj} + \\partial_j g_{li} - \\partial_l g_{ij})$",
              "注意 $g_{tt}$ 和 $g_{rr}$ 只依赖于 $r$"],
    ),
)