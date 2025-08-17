from enum import Enum, StrEnum, auto, unique


class EdgeProbabilityType(Enum):
    BY_SNR_AND_DEGREE = auto()


# Acquisition
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


# Dataset
@unique
class DatasetSplit(StrEnum):
    TRAIN_L = "train_l"  # labeled training set
    TRAIN_U = "train_u"  # unlabeled training set
    TRAIN_ALL = "train_all"  # all training data
    VAL = "val"
    TEST = "test"
    ALL = "all"


# Model
@unique
class ModelName(StrEnum):
    BAYES_OPTIMAL = "bayes_optimal"
    GCN = "gcn"
    SGC = "sgc"


# Trainer
@unique
class TrainerType(StrEnum):
    ADAM = "adam"
    ORACLE = "oracle"
    SGC = "sgc"
