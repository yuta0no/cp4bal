from cp4bal.dataset import ActiveLearningDataset

from .bayes_optimal import BayesOptimalModel
from .configs import BayesOptimalConfig, GCNConfig, SGCConfig
from .enums import ModelName
from .gcn import GCN
from .sgc import SGC


class ModelFactory:
    @staticmethod
    def create(name: ModelName, dataset: ActiveLearningDataset):
        match name:
            case ModelName.BAYES_OPTIMAL:
                return BayesOptimalModel(config=BayesOptimalConfig(), dataset=dataset)
            case ModelName.SGC:
                return SGC(config=SGCConfig(), dataset=dataset)
            case ModelName.GCN:
                return GCN(config=GCNConfig(), dataset=dataset)
            case _:
                raise ValueError(f"Model {name} is not supported.")
