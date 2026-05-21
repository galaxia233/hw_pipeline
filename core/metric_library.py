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


def _extract_from_einsteinpy(metric_class, name: str, tags: dict, heavy: bool = False) -> dict:
    """Extract metric info from an EinsteinPy predefined class."""
    m = metric_class()
    arr = m.arr
    dim = m.dims
    syms = list(m.symbols())
    var_names = [str(s) for s in syms]

    metric_matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            val = _simplify_expr(arr[i, j])
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