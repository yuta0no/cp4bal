from enum import StrEnum, unique


@unique
class EdgeProbabilityType(StrEnum):
    BY_SNR_AND_DEGREE = "by_snr_and_degree"


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


@unique
class TorchGeometricDatasetType(StrEnum):
    AMAZON_COMPUTERS = "amazon_computers"
    AMAZON_PHOTOS = "amazon_photos"
    CORA_ML = "cora_ml"
    CITESEER = "citeseer"
    OGBN_ARXIV = "ogbn_arxiv"
    PUBMED = "pubmed"
    REDDIT = "reddit"
