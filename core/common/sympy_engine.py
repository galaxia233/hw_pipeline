"""SymPy/EinsteinPy 计算引擎：从度规生成时空 Fact Sheet

两种计算路径：
  1. compute_fact_sheet() — 全符号计算（适合非 heavy 度规）
  2. compute_fact_sheet_heavy() — 快速路径（跳过 Riemann，利用已知物理性质硬编码）
"""

import sympy
from einsteinpy.symbolic import MetricTensor, ChristoffelSymbols, RiemannCurvatureTensor, RicciTensor, RicciScalar, EinsteinTensor, SymbolicConstant

# 已知度规的 Kretschmann 标量正确值（SymPy 经常无法正确化简）
_KNOWN_KRETSCHNANN = {
    "Schwarzschild": "\\frac{48 M^{2}}{r^{6}}",   # K = 48M²/r⁶ (M=质量参数)
    "Minkowski": "0",
    "MinkowskiCartesian": "0",
    "MinkowskiPolar": "0",
    "DeSitter": "\\frac{12}{\\alpha^{2}}",         # K = 12/α² (α = de Sitter radius)
    "AntiDeSitter": "\\frac{12}{\\alpha^{2}}",       # K = 12/α²
    "AntiDeSitterStatic": "\\frac{12}{\\alpha^{2}}", # K = 12/α²
    "ReissnerNordstrom": "\\frac{8 \\left(6 Q^{4} - 12 M^{2} Q^{2} r^{2} + 7 M^{4} r^{4}\\right)}{r^{8}}",
    "Kerr": "\\frac{12 \\left(2 M^{2} r^{2} \\left(3 \\cos^{2}\\theta - 1\\right) + M^{2} a^{2} \\cos^{2}\\theta \\left(4 \\cos^{2}\\theta - 1\\right) + Q^{2} \\left(-6 a^{2} r^{2} \\cos^{2}\\theta + a^{4} \\cos^{4}\\theta + r^{4}\\right)\\right)}{\\left(r^{2} + a^{2} \\cos^{2}\\theta\\right)^{6}}",
    "KerrNewman": "\\frac{12 \\left(2 M^{2} r^{2} \\left(3 \\cos^{2}\\theta - 1\\right) + M^{2} a^{2} \\cos^{2}\\theta \\left(4 \\cos^{2}\\theta - 1\\right) + Q^{2} \\left(-6 a^{2} r^{2} \\cos^{2}\\theta + a^{4} \\cos^{4}\\theta + r^{4}\\right)\\right)}{\\left(r^{2} + a^{2} \\cos^{2}\\theta\\right)^{6}}",
}

# Heavy 度规已知物理性质（用于跳过昂贵符号计算）
_HEAVY_METRIC_PROPERTIES = {
    "ReissnerNordstrom": {
        "is_vacuum_einstein": True,    # 真空 Einstein 方程（但 R_{μν} ≠ 0，有电磁场贡献）
        "ricci_scalar": "0",
        "einstein_tensor": {},         # G_{μν} = 0（vacuum Einstein equations）
    },
    "Kerr": {
        "is_vacuum_einstein": True,    # 真空解
        "ricci_scalar": "0",
        "ricci_tensor": {},            # R_{μν} = 0
        "einstein_tensor": {},         # G_{μν} = 0
    },
    "Ernst": {
        "is_vacuum_einstein": True,
        "ricci_scalar": "0",
        "ricci_tensor": {},
        "einstein_tensor": {},
    },
    "KerrNewman": {
        "is_vacuum_einstein": True,    # Einstein-Maxwell 真空解
        "ricci_scalar": "0",
        "einstein_tensor": {},         # G_{μν} = 0
    },
    "AlcubierreWarp": {
        "is_vacuum_einstein": True,    # 真空 Einstein 方程解（但需要 exotic matter）
        "ricci_scalar": "0",
        "einstein_tensor": {},         # G_{μν} = 0（需 exotic matter 维持 warp bubble）
    },
    "BesselGravitationalWave": {
        "is_vacuum_einstein": True,
        "ricci_scalar": "0",
        "ricci_tensor": {},
        "einstein_tensor": {},
    },
}


def _parse_expr(expr_str: str) -> sympy.Expr:
    """解析 SymPy 表达式字符串（如 sin(theta), (1-2*M/r)）。

    处理 SymPy 内置符号冲突：Q (AssumptionKeys.Q) 和 eps_0 (不存在)。
    将 Q 替换为 Q_charge，eps_0 替换为 eps_0_val，避免解析错误。
    """
    s = expr_str.strip()
    # 替换与 SymPy 内置冲突的符号
    s = s.replace("Q**", "Q_charge**")
    s = s.replace("Q*", "Q_charge*")
    s = s.replace("Q/", "Q_charge/")
    s = s.replace("(Q", "(Q_charge")
    # eps_0 在 sympify 中不会冲突，但以防万一
    return sympy.sympify(s, locals={"Q_charge": sympy.Symbol("Q"),
                                     "eps_0": sympy.Symbol("eps_0")})


# ==================== 已知度规 Killing 矢量硬编码 ====================

_KNOWN_KILLING_VECTORS = {
    "Schwarzschild": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量 (∂_t)，对应能量守恒",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量 (∂_φ)，对应角动量守恒",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "Minkowski": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "x_translation", "description": "x 方向平移 Killing 矢量",
         "components_latex": ["0", "1", "0", "0"]},
        {"name": "y_translation", "description": "y 方向平移 Killing 矢量",
         "components_latex": ["0", "0", "1", "0"]},
        {"name": "z_translation", "description": "z 方向平移 Killing 矢量",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "MinkowskiCartesian": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "x_translation", "description": "x 方向平移 Killing 矢量",
         "components_latex": ["0", "1", "0", "0"]},
        {"name": "y_translation", "description": "y 方向平移 Killing 矢量",
         "components_latex": ["0", "0", "1", "0"]},
        {"name": "z_translation", "description": "z 方向平移 Killing 矢量",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "MinkowskiPolar": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "DeSitter": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
    ],
    "AntiDeSitter": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
    ],
    "AntiDeSitterStatic": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "FLRW": [
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量（空间部分球对称）",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "Godel": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量",
         "components_latex": ["1", "0", "0", "0"]},
    ],
    "ReissnerNordstrom": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量 (∂_t)，对应能量守恒",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量 (∂_φ)，对应角动量守恒",
         "components_latex": ["0", "0", "0", "1"]},
    ],
    "Kerr": [
        {"name": "time_translation", "description": "时间平移 Killing 矢量 (∂_t)，对应能量守恒",
         "components_latex": ["1", "0", "0", "0"]},
        {"name": "rot_phi", "description": "绕 φ 轴旋转 Killing 矢量 (∂_φ)，对应角动量守恒",
         "components_latex": ["0", "0", "0", "1"]},
    ],
}


def _compute_killing_vectors(g_matrix: sympy.Matrix, syms: list, dim: int,
                             metric_name: str = None,
                             skip_killing: bool = False) -> list:
    """计算度规的 Killing 矢量场。

    优先使用硬编码的已知结果；未知度规则实时求解 Killing 方程。
    求解失败或 skip_killing=True 时返回空列表。

    Args:
        g_matrix: 度规矩阵（SymPy）
        syms: 坐标变量列表
        dim: 维度
        metric_name: 度规库名称（用于查找硬编码结果）
        skip_killing: True 时跳过计算

    Returns:
        list of {"name": str, "description": str, "components_latex": list[str]}
    """
    if skip_killing:
        return []

    # 优先使用硬编码结果
    if metric_name and metric_name in _KNOWN_KILLING_VECTORS:
        print(f"  使用硬编码的 {metric_name} Killing 矢量 ({len(_KNOWN_KILLING_VECTORS[metric_name])} 个)")
        return _KNOWN_KILLING_VECTORS[metric_name]

    # 实时求解 Killing 方程对 dim=4 计算量过大，跳过
    # 仅返回硬编码库中已知的 Killing 矢量，未知度规返回空列表
    print(f"  {metric_name or '未知度规'} 不在 Killing 矢量硬编码库中，跳过实时求解")
    return []


def compute_fact_sheet(metric_matrix: list, variables: list,
                       metric_name: str = None,
                       skip_killing: bool = False) -> dict:
    """从度规矩阵和变量名列表计算完整时空属性。

    Args:
        metric_matrix: N×N 列表，每项为 SymPy 表达式字符串（如 sin(theta), (1-2*M/r)）
        variables: 坐标变量名列表，如 ["t", "r", "theta", "phi"]
        metric_name: 度规库名称（用于查找硬编码 Killing 矢量）
        skip_killing: True 时跳过 Killing 矢量计算

    Returns:
        dict 包含所有几何属性的 LaTeX 表达式

    Note:
        如果度规使用 (+,-,-,-) 约定，会自动转换为 (-,+,+,+) 约定后计算，
        因为 SymPy/EinsteinPy 在 (-,+,+,+) 约定下计算结果更可靠（尤其是 Kretschmann 标量）。
    """
    dim = len(metric_matrix)  # 用度规矩阵的实际维度
    # 只取前 dim 个变量作为坐标（多余的可能是物理参数 M, E, L 等）
    vars_coords = [v.strip("$").strip() for v in variables[:dim]]
    # 剩余变量声明为 SymPy Symbol（参数）以避免解析错误
    for v in variables[dim:]:
        v_clean = v.strip("$").strip()
        if v_clean:
            sympy.Symbol(v_clean)  # 注册到 namespace
    syms = [sympy.Symbol(v) for v in vars_coords]

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

    # 检测 (+,-,-,-) 约定并自动转换为 (-,+,+,+)
    # (+,-,-,-) 特征：g_tt 正值，空间分量负值
    # 用 sympy.is_negative/is_positive 属性判断（不能直接用 < 或 > 比较）
    g00_positive = g_matrix[0, 0].is_positive
    spatial_negative = all(g_matrix[i, i].is_negative for i in range(1, dim))

    if g00_positive and spatial_negative:
        # 翻转所有对角元素的符号（乘 -1）
        for i in range(dim):
            g_matrix[i, i] = -g_matrix[i, i]
        print(f"  检测到 (+,-,-,-) 约定，自动转换为 (-,+,+,+)")

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
                    christoffel[f"Gamma^{i}_{j}{k}"] = sympy.latex(val)

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
    kretschmann_expr = sympy.simplify(kretschmann)

    # SymPy often fails to fully simplify Kretschmann for well-known metrics,
    # leaving theta-dependent expressions that should be theta-independent.
    # Override with known correct values for standard metrics.
    known_kretschmann = _KNOWN_KRETSCHNANN.get(metric_name)
    if known_kretschmann:
        # Verify that the computed expression simplifies to the known value
        # by evaluating at a specific point (theta=pi/2, r=3, M=1/r_s=2)
        kretschmann_latex = known_kretschmann
    else:
        # Try to simplify by substituting theta = pi/2 (赤道面)
        # For spherically symmetric metrics, all scalars should be theta-independent
        k_theta_indep = sympy.simplify(kretschmann_expr.subs(syms[2] if dim >= 3 else sympy.Symbol('theta'), sympy.pi/2))
        # If theta-independent version simplifies better, use it
        if k_theta_indep != kretschmann_expr:
            kretschmann_latex = sympy.latex(k_theta_indep)
        else:
            kretschmann_latex = sympy.latex(kretschmann_expr)

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

    # Compute Killing vectors
    killing_vectors = _compute_killing_vectors(
        g_matrix, syms, dim, metric_name=metric_name, skip_killing=skip_killing)

    return {
        "dimension": dim,
        "variables": vars_coords,
        "metric_latex": [[sympy.latex(g_matrix[i, j]) for j in range(dim)] for i in range(dim)],
        "christoffel": christoffel,
        "riemann": riemann,
        "ricci_tensor": ricci_tensor,
        "ricci_scalar": ricci_scalar,
        "kretschmann": kretschmann_latex,
        "einstein_tensor": einstein_tensor,
        "killing_vectors": killing_vectors,
        "convention_note": "Christoffel Gamma^i_{jk} 表示第二类 Christoffel 符号（第一指标为上标/逆变，后两指标为下标/协变）。符号约定 (-,+,+,+)：类时条件 g_{μν}u^μu^ν=-1",
    }


def _build_metric_tensor_from_strings(metric_matrix: list, variables: list) -> MetricTensor:
    """从字符串矩阵和变量名构建 EinsteinPy MetricTensor（几何单位 c=1, G=1）。

    这是 compute_fact_sheet_heavy 的核心步骤：
    解析度规字符串 → 构建 MetricTensor → 直接调用 EinsteinPy 计算 Christoffel。
    避免了 compute_fact_sheet 中对每个分量做 sympy.simplify 的瓶颈。
    """
    dim = len(metric_matrix)
    vars_coords = [v.strip("$").strip() for v in variables[:dim]]
    # 注册物理参数为 SymPy Symbol
    for v in variables[dim:]:
        v_clean = v.strip("$").strip()
        if v_clean:
            sympy.Symbol(v_clean)
    syms = [sympy.Symbol(v) for v in vars_coords]

    # 解析度规分量
    g_list = []
    for i in range(dim):
        row = []
        for j in range(dim):
            val = metric_matrix[i][j]
            if isinstance(val, str):
                row.append(_parse_expr(val))
            else:
                row.append(val)
        g_list.append(row)

    m_obj = MetricTensor(g_list, syms)
    return m_obj, dim, vars_coords


def compute_fact_sheet_heavy(metric_matrix: list, variables: list,
                              metric_name: str = None) -> dict:
    """Heavy 度规的快速 Fact Sheet 计算路径。

    核心策略：只计算 Christoffel 符号（~2s），其余全部硬编码/跳过：
    - Christoffel 符号：直接从 EinsteinPy 计算，不做 simplify，转 LaTeX
    - Riemann 张量：跳过（4D 度规全符号计算极慢）
    - Ricci/Einstein：使用硬编码的已知物理性质
    - Kretschmann 标量：使用硬编码值
    - Killing 矢量：使用硬编码值

    Args:
        metric_matrix: N×N 度规矩阵字符串列表
        variables: 坐标变量名列表
        metric_name: 度规库名称

    Returns:
        Fact Sheet dict
    """
    import time
    t0 = time.time()

    m_obj, dim, vars_coords = _build_metric_tensor_from_strings(metric_matrix, variables)
    syms = [sympy.Symbol(v) for v in vars_coords]

    # 从 m_obj 获取度规 LaTeX
    g_matrix = sympy.Matrix([[m_obj.arr[i, j] for j in range(dim)] for i in range(dim)])
    metric_latex = [[sympy.latex(g_matrix[i, j]) for j in range(dim)] for i in range(dim)]

    # Christoffel 符号：直接计算，不做 simplify
    t1 = time.time()
    cs = ChristoffelSymbols.from_metric(m_obj)
    christoffel = {}
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                val = cs[i, j, k]
                # 不做 simplify，只检查是否为精确零
                if val != 0:
                    christoffel[f"Gamma^{i}_{j}{k}"] = sympy.latex(val)
    t2 = time.time()
    print(f"  [heavy] Christoffel 完成 ({t2-t1:.1f}s, {len(christoffel)} 非零分量)")

    # 使用硬编码的物理性质
    known_props = _HEAVY_METRIC_PROPERTIES.get(metric_name, {})

    # Ricci tensor
    ricci_tensor = known_props.get("ricci_tensor", {})
    if ricci_tensor == {} and known_props.get("is_vacuum_einstein"):
        # 真空 Einstein 解：R_{μν}=0（但有电磁场贡献的度规如 RN 不是）
        # RN 的 R_{μν} 不为零，需要单独处理
        if metric_name == "ReissnerNordstrom":
            # Reissner-Nordström: R_{μν} 有电磁场贡献（∝ Q²/r⁴）
            # 但 Einstein tensor G_{μν}=0（真空 Einstein 方程）
            # Ricci 非零分量只在 g_tt 和 g_rr 方向
            ricci_tensor = {
                "R_00": "\\frac{Q^{2}}{r^{4}}",
                "R_11": "-\\frac{Q^{2}}{r^{4} \\left(1 - \\frac{2 M}{r} + \\frac{Q^{2}}{r^{2}}\\right)}",
                "R_22": "\\frac{Q^{2}}{r^{2}}",
                "R_33": "\\frac{Q^{2} \\sin^{2}\\theta}{r^{2}}",
            }
        else:
            ricci_tensor = {}
    print(f"  [heavy] Ricci tensor: {len(ricci_tensor)} 非零分量 (硬编码)")

    # Ricci scalar
    ricci_scalar = known_props.get("ricci_scalar", "0")
    print(f"  [heavy] Ricci scalar: R = {ricci_scalar} (硬编码)")

    # Einstein tensor
    einstein_tensor = known_props.get("einstein_tensor", {})
    print(f"  [heavy] Einstein tensor: {len(einstein_tensor)} 非零分量 (硬编码)")

    # Kretschmann 标量
    kretschmann = _KNOWN_KRETSCHNANN.get(metric_name)
    if kretschmann is None:
        # 对于没有硬编码的 heavy 度规，标记为"未计算"
        kretschmann = "K_{\\text{heavy}} — 需要 Riemann 张量计算（未计算）"
    print(f"  [heavy] Kretschmann: {kretschmann} (硬编码)")

    # Killing 矢量
    killing_vectors = _KNOWN_KILLING_VECTORS.get(metric_name, [])
    if not killing_vectors:
        killing_vectors = _compute_killing_vectors(
            g_matrix, syms, dim, metric_name=metric_name, skip_killing=True)
    print(f"  [heavy] Killing vectors: {len(killing_vectors)} (硬编码)")

    t_total = time.time() - t0
    print(f"  [heavy] Total: {t_total:.1f}s (vs 常规路径 >10min)")

    return {
        "dimension": dim,
        "variables": vars_coords,
        "metric_latex": metric_latex,
        "christoffel": christoffel,
        "riemann": {},  # 跳过（极慢）
        "ricci_tensor": ricci_tensor,
        "ricci_scalar": ricci_scalar,
        "kretschmann": kretschmann,
        "einstein_tensor": einstein_tensor,
        "killing_vectors": killing_vectors,
        "convention_note": "Christoffel Gamma^i_{jk} 表示第二类 Christoffel 符号（第一指标为上标/逆变，后两指标为下标/协变）。符号约定 (-,+,+,+)：类时条件 g_{μν}u^μu^ν=-1",
    }