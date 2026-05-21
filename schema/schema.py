from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Metadata:
    id: str
    type: str #"prove", "calculate", "concept"
    tags: Dict[str, str] = field(default_factory=dict)
    tools_used: List[str] = field(default_factory=list)
    validated: bool = False
    source: Optional[str] = None #书本名字 论文名字 或 generated


@dataclass
class PhysicalData:
    dimension: int
    variables: List[str]
    target: List[str]  # ["\\Gamma_{ij}^k", "R_{ijkl}"]
    metric: Optional[List[List[str]]] = None  # N×N matrix, aligned with variables order, LaTeX format
    metric_sympy: Optional[List[List[str]]] = None  # N×N matrix, SymPy format for validation


@dataclass
class Origin:
    question: str
    answer: Optional[str] = None
    solution: Optional[str] = None
    hint: Optional[List[str]] = None


@dataclass
class Problem:
    metadata: Metadata
    physical_data: PhysicalData
    origin: Origin