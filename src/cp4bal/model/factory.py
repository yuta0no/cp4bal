from cp4bal.dataset import ActiveLearningDataset
from cp4bal.util.configs import GCNConfig, SGCConfig
from cp4bal.util.enums import ModelName

from .gcn import GCN
from .sgc import SGC


class ModelFactory:
    @staticmethod
    def create(name: ModelName, dataset: ActiveLearningDataset):
        match name:
            case ModelName.SGC:
                return SGC(config=SGCConfig(), dataset=dataset)
            case ModelName.GCN:
                return GCN(config=GCNConfig(), dataset=dataset)
            case _:
                raise ValueError(f"Model {name} is not supported.")
