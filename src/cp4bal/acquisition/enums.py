from enum import Enum, StrEnum, auto, unique


@unique
class AcquisitionType(Enum):
    RANDOM = auto()
    CORESET_FEATURE = auto()
    DEGREE = auto()
    ENERGY = auto()
    ENTROPY = auto()
    LEAST_CONFIDENCE = auto()
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


@unique
class CoresetDistance(StrEnum):
    LATENT_FEATURES = "latent_space"
    INPUT_FEATURES = "input_features"
    APPR = "appr"


@unique
class DegreeType(Enum):
    IN = "in"
    OUT = "out"
