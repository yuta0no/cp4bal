from .configs import DatasetConfig
from .csbm import CSBM
from .torch_geometric import TorchGeometricDataset, TorchGeometricDatasetType


class DatasetFactory:
    @staticmethod
    def create(config: DatasetConfig) -> CSBM:
        if config.common.name == "csbm":
            return CSBM(
                csbm_config=config.detail,
            )
        if config.common.name in [d.value for d in TorchGeometricDatasetType]:
            ds = TorchGeometricDataset(config=config.detail)
            return ds
        else:
            raise ValueError(f"Unknown dataset name: {config.common.name}")
