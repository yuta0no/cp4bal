from enum import Enum, auto, unique


@unique
class AcquisitionType(Enum):
    RANDOM = auto()
    ENTROPY = auto()
    ORACLE_UNCERTAINTY = auto()


@unique
class UncertaintyType(Enum):
    EPISTEMIC = auto()
    ALEATORIC = auto()
    TOTAL = auto()
