from dataclasses import dataclass
from enum import Enum


class ActiveLearningMethod(Enum):
    RANDOM = "random"
    ORACLE_UNCERTAINTY = "oracle_uncertainty"
    ORACLE_UNCERTAINTY_CP = "oracle_uncertainty_cp"


@dataclass
class ResultPaths:
    name: str
    method: ActiveLearningMethod
    paths: list[str]
