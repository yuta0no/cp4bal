from enum import Enum, StrEnum, auto, unique


class EdgeProbabilityType(Enum):
    BY_SNR_AND_DEGREE = auto()


@unique
class DatasetSplit(StrEnum):
    TRAIN_L = "train_l"  # labeled training set
    TRAIN_U = "train_u"  # unlabeled training set
    TRAIN_ALL = "train_all"  # all training data
    VAL = "val"
    TEST = "test"
    ALL = "all"


@unique
class ImplementationType(StrEnum):
    VANILLA = "vanilla"
    NUMBA = "numba"


@unique
class InitialPoolSelectionType(StrEnum):
    RANDOM = "random"
    RANDOM_1 = "random_1"
    BALANCED = "balanced"
