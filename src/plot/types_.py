from dataclasses import dataclass
from enum import Enum


class ActiveLearningMethod(Enum):
    ENERGY = "energy"
    ENTROPY = "entropy"
    RANDOM = "random"
    MARGIN = "margin"
    LEAST_CONFIDENCE = "least_confidence"
    ORACLE_UNCERTAINTY = "oracle_uncertainty"
    ORACLE_UNCERTAINTY_CP = "oracle_uncertainty_cp"
    APPROXIMATE_UNCERTAINTY = "approximate_uncertainty"


@dataclass
class ResultPaths:
    name: str
    method: ActiveLearningMethod
    paths: list[str]
