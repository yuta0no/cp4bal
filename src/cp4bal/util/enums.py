from enum import Enum, StrEnum, auto, unique


class EdgeProbabilityType(Enum):
    BY_SNR_AND_DEGREE = auto()


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
    GCN = "gcn"
    BAYES_OPTIMAL = "bayes_optimal"


# Trainer
@unique
class TrainerType(StrEnum):
    SGD = "sgd"
    ORACLE = "oracle"
