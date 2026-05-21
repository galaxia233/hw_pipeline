"""SymPy/EinsteinPy 计算引擎：从度规生成时空 Fact Sheet"""

import sympy
from einsteinpy.symbolic import MetricTensor, ChristoffelSymbols, RiemannCurvatureTensor, RicciTensor, RicciScalar, EinsteinTensor


def _parse_expr(expr_str: str) -> sympy.Expr:
    """解析 SymPy 表达式字符串（如 sin(theta), (1-2*M/r)）。"""
    s = expr_str.strip()
    return sympy.sympify(s)


def compute_fact_sheet(metric_matrix: list, variables: list) -> dict:
    """从度规矩阵和变量名列表计算完整时空属性。

    Args:
        metric_matrix: N×N 列表，每项为 SymPy 表达式字符串（如 sin(theta), (1-2*M/r)）
        variables: 坐标变量名列表，如 ["t", "r", "theta", "phi"]

    Returns:
        dict 包含所有几何属性的 LaTeX 表达式
    """
    dim = len(variables)
    syms = [sympy.Symbol(v) for v in variables]

    # Parse metric components
    g_matrix = sympy.Matrix.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            val = metric_matrix[i][j]
            if isinstance(val, str):
                expr = _parse_expr(val)
            else:
                expr = val
            g_matrix[i, j] = expr

    # Build EinsteinPy MetricTensor
    # EinsteinPy expects a list of lists of sympy expressions
    g_list = [[g_matrix[i, j] for j in range(dim)] for i in range(dim)]
    m_obj = MetricTensor(g_list, syms)

    # Compute Christoffel symbols
    cs = ChristoffelSymbols.from_metric(m_obj)
    christoffel = {}
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                val = sympy.simplify(cs[i, j, k])
                if val != 0:
                    christoffel[f"Gamma_{i}{j}{k}"] = sympy.latex(val)

    # Compute Riemann tensor
    rm = RiemannCurvatureTensor.from_metric(m_obj)
    riemann = {}
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    val = sympy.simplify(rm[i, j, k, l])
                    if val != 0:
                        riemann[f"R_{i}{j}{k}{l}"] = sympy.latex(val)

    # Compute Ricci tensor
    rt = RicciTensor.from_metric(m_obj)
    ricci_tensor = {}
    for i in range(dim):
        for j in range(dim):
            val = sympy.simplify(rt[i, j])
            if val != 0:
                ricci_tensor[f"R_{i}{j}"] = sympy.latex(val)

    # Compute Ricci scalar
    rs = RicciScalar.from_metric(m_obj)
    ricci_scalar = sympy.latex(sympy.simplify(rs.expr))

    # Compute Kretschmann scalar: K = R_{ijkl} R^{ijkl}
    # Need inverse metric for raising indices
    g_inv = g_matrix.inv()
    kretschmann = 0
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                for l in range(dim):
                    r_lower = rm[i, j, k, l]
                    r_upper = 0
                    for a in range(dim):
                        for b in range(dim):
                            r_upper += g_inv[i, a] * g_inv[j, b] * rm[a, b, k, l]
                    kretschmann += r_lower * r_upper
    kretschmann = sympy.latex(sympy.simplify(kretschmann))

    # Compute Einstein tensor G_{μν} = R_{μν} - (1/2) g_{μν} R
    einstein_tensor = {}
    for i in range(dim):
        for j in range(dim):
            g_val = g_matrix[i, j]
            r_val = rt[i, j]
            g_ij = sympy.simplify(r_val - sympy.Rational(1, 2) * g_val * rs.expr)
            g_ij = sympy.simplify(g_ij)
            if g_ij != 0:
                einstein_tensor[f"G_{i}{j}"] = sympy.latex(g_ij)

    return {
        "dimension": dim,
        "variables": variables,
        "metric_latex": [[sympy.latex(g_matrix[i, j]) for j in range(dim)] for i in range(dim)],
        "christoffel": christoffel,
        "riemann": riemann,
        "ricci_tensor": ricci_tensor,
        "ricci_scalar": ricci_scalar,
        "kretschmann": kretschmann,
        "einstein_tensor": einstein_tensor,
    }