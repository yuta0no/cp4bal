import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Args:
    seed: int
    gpu_id: int
    experiment_name: str
    dataset_config_file: Path
    model_config_file: Path
    acquisition_name: str
    budget: int
    round: int
    propagation: bool


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Options for the application")
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument(
            "--seed",
            type=int,
            default=42,
            help="random seed",
        )
        self.parser.add_argument(
            "--gpu_id",
            type=int,
            default=0,
            help="GPU ID to use (default: 0)",
        )
        self.parser.add_argument(
            "--experiment_name",
            type=str,
            default="auto",
            help="experiment name",
        )
        self.parser.add_argument(
            "--dataset_config_file",
            type=Path,
            default="configs/dataset/csbm.yaml",
            help="dataset config file path",
        )
        self.parser.add_argument(
            "--model_config_file",
            type=Path,
            default="configs/model/bayes_optimal.yaml",
            help="model config file path",
        )
        self.parser.add_argument(
            "--acquisition_name",
            type=str,
            default="random",
            help="acquisition name",
        )
        self.parser.add_argument(
            "--budget",
            type=int,
            default=1,
            help="budget size per AL round",
        )
        self.parser.add_argument(
            "--round",
            type=int,
            default=10,
            help="number of AL rounds",
        )
        self.parser.add_argument(
            "--propagation",
            action="store_true",
            help="whether to use confidence propagation",
        )

    def parse(self):
        self.args = self.parser.parse_args(namespace=Args)
        return self
