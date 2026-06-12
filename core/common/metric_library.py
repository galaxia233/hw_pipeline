"""度规库：从 EinsteinPy 预设度规和自定义度规提取可用于 pipeline 的格式"""

import sympy
from einsteinpy.symbolic.predefined import (
    Schwarzschild, Minkowski, DeSitter, AntiDeSitter,
    AntiDeSitterStatic, Godel, ReissnerNordstorm,
    BarriolaVilekin, BertottiKasner, CMetric, Davidson,
    Ernst, JanisNewmanWinicour, Kerr, KerrNewman,
    MinkowskiCartesian, MinkowskiPolar, AlcubierreWarp,
    BesselGravitationalWave,
)

# 自定义度规：FLRW（EinsteinPy 没有，需要手动定义）
FLRW_METRIC = {
    "name": "FLRW",
    "dimension": 4,
    "variables": ["t", "r", "theta", "phi"],
    "metric": [
        ["-1", "0", "0", "0"],
        ["0", "a(t)**2/(1 - k*r**2)", "0", "0"],
        ["0", "0", "r**2 * a(t)**2", "0"],
        ["0", "0", "0", "r**2 * a(t)**2 * sin(theta)**2"],
    ],
    "tags": {
        "metric": "FLRW",
        "target_object": "Ricci scalar",
        "coordinate": "spherical coordinates",
        "scenario": "cosmology",
        "method": "tensor calculus",
    },
    "heavy": False,
}


def _simplify_expr(expr, c_val=1, G_val=1) -> sympy.Expr:
    """Simplify a metric expression, setting c=1 and G=1 (geometric units)."""
    from einsteinpy.symbolic import SymbolicConstant
    for sym in expr.free_symbols:
        if isinstance(sym, SymbolicConstant) and sym.name == "c":
            expr = expr.subs(sym, c_val)
        elif isinstance(sym, SymbolicConstant) and sym.name == "G":
            expr = expr.subs(sym, G_val)
    # Also try plain Symbol substitution as fallback
    expr = expr.subs(sympy.Symbol("c"), c_val).subs(sympy.Symbol("G"), G_val)
    return sympy.simplify(expr)


def _normalize_sign_convention_sympy(g_matrix: sympy.Matrix, dim: int) -> sympy.Matrix:
    """将度规矩阵统一为 Lorentzian (-,+,+,+,...) 符号约定（SymPy 版）。

    EinsteinPy 的某些度规（如 Schwarzschild）使用 (+,-,-,-) 约定，
    即 g_tt > 0、空间分量 < 0。这与大多数 GR 教材和 (-,+,+,+) 约定不同。
    此函数检测 (+,-,-,-) 约定并翻转所有对角元素的符号。

    使用 SymPy 的 is_positive / is_negative 属性判断符号，比字符串前缀检测更可靠。
    当 SymPy 无法确定符号时（返回 None），回退到字符串前缀检测。

    Args:
        g_matrix: N×N SymPy Matrix
        dim: 维度

    Returns:
        转换后的 SymPy Matrix（原地修改并返回）
    """
    # 检测 (+,-,-,-) 约定：g_tt 正值，空间分量负值
    # SymPy 的 is_positive/is_negative 可能返回 None（无法确定），
    # 此时回退到字符串前缀检测
    g00_val = g_matrix[0, 0]
    g00_str = str(g00_val).strip()

    g00_positive = g00_val.is_positive
    if g00_positive is None:
        # SymPy 无法确定 → 回退到字符串检测
        g00_positive = not (g00_str.startswith("-") or g00_str.startswith("-1"))

    spatial_negative = True
    for i in range(1, dim):
        val = g_matrix[i, i]
        val_str = str(val).strip()
        is_neg = val.is_negative
        if is_neg is None:
            # SymPy 无法确定 → 回退到字符串检测
            is_neg = (val_str.startswith("-") or val_str.startswith("-1") or val_str.startswith("-r"))
        if is_neg is not True:
            spatial_negative = False
            break

    if g00_positive is True and spatial_negative:
        # (+,-,-,-) 约定 → 翻转为 (-,+,+,+)
        # 乘 -1：对角元素翻转符号
        for i in range(dim):
            g_matrix[i, i] = -g_matrix[i, i]
        print(f"  检测到 (+,-,-,-) 约定，已自动转换为 (-,+,+,+)")
        return g_matrix

    # 已经是标准 (-,+,+,+) 约定或无法判断，保持不变
    return g_matrix


def _normalize_sign_convention(metric_matrix: list, dim: int) -> list:
    """将度规矩阵字符串列表统一为 (-,+,+,+) 符号约定（字符串版，仅作兼容保留）。

    优先使用 _normalize_sign_convention_sympy()（更可靠）。
    此函数仅在无法使用 SymPy 时作为 fallback。

    Args:
        metric_matrix: N×N 列表，SymPy 表达式字符串
        dim: 维度

    Returns:
        转换后的 N×N 列表
    """
    # 使用 SymPy 解析判断
    parsed_diag = []
    for i in range(dim):
        try:
            expr = sympy.sympify(str(metric_matrix[i][i]).strip(),
                                  locals={"M": sympy.Symbol("M"), "r_s": sympy.Symbol("r_s"),
                                          "alpha": sympy.Symbol("alpha"), "a": sympy.Symbol("a"),
                                          "k": sympy.Symbol("k"), "Q": sympy.Symbol("Q"),
                                          "gam": sympy.Symbol("gam"), "eps_0": sympy.Symbol("eps_0")})
            parsed_diag.append(expr)
        except Exception:
            # 解析失败 → fallback 字符串检测
            parsed_diag.append(None)

    # 判断符号
    g00_positive = False
    spatial_negative = True

    if parsed_diag[0] is not None:
        g00_positive = parsed_diag[0].is_positive is True
    else:
        # fallback: 字符串检测
        g00_str = str(metric_matrix[0][0]).strip()
        g00_positive = not (g00_str.startswith("-") or g00_str.startswith("-1"))

    for i in range(1, dim):
        if parsed_diag[i] is not None:
            if parsed_diag[i].is_negative is not True:
                spatial_negative = False
                break
        else:
            # fallback: 字符串检测
            diag_str = str(metric_matrix[i][i]).strip()
            if not (diag_str.startswith("-") or diag_str.startswith("-1") or diag_str.startswith("-r")):
                spatial_negative = False
                break

    if g00_positive and spatial_negative:
        result = [row[:] for row in metric_matrix]
        for i in range(dim):
            old = str(result[i][i]).strip()
            if old.startswith("-"):
                result[i][i] = old[1:].strip()
            elif old == "0":
                result[i][i] = "0"
            else:
                result[i][i] = f"-{old}"
        print(f"  检测到 (+,-,-,-) 约定，已自动转换为 (-,+,+,+) (字符串版)")
        return result

    return metric_matrix


def _extract_from_einsteinpy(metric_class, name: str, tags: dict, heavy: bool = False) -> dict:
    """Extract metric info from an EinsteinPy predefined class.

    自动将 (+,-,-,-) 约定的度规统一为 (-,+,+,+) 约定。
    使用 SymPy 的 is_positive/is_negative 属性判断符号约定，比字符串前缀检测更可靠。
    """
    m = metric_class()
    arr = m.arr
    dim = m.dims
    syms = list(m.symbols())
    var_names = [str(s) for s in syms]

    # 先构建 SymPy Matrix 做符号约定检测（比字符串检测更可靠）
    g_matrix = sympy.Matrix.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            val = _simplify_expr(arr[i, j])
            g_matrix[i, j] = val

    # 统一符号约定为 (-,+,+,+)（SymPy 版）
    g_matrix = _normalize_sign_convention_sympy(g_matrix, dim)

    # 从 SymPy Matrix 转为字符串矩阵
    metric_matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            val = g_matrix[i, j]
            row.append(str(val) if val != 0 else "0")
        metric_matrix.append(row)

    return {
        "name": name,
        "dimension": dim,
        "variables": var_names,
        "metric": metric_matrix,
        "tags": tags,
        "heavy": heavy,
    }


# Build the library
METRIC_LIBRARY = {}

# EinsteinPy predefined metrics (geometric units c=1, G=1)
_einsteinpy_metrics = {
    "Schwarzschild": (Schwarzschild, {
        "metric": "Schwarzschild", "target_object": "Christoffel symbols",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, False),
    "Minkowski": (Minkowski, {
        "metric": "Minkowski", "target_object": "Riemann tensor",
        "coordinate": "Cartesian coordinates", "scenario": "vacuum spacetime",
        "method": "tensor calculus",
    }, False),
    "DeSitter": (DeSitter, {
        "metric": "de Sitter", "target_object": "Ricci scalar",
        "coordinate": "Cartesian coordinates", "scenario": "cosmology",
        "method": "tensor calculus",
    }, False),
    "AntiDeSitter": (AntiDeSitter, {
        "metric": "anti-de Sitter", "target_object": "Ricci scalar",
        "coordinate": "spherical coordinates", "scenario": "cosmology",
        "method": "tensor calculus",
    }, False),
    "AntiDeSitterStatic": (AntiDeSitterStatic, {
        "metric": "anti-de Sitter (static)", "target_object": "Ricci scalar",
        "coordinate": "hyperbolic coordinates", "scenario": "cosmology",
        "method": "tensor calculus",
    }, False),
    "Godel": (Godel, {
        "metric": "Gödel", "target_object": "Ricci tensor",
        "coordinate": "Cartesian coordinates", "scenario": "cosmology",
        "method": "tensor calculus",
    }, False),
    "ReissnerNordstrom": (ReissnerNordstorm, {
        "metric": "Reissner-Nordström", "target_object": "Christoffel symbols",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, True),
    "BarriolaVilekin": (BarriolaVilekin, {
        "metric": "Barriola-Vilenkin", "target_object": "Ricci tensor",
        "coordinate": "spherical coordinates", "scenario": "cosmic string",
        "method": "tensor calculus",
    }, False),
    "BertottiKasner": (BertottiKasner, {
        "metric": "Bertotti-Kasner", "target_object": "Ricci scalar",
        "coordinate": "spherical coordinates", "scenario": "electromagnetic spacetime",
        "method": "tensor calculus",
    }, False),
    "CMetric": (CMetric, {
        "metric": "C-metric", "target_object": "Christoffel symbols",
        "coordinate": "mixed coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, False),
    "Davidson": (Davidson, {
        "metric": "Davidson", "target_object": "Ricci tensor",
        "coordinate": "cylindrical coordinates", "scenario": "cosmology",
        "method": "tensor calculus",
    }, False),
    "JanisNewmanWinicour": (JanisNewmanWinicour, {
        "metric": "Janis-Newman-Winicour", "target_object": "Ricci scalar",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, False),
    "MinkowskiCartesian": (MinkowskiCartesian, {
        "metric": "Minkowski", "target_object": "Riemann tensor",
        "coordinate": "Cartesian coordinates", "scenario": "vacuum spacetime",
        "method": "tensor calculus",
    }, False),
    "MinkowskiPolar": (MinkowskiPolar, {
        "metric": "Minkowski", "target_object": "Riemann tensor",
        "coordinate": "spherical coordinates", "scenario": "vacuum spacetime",
        "method": "tensor calculus",
    }, False),
    # Heavy metrics: Fact Sheet computation is slow (>30s)
    "Kerr": (Kerr, {
        "metric": "Kerr", "target_object": "Christoffel symbols",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, True),
    "Ernst": (Ernst, {
        "metric": "Ernst", "target_object": "Einstein tensor",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, True),
    "KerrNewman": (KerrNewman, {
        "metric": "Kerr-Newman", "target_object": "Einstein tensor",
        "coordinate": "spherical coordinates", "scenario": "black hole",
        "method": "tensor calculus",
    }, True),
    "AlcubierreWarp": (AlcubierreWarp, {
        "metric": "Alcubierre warp", "target_object": "Christoffel symbols",
        "coordinate": "Cartesian coordinates", "scenario": "warp drive",
        "method": "tensor calculus",
    }, True),
    "BesselGravitationalWave": (BesselGravitationalWave, {
        "metric": "Bessel gravitational wave", "target_object": "Ricci tensor",
        "coordinate": "cylindrical coordinates", "scenario": "gravitational wave",
        "method": "tensor calculus",
    }, True),
}

for name, (cls, tags, heavy) in _einsteinpy_metrics.items():
    METRIC_LIBRARY[name] = _extract_from_einsteinpy(cls, name, tags, heavy)

# Add custom metrics
METRIC_LIBRARY["FLRW"] = FLRW_METRIC


def get_metric_names() -> list:
    """Return all available metric names."""
    return list(METRIC_LIBRARY.keys())


def get_metric(name: str) -> dict:
    """Get a metric dict by name."""
    return METRIC_LIBRARY[name]


def get_metrics_for_substitution(exclude: str = None, skip_heavy: bool = True) -> list:
    """Get a list of metric dicts for substitution, optionally excluding one.

    Args:
        exclude: metric name to exclude (typically the seed's metric)
        skip_heavy: if True, skip metrics marked as heavy (slow Fact Sheet)
    """
    result = []
    for name, data in METRIC_LIBRARY.items():
        if name != exclude and (not skip_heavy or not data.get("heavy", False)):
            result.append(data)
    return result