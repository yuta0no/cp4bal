from logging import getLogger
from pathlib import Path

import torch

from cp4bal.acquisition import AcquisitionFactory
from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import (
    CSBM,
    ActiveLearningDataset,
    CommonDatasetConfig,
    CSBMConfig,
    DatasetConfig,
    DatasetSplit,
    EdgeProbabilityType,
)
from cp4bal.model import ModelFactory, ModelName
from cp4bal.model.trainer import OracleTrainerConfig
from cp4bal.util.logger import init_logger
from cp4bal.util.seed import set_seed

logger = getLogger(__name__)


def main():
    rng, big_seed = set_seed(seed=52)
    generator = torch.random.manual_seed(rng.integers(2**31))

    # Dataset
    ds_config = DatasetConfig(
        common=CommonDatasetConfig(
            seed=big_seed, name="csbm", num_nodes=24, num_classes=3, dim_features=10, val_size=0.0, test_size=0.3
        ),
        detail=CSBMConfig(
            feature_sigma=1.0,
            feature_class_mean_distance=1.0,
            edge_p_type=EdgeProbabilityType.BY_SNR_AND_DEGREE,
            p_edge_inter=None,
            p_edge_intra=None,
            expected_degree=8,
            edge_p_snr=10,
        ),
    )
    csbm = CSBM(
        common_config=ds_config.common,
        csbm_config=ds_config.detail,
    )
    ds = ActiveLearningDataset(base=csbm, config=ds_config)
    ds.split().print_masks()
    ds.select_initial_pool(count_per_class=1)

    # Model for Training
    model_name = ModelName.BAYES_OPTIMAL
    model = ModelFactory.create(name=model_name, dataset=ds)
    trainer_config = OracleTrainerConfig()

    # Active Learning
    acquisition_method = AcquisitionFactory.create(acquisition_type="oracle_uncertainty")

    TOTAL_AL_ROUND = 10
    for al_round in range(TOTAL_AL_ROUND):
        logger.info(f"Round {al_round + 1}/{TOTAL_AL_ROUND}")

        AL.train_model(
            config=trainer_config,
            model=model,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )

        AL.evaluate_model(
            model=model,
            dataset=ds,
            rg=generator,
            which=DatasetSplit.VAL,
            al_round=al_round,
        )
        AL.evaluate_model(
            model=model,
            dataset=ds,
            rg=generator,
            which=DatasetSplit.TEST,
            al_round=al_round,
        )

        ds = AL.acquire_samples(
            budget=1,  # TODO
            model=model,
            acquisition=acquisition_method,
            dataset=ds,
            rg=generator,
            al_round=al_round,
        )


if __name__ == "__main__":
    init_logger(log_dir=Path("logs"), log_file_name="cp4bal")
    try:
        main()
    except Exception as e:
        logger.error(f"error occurred: {e}")
        raise e

    logger.info("finished")
