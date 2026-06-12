"""Fact Sheet 预计算缓存：度规库中的度规几何量只需计算一次，存入 JSON 供后续直接读取。

用法：
  python main.py precompute       — 预计算所有非 heavy 度规的 Fact Sheet
  get_cached_fact_sheet("Schwarzschild")  — 读取缓存，未缓存则实时计算并自动存入
"""

import json
from pathlib import Path

from core.common.metric_library import METRIC_LIBRARY
from core.common.sympy_engine import compute_fact_sheet, compute_fact_sheet_heavy

CACHE_PATH = Path(__file__).parent / "fact_sheet_cache.json"


def _reset_cache_for_metric(metric_name: str):
    """清除指定度规的缓存（用于度规约定变更后重算）。"""
    cache = _load_cache()
    if metric_name in cache:
        del cache[metric_name]
        _save_cache(cache)
        print(f"  已清除 {metric_name} 的缓存，下次调用时将重新计算")


def _load_cache() -> dict:
    """从 JSON 文件加载缓存，文件不存在则返回空 dict。"""
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def _save_cache(cache: dict):
    """将缓存写入 JSON 文件。"""
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def build_cache(force: bool = False, include_heavy: bool = False):
    """遍历度规库中所有度规，预计算 Fact Sheet 并存入缓存。

    Args:
        force: True 时重新计算所有度规（覆盖已有缓存）；False 时跳过已缓存的度规。
        include_heavy: True 时也计算 heavy 度规（计算较慢，每完成一个立即写入缓存）。
    """
    cache = {} if force else _load_cache()

    to_compute = [
        (name, data) for name, data in METRIC_LIBRARY.items()
        if (include_heavy or not data.get("heavy", False)) and (force or name not in cache)
    ]

    if not to_compute:
        if cache:
            print(f"所有 {len(cache)} 个度规已缓存，无需重新计算")
        else:
            print("没有需要计算的度规")
        return cache

    heavy_count = sum(1 for _, data in to_compute if data.get("heavy", False))
    light_count = len(to_compute) - heavy_count
    print(f"需要预计算 {len(to_compute)} 个度规的 Fact Sheet ({light_count} 个常规 + {heavy_count} 个 heavy)...")

    # 先计算非 heavy 度规，再逐个计算 heavy 度规（每完成一个立即写入）
    light_items = [(name, data) for name, data in to_compute if not data.get("heavy", False)]
    heavy_items = [(name, data) for name, data in to_compute if data.get("heavy", False)]

    for i, (name, data) in enumerate(light_items, 1):
        print(f"  [{i}/{len(light_items)}] 计算 {name}...")
        try:
            fs = compute_fact_sheet(data["metric"], data["variables"], metric_name=name)
            cache[name] = fs
            print(f"  [{i}/{len(light_items)}] {name} 完成")
        except Exception as e:
            print(f"  [{i}/{len(light_items)}] {name} 失败: {e}")
            cache[name] = {"error": str(e)}

    # 每完成一个 heavy 度规就写入缓存（避免中途失败丢失进度）
    for i, (name, data) in enumerate(heavy_items, 1):
        print(f"  [heavy {i}/{len(heavy_items)}] 计算 {name}（使用快速路径，跳过 Riemann）...")
        try:
            fs = compute_fact_sheet_heavy(data["metric"], data["variables"], metric_name=name)
            cache[name] = fs
            _save_cache(cache)  # 立即写入
            print(f"  [heavy {i}/{len(heavy_items)}] {name} 完成（已写入缓存）")
        except Exception as e:
            print(f"  [heavy {i}/{len(heavy_items)}] {name} 失败: {e}")
            cache[name] = {"error": str(e)}
            _save_cache(cache)  # 即使失败也写入，避免反复重试

    _save_cache(cache)
    ok_count = sum(1 for v in cache.values() if "error" not in v)
    err_count = sum(1 for v in cache.values() if "error" in v)
    print(f"预计算完成: {ok_count} 成功, {err_count} 失败, 缓存写入 {CACHE_PATH}")
    return cache


def _migrate_old_christoffel_keys(fs: dict) -> dict:
    """将旧格式 Christoffel key (Gamma_ijk) 转换为新格式 (Gamma^i_jk)。

    SymPy engine 现在使用 Gamma^i_{jk} 格式（明确标识第一指标为上标），
    但旧缓存中存储的是 Gamma_{ijk} 格式。此函数检测旧格式并自动转换。

    Args:
        fs: Fact Sheet dict（可能包含旧格式的 christoffel key）

    Returns:
        转换后的 Fact Sheet dict（如果需要转换则标记为已迁移）
    """
    if not fs or "christoffel" not in fs:
        return fs

    christoffel = fs["christoffel"]
    if not christoffel:
        return fs

    # 检测是否有旧格式的 key（Gamma_ijk 全数字索引）
    old_keys = [k for k in christoffel if k.startswith("Gamma_") and len(k) == 9 and all(c.isdigit() for c in k[6:9])]
    if not old_keys:
        # 已经是新格式，无需转换
        return fs

    # 转换：Gamma_ijk → Gamma^i_jk
    new_christoffel = {}
    for key, val in christoffel.items():
        if key.startswith("Gamma_") and len(key) == 9 and all(c.isdigit() for c in key[6:9]):
            # Gamma_{i}{j}{k} → Gamma^{i}_{j}{k}
            i_idx, j_idx, k_idx = key[6], key[7], key[8]
            new_key = f"Gamma^{i_idx}_{j_idx}{k_idx}"
            new_christoffel[new_key] = val
        else:
            new_christoffel[key] = val

    fs["christoffel"] = new_christoffel

    # 添加 convention_note（旧缓存没有此字段）
    if "convention_note" not in fs:
        fs["convention_note"] = "Christoffel Gamma^i_{jk} 表示第二类 Christoffel 符号（第一指标为上标/逆变，后两指标为下标/协变）。符号约定 (-,+,+,+)：类时条件 g_{μν}u^μu^ν=-1"

    print(f"  [缓存迁移] 已将 {len(old_keys)} 个旧格式 Christoffel key 转换为新格式")
    return fs


def get_cached_fact_sheet(metric_name: str) -> dict | None:
    """读取指定度规的缓存 Fact Sheet。

    对于 heavy 度规：缓存有就用，缓存没有就返回 None（提示用户先运行 precompute --include-heavy），不做实时计算以避免阻塞。
    对于非 heavy 度规：缓存有就用，缓存没有则实时计算并存入。

    自动检测并迁移旧格式的 Christoffel key（Gamma_ijk → Gamma^i_jk）。

    Args:
        metric_name: 度规库名称，如 "Schwarzschild"

    Returns:
        Fact Sheet dict，或 None（度规不在库中或计算失败）
    """
    # 度规不在库中 → 无法缓存
    if metric_name not in METRIC_LIBRARY:
        return None

    data = METRIC_LIBRARY[metric_name]
    is_heavy = data.get("heavy", False)

    # 尝试读缓存
    cache = _load_cache()
    cached = cache.get(metric_name)
    if cached is not None:
        if "error" not in cached:
            # 自动迁移旧格式 Christoffel key
            cached = _migrate_old_christoffel_keys(cached)
            if cached != cache.get(metric_name):
                # 格式已更新，写回缓存
                cache[metric_name] = cached
                _save_cache(cache)
            print(f"  [缓存] 使用已缓存的 {metric_name} Fact Sheet")
            return cached
        # 缓存的是 error 记录，尝试重新计算（仅非 heavy）
        if is_heavy:
            print(f"  [缓存] {metric_name} 之前计算失败，请先运行 precompute --include-heavy 重新尝试")
            return None
        print(f"  [缓存] {metric_name} 之前计算失败，重新尝试...")

    # Heavy 度规未缓存 → 不实时计算，提示用户预计算
    if is_heavy:
        print(f"  [缓存] {metric_name} 是 heavy 度规且未缓存，请先运行 precompute --include-heavy")
        return None

    # 非 heavy 度规未缓存 → 实时计算并存入
    print(f"  [缓存] 计算 {metric_name} Fact Sheet 并存入缓存...")
    try:
        fs = compute_fact_sheet(data["metric"], data["variables"], metric_name=metric_name)
        cache[metric_name] = fs
        _save_cache(cache)
        return fs
    except Exception as e:
        cache[metric_name] = {"error": str(e)}
        _save_cache(cache)
        return None