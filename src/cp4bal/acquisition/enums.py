from enum import Enum, auto, unique


@unique
class AcquisitionType(Enum):
    RANDOM = auto()
    ENTROPY = auto()
    MARGIN = auto()
    ORACLE_UNCERTAINTY = auto()
    ORACLE_UNCERTAINTY_CP = auto()
    APPROXIMATE_UNCERTAINTY = auto()
    APPROXIMATE_UNCERTAINTY_CP = auto()
    BY_ATTRIBUTE = auto()


@unique
class UncertaintyType(Enum):
    EPISTEMIC = auto()
    ALEATORIC = auto()
    TOTAL = auto()
