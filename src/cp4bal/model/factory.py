from cp4bal.dataset import ActiveLearningDataset

from .bayes_optimal import BayesOptimalModel
from .configs import ModelConfig
from .enums import ModelName
from .gcn import GCN
from .sgc import SGC


class ModelFactory:
    @staticmethod
    def create(config: ModelConfig, dataset: ActiveLearningDataset):
        match config.name:
            case ModelName.BAYES_OPTIMAL:
                return BayesOptimalModel(config=config, dataset=dataset)
            case ModelName.SGC:
                return SGC(config=config, dataset=dataset)
            case ModelName.GCN:
                return GCN(config=config, dataset=dataset)
            case _:
                raise ValueError(f"Model {config.name} is not supported.")
