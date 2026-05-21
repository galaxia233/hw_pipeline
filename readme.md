# hw_pipeline：广义相对论题目自动泛化流水线

从一道种子题目出发，自动生成多道相关但不同的物理题目，并通过 SymPy/EinsteinPy 计算保证答案中几何量的正确性。

## 环境依赖

- Python 3.10+
- [EinsteinPy](https://einsteinpy.org/) — 符号计算 GR 时空几何量
- [SymPy](https://sympy.org/) — 符号数学引擎
- [python-dotenv](https://github.com/theskumar/python-dotenv) — 加载 `.env` 环境变量
- [requests](https://docs.python-requests.org/) — HTTP API 调用
- [pillow](https://python-pillow.org/) — 图片处理（PDF/Word 转图片）
- [pdf2image](https://github.com/Belval/pdf2image) — PDF 转图片（需要系统安装 [Poppler](https://poppler.freedesktop.org/)）
- [python-docx](https://github.com/python-openxml/python-docx) — Word 文件转图片
- DashScope API Key（通过 `.env` 配置，参见 `.env.example`）

安装：
```bash
pip install einsteinpy sympy python-dotenv requests pillow pdf2image python-docx
```

Windows 用户还需安装 Poppler（PDF 转图片所需），可从 [poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases) 下载并添加到 PATH。

## 泛化思路

流水线的核心是**从种子题目向不同方向延伸**，而非随意生成新题。具体策略：

### Phase 1：同度规延伸

保持种子题的度规不变，LLM 自行选择一个有意义的泛化方向，从种子题的设问出发延伸出一道后续题目。泛化方向由 LLM 根据种子题的物理场景和度规的非平凡几何特性自行决定，不做预设限制。

每道延伸题都是**独立完整的题目**——包含物理背景、度规定义和所有假设，做题者无需参考种子题。难度与种子题相当，只聚焦一个物理问题。

### Phase 2：度规替换

将 Phase 1 生成的每道题适配到一个新的度规上（从度规库中挑选）。保持题目类型和结构不变，用新度规的数据替换原度规，答案从新度规的几何属性推导。

度规挑选由 LLM 完成——根据题目的物理场景和求解目标，从度规库中选择最合适的替换度规（排除 heavy 度规和当前度规）。

## 正确性保证

### SymPy Fact Sheet（绝对可靠）

从度规出发，SymPy 符号计算所有几何属性：Christoffel 符号、Riemann 张量、Ricci 张量/标量、Kretschmann 标量、Einstein 张量。这些数据数学上精确无误，作为答案验证的基准。

Fact Sheet 计算一次后缓存到种子 JSON 中，后续步骤直接读取。

### LLM 验证 + 修正循环

每道生成题经过验证：
1. 检查 answer/solution 中引用的中间量是否与 Fact Sheet 一致
2. 检查推导逻辑是否正确
3. 如果验证失败，LLM 根据 issues 修正答案，再重新验证
4. 最多循环 2 次

`tools_used` 字段记录了验证使用的模型（如 `validate:glm-5.1`）。

## 使用方法

### 一步运行（推荐）

```bash
python main.py run <输入文件> --num 3 --subs 3 -o variants
```

输入可以是 `.md`（自动抽象化）或 `.json`（已有种子题）。

示例：
```bash
python main.py run test.md --num 3 --subs 3 -o variants
```

生成 3 道基础题 + 3×3 = 9 道度规替换题，共 12 道。

### 分步运行

```bash
# 只做抽象化
python main.py abstract <文件> -o seed.json

# 只做泛化（需要已有种子 JSON）
python main.py generate seed.json --num 3 --subs 3 -o variants

# 对已有题目做验证+修正
python main.py validate <json文件>

# 清理排版（只清理 $...$ 内的空格）
python main.py clean <json文件>
```

## 模型配置

各阶段使用的 LLM 模型可在 `core/config.py` 中配置：

| 变量 | 阶段 | 默认值 |
|------|------|--------|
| `MODEL_ABSTRACT` | 抽象化 | `qwen3.6-flash` |
| `MODEL_COMPOSE` | 编题 | `glm-5.1` |
| `MODEL_SUBSTITUTE` | 度规替换 | `glm-5.1` |
| `MODEL_PICK_METRIC` | 挑选度规 | `qwen3.6-flash` |
| `MODEL_VALIDATE` | 验证 | `glm-5.1` |
| `MODEL_FIX` | 修正 | `glm-5.1` |

也可通过环境变量覆盖：
```bash
MODEL_VALIDATE=claude-sonnet-4-6 python main.py run test.json ...
```

## 度规库

包含 8 个核心度规（聚焦 GR 张量计算，Fact Sheet $<30$s）和 6 个 heavy 度规（计算太慢，不用于自动化）：

**核心度规**：Schwarzschild, Minkowski, DeSitter, AntiDeSitter, AntiDeSitterStatic, MinkowskiCartesian, MinkowskiPolar, FLRW

**Heavy 度规**：Kerr, Ernst, KerrNewman, ReissnerNordstrom, AlcubierreWarp, BesselGravitationalWave

## 项目结构

```
hw_pipeline/
├── main.py              # CLI 入口
├── core/
│   ├── config.py        # 模型和 API 配置
│   ├── pipeline.py      # 泛化流水线主逻辑
│   ├── validator.py     # 验证+修正循环
│   ├── formatter.py     # 题目抽象化
│   ├── cleaner.py       # 排版清理
│   ├── metric_library.py# 度规库
│   ├── sympy_engine.py  # SymPy Fact Sheet 计算
│   ├── system_prompts.py# 各阶段 LLM prompt
│   ├── api_client.py    # API 调用客户端
│   └── file_converter.py # PDF/Word → 图片
├── schema/
│   └── schema.py        # 数据结构定义
└── variants/            # 输出目录
```

## 输出 JSON 格式

每道题包含三个部分：

```json
{
  "metadata": {
    "id": "test-0",
    "type": "calculate",
    "tags": {"metric": "Schwarzschild", "target_object": "geodesic equation", ...},
    "tools_used": ["EinsteinPy", "validate:glm-5.1"],
    "validated": true,
    "source": "generated"
  },
  "physical_data": {
    "dimension": 4,
    "variables": ["$t$", "$r$", "$\\theta$", "$\\phi$"],
    "metric": [["$-(1-\\frac{2M}{r})$", ...], ...],
    "metric_sympy": [["-1", ...], ...],
    "target": ["$\\Gamma_{01}^{1}$", ...]
  },
  "origin": {
    "question": "独立完整的题目原文...",
    "answer": "最终结论或无答案",
    "solution": "推导思路或 null",
    "hint": ["实用提示列表或 null"]
  }
}
```