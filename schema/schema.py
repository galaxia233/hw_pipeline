"""Pipeline 数据 Schema

内部使用嵌套结构（保留 physical_data 等GR专用字段），
输出到 dataset.jsonl 时通过 to_dataset_record() 转为作业要求的 flat 格式。

作业要求格式 (Appendix A):
  id / statement / answer / solution / meta / verification
内部格式 (保留已有):
  metadata / physical_data / origin / verification
"""

import hashlib
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional


# ==================== ID 生成 ====================


def generate_id(*parts: str, length: int = 12) -> str:
    """基于多个字符串生成短 hash ID

    Args:
        parts: 用于生成 hash 的字符串（如 source_id, seed_id, stage 等）
        length: hash 长度（默认 12 字符）

    Returns:
        短 hash 字符串，全局唯一
    """
    raw = "_".join(parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]


# ==================== 认知形式枚举 ====================


COGNITIVE_FORMS = [
    "derivation",       # 推导/证明题（原 type="prove"）
    "numerical",        # 数值计算题（原 type="calculate"）
    "conceptual",       # 概念理解题（原 type="concept"）
    "code",             # 编程题
    "multiple_choice",  # 选择题（带 distractor）
    "open",             # 开放题（answer=NO_ANSWER）
]

# type → cognitive_form 映射（保留旧字段兼容）
TYPE_TO_COGNITIVE = {
    "prove": "derivation",
    "calculate": "numerical",
    "concept": "conceptual",
    "code": "code",
    "multiple_choice": "multiple_choice",
    "open": "open",
}

# 反向映射（cognitive_form → type）
COGNITIVE_TO_TYPE = {
    "derivation": "prove",
    "numerical": "calculate",
    "conceptual": "concept",
    "code": "calculate",
    "multiple_choice": "concept",
    "open": "concept",
}

# 软变体类型
SOFT_VARIANTS = [
    "substitute",   # 度规替换
    "extend",       # 延伸（种子题方向的进一步推进）
    "reduce",       # 简化（降低难度）
    "contrast",     # 对比（不同条件下的对比）
    "design",       # 设计（从零设计新题）
    "form_change:multiple_choice",  # 形式变换→选择题
    "form_change:code",             # 形式变换→编程题
    "form_change:conceptual",       # 形式变换→概念题
]

# 来源类型
SOURCE_TYPES = ["paper", "textbook", "problem_set"]

# stage 名称
STAGE_NAMES = [
    "seed",                              # Stage 0: 原始种子题
    "scale:cognitive_fanout",            # 认知泛化
    "scale:metric_substitute",           # 度规替换
    "scale:form_change",                 # 形式变换（multiple_choice/code/conceptual）
    "scale:soft_rewrite",                # 软变体重写
]


# ==================== 数据类定义 ====================


@dataclass
class Metadata:
    id: str
    type: str  # "prove" | "calculate" | "concept"（保留兼容，cognitive_form 为主分类）
    tags: Dict[str, str] = field(default_factory=dict)
    tools_used: List[str] = field(default_factory=list)
    validated: bool = False   # 旧字段，保留兼容；verification.ok 替代
    source: Optional[str] = None  # 旧字段，保留兼容；source_id 替代

    # ---- 作业要求新增字段 ----
    source_id: Optional[str] = None      # 来源ID (arXiv ID / 书名 / 题集名)
    source_type: Optional[str] = None    # "paper" | "textbook" | "problem_set"
    stage: Optional[str] = None          # 当前 stage 名称
    lineage: List[str] = field(default_factory=list)  # ID 链: [source_id, ..., current_id]
    topic: Optional[str] = None          # 主题 (如 "f(R) gravity stability conditions")
    concepts: List[str] = field(default_factory=list) # 概念列表
    cognitive_form: Optional[str] = None # 认知形式 (derivation/numerical/conceptual/code/multiple_choice/open)
    physics_env: Optional[str] = None    # 物理环境/度规 (如 "Schwarzschild", "FLRW_flat")
    soft_variant: Optional[str] = None   # 软变体类型 (substitute/extend/reduce/contrast/design)
    training_value: Optional[float] = None  # 训练价值 0.0–1.0
    degraded: Optional[bool] = None      # 重跑耗尽仍不达标时标记
    quality: Optional[Dict] = None       # 质量评分 {physical_depth, generalizability, completeness, mathematical_richness, overall, rationale}


@dataclass
class PhysicalData:
    dimension: int
    variables: List[str]
    target: List[str]  # ["$\\Gamma_{ij}^k$", "$R_{ijkl}$"]
    metric: Optional[List[List[str]]] = None  # N×N LaTeX 矩阵
    metric_sympy: Optional[List[List[str]]] = None  # N×N SymPy 矩阵（验证用）


@dataclass
class Origin:
    question: str         # 题目原文 → dataset.jsonl 的 statement
    answer: Optional[str] = None    # 答案 → dataset.jsonl 的 answer（"无答案" → NO_ANSWER）
    solution: Optional[str] = None  # 解题过程 → dataset.jsonl 的 solution


# ==================== Verification 结构 ====================


@dataclass
class StructuralCheck:
    """结构完整性检查：字段齐全、answer非空等"""
    ok: bool = False
    issues: List[str] = field(default_factory=list)


@dataclass
class MetricCheck:
    """SymPy 度规/几何量验证"""
    checker: Optional[str] = None   # 如 "sympy_verify.is_vacuum_einstein"
    status: Optional[str] = None    # "ok" | "fail" | "skip"
    details: Optional[Dict] = None  # 如 {"vacuum": true, "ricci_scalar": "0"}


@dataclass
class JudgeCheck:
    """LLM judge 验证：正确性、自洽性、self-contained"""
    correct: bool = False
    self_contained: bool = False
    training_value: Optional[float] = None  # judge 给出的训练价值
    issue: str = ""


@dataclass
class RedTeamCheck:
    """Adversarial red-team 检查"""
    survives: bool = False
    flaw: str = ""


@dataclass
class StageEval:
    """Stage 级别评估"""
    ok: bool = False
    score: Optional[float] = None


@dataclass
class Verification:
    """验证结果汇总"""
    structural: Optional[StructuralCheck] = None
    metric_check: Optional[MetricCheck] = None
    judge: Optional[JudgeCheck] = None
    red_team: Optional[RedTeamCheck] = None
    stage_eval: Optional[StageEval] = None


# ==================== Problem 主体 ====================


@dataclass
class Problem:
    metadata: Metadata
    physical_data: PhysicalData
    origin: Origin
    verification: Optional[Verification] = None  # 新增


# ==================== dataset.jsonl 输出转换 ====================


def problem_to_dataset_record(problem: Problem) -> dict:
    """将内部 Problem 转为作业要求的 dataset.jsonl 格式

    保留的字段映射：
      metadata.id       → id
      origin.question   → statement
      origin.answer     → answer (无答案/NO_ANSWER)
      origin.solution   → solution
      metadata.source   → meta.source_id (fallback)
      metadata.tags     → meta.physics_env / meta.topic
      metadata.type     → meta.cognitive_form (映射)

    不进入 dataset 的字段：
      physical_data     — 内部验证用，保留在文件中但不写入 dataset.jsonl
      metadata.validated/source — 旧兼容字段
    """
    meta = problem.metadata
    verification = problem.verification

    # answer 处理：中文"无答案" → NO_ANSWER
    answer = problem.origin.answer
    if answer is None or (answer and "无答案" in answer):
        answer = "NO_ANSWER"

    # cognitive_form 处理：有值直接用，否则从 type 映射
    cognitive_form = meta.cognitive_form or TYPE_TO_COGNITIVE.get(meta.type, meta.type)

    # physics_env 处理：有值直接用，否则从 tags.metric 映射
    physics_env = meta.physics_env or meta.tags.get("metric", "")

    # source_id 处理：有值直接用，否则 fallback 到 source
    source_id = meta.source_id or meta.source or ""

    # lineage 处理：有值直接用，否则 fallback [source_id]
    lineage = meta.lineage if meta.lineage else [source_id]

    # topic 处理：有值直接用，否则 fallback 到 tags.scenario
    topic = meta.topic or meta.tags.get("scenario", "")

    # training_value 处理：meta 优先，否则从 judge 取
    training_value = meta.training_value
    if training_value is None and verification and verification.judge:
        training_value = verification.judge.training_value

    result = {
        "id": meta.id,
        "statement": problem.origin.question,
        "answer": answer,
        "solution": problem.origin.solution or "",
        "meta": {
            "source_id": source_id,
            "source_type": meta.source_type or "problem_set",
            "stage": meta.stage or "seed",
            "lineage": lineage,
            "topic": topic,
            "concepts": meta.concepts,
            "tools_used": meta.tools_used,
            "cognitive_form": cognitive_form,
            "physics_env": physics_env,
            "soft_variant": meta.soft_variant or "",
            "training_value": training_value,
            "degraded": meta.degraded or False,
            "quality": meta.quality or {},
        },
    }

    # verification：有值才写入
    if verification:
        result["verification"] = _verification_to_dict(verification)
    else:
        result["verification"] = {}

    return result


def _verification_to_dict(v: Verification) -> dict:
    """将 Verification 对象转为 dict"""
    result = {}

    if v.structural:
        result["structural"] = {"ok": v.structural.ok}
        if v.structural.issues:
            result["structural"]["issues"] = v.structural.issues

    if v.metric_check:
        mc = {"checker": v.metric_check.checker or "", "status": v.metric_check.status or "skip"}
        if v.metric_check.details:
            mc.update(v.metric_check.details)
        result["metric_check"] = mc

    if v.judge:
        result["judge"] = {
            "correct": v.judge.correct,
            "self_contained": v.judge.self_contained,
            "training_value": v.judge.training_value,
            "issue": v.judge.issue,
        }

    if v.red_team:
        result["red_team"] = {
            "survives": v.red_team.survives,
            "flaw": v.red_team.flaw,
        }

    if v.stage_eval:
        result["stage_eval"] = {
            "ok": v.stage_eval.ok,
            "score": v.stage_eval.score,
        }

    return result


def dataset_record_to_problem(record: dict) -> Problem:
    """将 dataset.jsonl 格式转回内部 Problem 格式（用于从 dataset 加载）

    physical_data 需要额外提供（dataset.jsonl 中不包含）。
    """
    m = record.get("meta", {})

    # cognitive_form → type 反向映射
    cognitive_form = m.get("cognitive_form", "")
    type_ = COGNITIVE_TO_TYPE.get(cognitive_form, "calculate")

    # 从 dataset 格式重建 metadata
    metadata = Metadata(
        id=record["id"],
        type=type_,
        tags={"metric": m.get("physics_env", ""), "scenario": m.get("topic", "")},
        tools_used=m.get("tools_used", []),
        validated=False,  # will be set from verification
        source=m.get("source_id", ""),
        source_id=m.get("source_id", ""),
        source_type=m.get("source_type", "problem_set"),
        stage=m.get("stage", "seed"),
        lineage=m.get("lineage", []),
        topic=m.get("topic", ""),
        concepts=m.get("concepts", []),
        cognitive_form=cognitive_form,
        physics_env=m.get("physics_env", ""),
        soft_variant=m.get("soft_variant", ""),
        training_value=m.get("training_value"),
    )

    # answer 处理：NO_ANSWER → None
    answer = record.get("answer", "")
    if answer == "NO_ANSWER":
        answer = None

    origin = Origin(
        question=record["statement"],
        answer=answer,
        solution=record.get("solution") or None,
    )

    # physical_data: 需要从外部文件加载，此处用占位
    physical_data = PhysicalData(
        dimension=4,
        variables=[],
        target=[],
    )

    # verification: 从 dataset 格式重建
    verification = _dict_to_verification(record.get("verification", {}))

    return Problem(
        metadata=metadata,
        physical_data=physical_data,
        origin=origin,
        verification=verification,
    )


def _dict_to_verification(v_dict: dict) -> Optional[Verification]:
    """从 dict 转 Verification 对象"""
    if not v_dict:
        return None

    structural = None
    if "structural" in v_dict:
        s = v_dict["structural"]
        structural = StructuralCheck(
            ok=s.get("ok", False),
            issues=s.get("issues", []),
        )

    metric_check = None
    if "metric_check" in v_dict:
        mc = v_dict["metric_check"]
        details = {k: v for k, v in mc.items() if k not in ("checker", "status")}
        metric_check = MetricCheck(
            checker=mc.get("checker"),
            status=mc.get("status"),
            details=details or None,
        )

    judge = None
    if "judge" in v_dict:
        j = v_dict["judge"]
        judge = JudgeCheck(
            correct=j.get("correct", False),
            self_contained=j.get("self_contained", False),
            training_value=j.get("training_value"),
            issue=j.get("issue", ""),
        )

    red_team = None
    if "red_team" in v_dict:
        rt = v_dict["red_team"]
        red_team = RedTeamCheck(
            survives=rt.get("survives", False),
            flaw=rt.get("flaw", ""),
        )

    stage_eval = None
    if "stage_eval" in v_dict:
        se = v_dict["stage_eval"]
        stage_eval = StageEval(
            ok=se.get("ok", False),
            score=se.get("score"),
        )

    return Verification(
        structural=structural,
        metric_check=metric_check,
        judge=judge,
        red_team=red_team,
        stage_eval=stage_eval,
    )


# ==================== 全扁平 Parquet 输出 ====================


def problem_to_flat_record(problem: Problem) -> dict:
    """将 Problem 转为全扁平 dict（28 列，Parquet 列式存储友好）

    与 problem_to_dataset_record 不同，所有 meta/verification 子字段
    提升为顶层键，无嵌套结构。

    字段列表:
      id, statement, answer, solution,
      source_id, source_type, stage, lineage, topic, concepts,
      cognitive_form, physics_env, soft_variant, training_value,
      degraded, quality, tools_used,
      structural_ok, metric_check_status, metric_check_checker,
      judge_correct, judge_self_contained, judge_training_value, judge_issue,
      red_team_survives, red_team_flaw,
      stage_eval_ok, stage_eval_score
    """
    meta = problem.metadata
    verification = problem.verification

    # answer 处理
    answer = problem.origin.answer
    if answer is None or (answer and "无答案" in answer):
        answer = "NO_ANSWER"

    # cognitive_form 处理
    cognitive_form = meta.cognitive_form or TYPE_TO_COGNITIVE.get(meta.type, meta.type)

    # physics_env 处理
    physics_env = meta.physics_env or meta.tags.get("metric", "")

    # source_id 处理
    source_id = meta.source_id or meta.source or ""

    # lineage 处理
    lineage = meta.lineage if meta.lineage else [source_id]

    # topic 处理
    topic = meta.topic or meta.tags.get("scenario", "")

    # training_value 处理
    training_value = meta.training_value
    if training_value is None and verification and verification.judge:
        training_value = verification.judge.training_value

    # quality: 将 dict 值转为 string（map<string,string> 类型友好）
    quality = {}
    if meta.quality:
        for k, v in meta.quality.items():
            quality[k] = str(v) if v is not None else ""

    # verification 字段
    structural_ok = False
    metric_check_status = "skip"
    metric_check_checker = ""
    judge_correct = False
    judge_self_contained = False
    judge_training_value = None
    judge_issue = ""
    red_team_survives = False
    red_team_flaw = ""
    stage_eval_ok = False
    stage_eval_score = None

    if verification:
        if verification.structural:
            structural_ok = verification.structural.ok
        if verification.metric_check:
            metric_check_status = verification.metric_check.status or "skip"
            metric_check_checker = verification.metric_check.checker or ""
        if verification.judge:
            judge_correct = verification.judge.correct
            judge_self_contained = verification.judge.self_contained
            judge_training_value = verification.judge.training_value
            judge_issue = verification.judge.issue
        if verification.red_team:
            red_team_survives = verification.red_team.survives
            red_team_flaw = verification.red_team.flaw
        if verification.stage_eval:
            stage_eval_ok = verification.stage_eval.ok
            stage_eval_score = verification.stage_eval.score

    return {
        "id": meta.id,
        "statement": problem.origin.question,
        "answer": answer,
        "solution": problem.origin.solution or "",
        "source_id": source_id,
        "source_type": meta.source_type or "problem_set",
        "stage": meta.stage or "seed",
        "lineage": lineage,
        "topic": topic,
        "concepts": meta.concepts,
        "cognitive_form": cognitive_form,
        "physics_env": physics_env,
        "soft_variant": meta.soft_variant or "",
        "training_value": training_value,
        "degraded": meta.degraded or False,
        "quality": quality,
        "tools_used": meta.tools_used,
        "structural_ok": structural_ok,
        "metric_check_status": metric_check_status,
        "metric_check_checker": metric_check_checker,
        "judge_correct": judge_correct,
        "judge_self_contained": judge_self_contained,
        "judge_training_value": judge_training_value,
        "judge_issue": judge_issue,
        "red_team_survives": red_team_survives,
        "red_team_flaw": red_team_flaw,
        "stage_eval_ok": stage_eval_ok,
        "stage_eval_score": stage_eval_score,
    }


def dict_to_flat_record(problem_dict: dict) -> dict:
    """将 pipeline 内部格式的 dict 转为全扁平 record（用于从 JSON 文件直接转换）。

    内部格式: {metadata, physical_data, origin, verification}
    扁平格式: 28 个顶层字段，无嵌套。
    """
    md = problem_dict.get("metadata", {})
    vf = problem_dict.get("verification", {}) or {}

    # answer 处理
    answer = problem_dict.get("origin", {}).get("answer")
    if answer is None or (answer and "无答案" in answer):
        answer = "NO_ANSWER"

    # cognitive_form 处理
    cognitive_form = md.get("cognitive_form") or TYPE_TO_COGNITIVE.get(md.get("type", ""), md.get("type", ""))

    # physics_env 处理
    physics_env = md.get("physics_env") or md.get("tags", {}).get("metric", "")

    # source_id 处理
    source_id = md.get("source_id") or md.get("source", "")

    # lineage 处理
    lineage = md.get("lineage") or [source_id]

    # topic 处理
    topic = md.get("topic") or md.get("tags", {}).get("scenario", "")

    # training_value 处理
    training_value = md.get("training_value")
    if training_value is None:
        judge = vf.get("judge", {})
        if judge:
            training_value = judge.get("training_value")

    # quality: 将 dict 值转为 string
    quality = {}
    q = md.get("quality")
    if q:
        for k, v in q.items():
            quality[k] = str(v) if v is not None else ""

    # verification 字段
    structural = vf.get("structural", {}) or {}
    metric_check = vf.get("metric_check", {}) or {}
    judge = vf.get("judge", {}) or {}
    red_team = vf.get("red_team", {}) or {}
    stage_eval = vf.get("stage_eval", {}) or {}

    return {
        "id": md.get("id") or "",
        "statement": problem_dict.get("origin", {}).get("question") or "",
        "answer": answer,
        "solution": problem_dict.get("origin", {}).get("solution") or "",
        "source_id": source_id,
        "source_type": md.get("source_type") or "problem_set",
        "stage": md.get("stage") or "seed",
        "lineage": lineage,
        "topic": topic,
        "concepts": md.get("concepts") or [],
        "cognitive_form": cognitive_form,
        "physics_env": physics_env,
        "soft_variant": md.get("soft_variant") or "",
        "training_value": training_value,
        "degraded": md.get("degraded") or False,
        "quality": quality,
        "tools_used": md.get("tools_used") or [],
        "structural_ok": structural.get("ok") or False,
        "metric_check_status": metric_check.get("status") or "skip",
        "metric_check_checker": metric_check.get("checker") or "",
        "judge_correct": judge.get("correct") or False,
        "judge_self_contained": judge.get("self_contained") or False,
        "judge_training_value": judge.get("training_value"),
        "judge_issue": judge.get("issue") or "",
        "red_team_survives": red_team.get("survives") or False,
        "red_team_flaw": red_team.get("flaw") or "",
        "stage_eval_ok": stage_eval.get("ok") or False,
        "stage_eval_score": stage_eval.get("score"),
    }


# ==================== dataset.jsonl 读写 ====================


def write_dataset_jsonl(problems: List[Problem], path: str):
    """将 Problem 列表写为 dataset.jsonl（每行一个作业格式的记录）"""
    from pathlib import Path
    Path(path).write_text(
        "\n".join(json.dumps(problem_to_dataset_record(p), ensure_ascii=False) for p in problems),
        encoding="utf-8",
    )


def read_dataset_jsonl(path: str) -> List[Problem]:
    """从 dataset.jsonl 读取记录列表（每行转回内部 Problem 格式）

    注意：physical_data 为占位值，需要从额外文件补充。
    """
    from pathlib import Path
    problems = []
    for line in Path(path).read_text(encoding="utf-8").strip().split("\n"):
        if line.strip():
            record = json.loads(line)
            problems.append(dataset_record_to_problem(record))
    return problems


# ==================== Parquet 读写 ====================


def _get_parquet_schema():
    """构建 Parquet schema（28 列全扁平）

    延迟导入 pyarrow，仅在写入 Parquet 时才需要。
    """
    import pyarrow as pa

    return pa.schema([
        # 核心字段 (4)
        pa.field("id", pa.string()),
        pa.field("statement", pa.string()),
        pa.field("answer", pa.string()),
        pa.field("solution", pa.string()),
        # 元信息字段 (13)
        pa.field("source_id", pa.string()),
        pa.field("source_type", pa.string()),
        pa.field("stage", pa.string()),
        pa.field("lineage", pa.list_(pa.string())),
        pa.field("topic", pa.string()),
        pa.field("concepts", pa.list_(pa.string())),
        pa.field("cognitive_form", pa.string()),
        pa.field("physics_env", pa.string()),
        pa.field("soft_variant", pa.string()),
        pa.field("training_value", pa.float64()),
        pa.field("degraded", pa.bool_()),
        pa.field("quality", pa.map_(pa.string(), pa.string())),
        pa.field("tools_used", pa.list_(pa.string())),
        # 验证溯源字段 (11)
        pa.field("structural_ok", pa.bool_()),
        pa.field("metric_check_status", pa.string()),
        pa.field("metric_check_checker", pa.string()),
        pa.field("judge_correct", pa.bool_()),
        pa.field("judge_self_contained", pa.bool_()),
        pa.field("judge_training_value", pa.float64()),
        pa.field("judge_issue", pa.string()),
        pa.field("red_team_survives", pa.bool_()),
        pa.field("red_team_flaw", pa.string()),
        pa.field("stage_eval_ok", pa.bool_()),
        pa.field("stage_eval_score", pa.float64()),
    ])


def write_dataset_parquet(problems_or_records, path: str, from_dict: bool = False):
    """将题目列表写为 Parquet 文件（全扁平 28 列）

    Args:
        problems_or_records: Problem 对象列表 或 flat dict 列表
        path: 输出文件路径（.parquet）
        from_dict: True 时 problems_or_records 为 flat dict 列表（来自 dict_to_flat_record）
    """
    import pyarrow as pa
    import pyarrow.parquet as pq

    if from_dict:
        records = problems_or_records
    else:
        records = [problem_to_flat_record(p) for p in problems_or_records]

    schema = _get_parquet_schema()
    table = pa.Table.from_pylist(records, schema=schema)
    pq.write_table(table, path)


def write_json_dir_to_parquet(input_dir: str, output_path: str,
                              skip_degraded: bool = False,
                              skip_seeds: bool = False,
                              min_training_value: float = 0.0) -> int:
    """扫描目录中的 JSON 文件，汇总为 Parquet 文件

    Args:
        input_dir: 包含题目 JSON 文件的目录
        output_path: 输出 Parquet 文件路径
        skip_degraded: 是否跳过 degraded 题
        skip_seeds: 是否跳过 stage=seed 题
        min_training_value: 最低训练价值过滤

    Returns:
        写入的记录数
    """
    from pathlib import Path

    input_path = Path(input_dir)
    json_files = sorted(input_path.glob("*.json"))

    records = []
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
            if "metadata" not in data or "origin" not in data:
                continue

            md = data["metadata"]

            # 过滤
            if skip_degraded and md.get("degraded", False):
                continue
            if skip_seeds and md.get("stage", "") == "seed":
                continue
            tv = md.get("training_value")
            if tv is None and data.get("verification", {}).get("judge", {}).get("training_value") is not None:
                tv = data["verification"]["judge"]["training_value"]
            if min_training_value > 0 and (tv is None or tv < min_training_value):
                continue

            records.append(dict_to_flat_record(data))
        except Exception as e:
            print(f"  跳过 {jf.name}: {e}")

    if records:
        write_dataset_parquet(records, output_path, from_dict=True)

    return len(records)


def read_dataset_parquet(path: str) -> List[dict]:
    """从 Parquet 文件读取 flat record 列表

    Returns:
        flat dict 列表（28 列格式）
    """
    import pyarrow.parquet as pq

    table = pq.read_table(path)
    return table.to_pylist()