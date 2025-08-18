from logging import getLogger
from pathlib import Path

import torch

from cp4bal.acquisition import AcquisitionFactory
from cp4bal.active_learning import ActiveLearning as AL
from cp4bal.dataset import (
    ActiveLearningDataset,
    DatasetSplit,
)
from cp4bal.dataset.enums import EdgeProbabilityType
from cp4bal.dataset.factory import DatasetFactory
from cp4bal.model import ModelFactory
from cp4bal.util.config_builder import ConfigBuilder
from cp4bal.util.logger import init_logger
from cp4bal.util.seed import set_seed

logger = getLogger(__name__)


def main():
    rng, big_seed = set_seed(seed=52)
    generator = torch.random.manual_seed(rng.integers(2**31))

    # configs
    cb = ConfigBuilder().set_seed(big_seed)
    # config for dataset
    cb.set_ds_name("csbm").set_n_nodes(140).set_n_classes(7).set_dim_features(10).set_val_size(0.0).set_test_size(
        0.3
    ).set_feature_sigma(1.0).set_feature_class_mean_distance(1.0).set_edge_p_type(
        EdgeProbabilityType.BY_SNR_AND_DEGREE
    ).set_expected_degree(8).set_edge_p_snr(10.0)

    # config for trainer
    cb.set_trainer_name("sgc")

    # config for model
    cb.set_model_name("sgc")

    # config for acquisition
    cb.set_acquisition_name("random")

    # config for active learning
    cb.set_budget(5).set_round(5)

    configs = cb.build(config_path=Path("configs/dataset.yaml"))

    # Dataset
    base_ds = DatasetFactory.create(config=configs.dataset)
    ds = ActiveLearningDataset(base=base_ds, config=configs.dataset)
    ds.split().print_masks()
    ds.select_initial_pool(count_per_class=1)

    # Model for Training
    model = ModelFactory.create(config=configs.model, dataset=ds)

    # Active Learning
    acquisition_method = AcquisitionFactory.create(config=configs.acquisition)

    for al_round in range(configs.al.num_rounds):
        logger.info(f"Round {al_round + 1}/{configs.al.num_rounds}")

        AL.train_model(
            trainer_config=configs.trainer,
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
            budget=configs.al.budget_per_round,  # TODO
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
