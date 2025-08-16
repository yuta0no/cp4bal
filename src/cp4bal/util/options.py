class Options:
    # def __init__(self):
    #     self.parser = argparse.ArgumentParser(description="Options for the application")
    #     self.add_arguments()

    # def add_arguments(self):
    #     self.parser.add_argument(
    #         "--seed",
    #         type=int,
    #         default=42,
    #         help="random seed",
    #     )
    #     self.parser.add_argument(
    #         "--gpu_id",
    #         type=int,
    #         default=0,
    #         help="GPU ID to use (default: 0)",
    #     )
    #     self.parser.add_argument(
    #         "--experiment_name",
    #         type=str,
    #         default="auto",
    #         help="experiment name",
    #     )
    #     self.parser.add_argument(
    #         "--model_config",
    #         type=Path,
    #         default="config/model/gcn.yaml",
    #         help="path to the model config file",
    #     )
    #     self.parser.add_argument(
    #         "--al_config",
    #         type=Path,
    #         default="config/al/random_tiny.yaml",
    #         help="path to the active learning config file",
    #     )
    #     self.parser.add_argument(
    #         "--dataset_config",
    #         type=Path,
    #         default="config/dataset/csbm.yaml",
    #         help="path to the dataset config file",
    #     )

    # def parse(self):
    #     self.args = self.parser.parse_args(namespace=ArgConfig)
    #     return self

    # def get_configs(self):
    #     sc = SystemConfig(
    #         seed=self.args.seed,
    #         device=self.__auto_detect_gpu(self.args.gpu_id),
    #     )
    #     ec = ExperimentConfig(
    #         name=self.__auto_exp_name(self.args.experiment_name),
    #     )
    #     dc = self._get_dataset_config()
    #     ac = self._get_al_config(num_classes=dc.common.num_classes)
    #     mc = self._get_model_config()
    #     return OverallConfig(system=sc, experiment=ec, al=ac, data=dc, model=mc)

    # def _get_al_config(self, num_classes: int) -> ActiveLearningConfig:
    #     yaml_data = OmegaConf.load(get_root_path() / self.args.al_config)
    #     yaml_data = self._process_al_config(yaml_data, num_classes)
    #     ac = OmegaConf.structured(ActiveLearningConfig)
    #     ac.merge_with(yaml_data)
    #     return OmegaConf.to_object(ac)

    # def _process_al_config(self, yaml_data: DictConfig | ListConfig, num_classes: int) -> DictConfig | ListConfig:
    #     # set actual budget size based on budget style
    #     match yaml_data.budget_style.lower():
    #         case "tiny":
    #             yaml_data.budget_per_round = num_classes
    #         case "small":
    #             yaml_data.budget_per_round = num_classes * 3
    #         case "custom":
    #             if yaml_data.budget_per_round is not None:
    #                 yaml_data.budget_per_round = int(yaml_data.budget_per_round)
    #         case _:
    #             raise ValueError(f"Unknown budget style: {yaml_data.budget_style}")
    #     return yaml_data

    # def _get_model_config(self) -> ModelConfig:
    #     yaml_data = OmegaConf.load(get_root_path() / self.args.model_config)
    #     mc = OmegaConf.structured(get_model_config_class(yaml_data.name))
    #     yaml_data = self._process_model_config(yaml_data)
    #     mc.merge_with(yaml_data)
    #     return OmegaConf.to_object(mc)

    # def _process_model_config(self, yaml_data: DictConfig | ListConfig) -> DictConfig | ListConfig:
    #     if isinstance(yaml_data.approximation_type, str):
    #         yaml_data.approximation_type = ApproximationType(yaml_data.approximation_type.lower())
    #     return yaml_data

    # def _get_dataset_config(self) -> DatasetConfig:
    #     yaml_data_common = OmegaConf.load(get_root_path() / self.args.dataset_config)
    #     yaml_data_common.type_ = self.__name_to_type(yaml_data_common.name)

    #     cdc = OmegaConf.structured(CommonDatasetConfig)
    #     cdc.merge_with(yaml_data_common)

    #     if cdc.name.lower() == "csbm":
    #         yaml_data_detail = OmegaConf.load(get_root_path() / yaml_data_common.detail_config)
    #         if isinstance(yaml_data_detail.edge_p_type, str):
    #             yaml_data_detail.edge_p_type = CSBMEdgeProbabilityType(yaml_data_detail.edge_p_type)
    #         ddc = OmegaConf.structured(CSBMConfig)
    #         ddc.merge_with(yaml_data_detail)
    #     else:
    #         ddc = None
    #     return DataConfig(common=cdc, detail=ddc)

    # def __auto_exp_name(self, name: str) -> str:
    #     """Generate a unique experiment name based on the current time."""
    #     if name == "auto":
    #         now = datetime.now(tz=ZoneInfo("Asia/Tokyo"))
    #         name = now.strftime("%Y-%m-%dT%H:%M:%S")
    #     return name

    # def __auto_detect_gpu(self, gpu_id: int) -> str:
    #     """Automatically detect the device to use."""
    #     if torch.cuda.is_available() and (0 <= gpu_id < torch.cuda.device_count()):
    #         return f"cuda:{gpu_id}"
    #     else:
    #         return "cpu"

    # def __name_to_type(self, name: str) -> DatasetType:
    #     """Convert dataset name to DatasetType enum."""
    #     if name.lower() == "csbm":
    #         return DatasetType.RANDOM_SBM
    #     else:
    #         raise NotImplementedError
    ...  # TODO
