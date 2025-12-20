from enum import Enum, auto, unique


@unique
class AcquisitionType(Enum):
    RANDOM = auto()
    ENTROPY = auto()
    ORACLE_UNCERTAINTY = auto()
    ORACLE_UNCERTAINTY_CP = auto()
    APPROXIMATE_UNCERTAINTY = auto()
    APPROXIMATE_UNCERTAINTY_CP = auto()


@unique
class UncertaintyType(Enum):
    EPISTEMIC = auto()
    ALEATORIC = auto()
    TOTAL = auto()
