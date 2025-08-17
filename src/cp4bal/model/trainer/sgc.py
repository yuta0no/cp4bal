import torch

from cp4bal.dataset import ActiveLearningDataset, DatasetSplit, GraphData

from ..sgc import SGC
from .base import Trainer
from .configs import SGCTrainerConfig


class SGCTrainer(Trainer):
    def __init__(
        self, config: SGCTrainerConfig, model: SGC, dataset: ActiveLearningDataset, generator: torch.Generator
    ):
        super().__init__(config, model, dataset, generator)
        self.model = model

    def fit(self):
        """Fits the model to a dataset.

        Args:
            model (BaseModel): The model to fit
            dataset (Dataset): The dataset to fit to
            generator (torch.Generator): A random number generator
            acquisition_step (int): Which acquisition step it is

        Returns:
            Result: Metrics, etc. for this model fit
        """
        batch: GraphData = self.dataset.data
        mask_train = batch.get_mask(DatasetSplit.TRAIN_L)

        x = self.model.get_diffused_node_features(batch)[mask_train]
        labels_in_mask_train = torch.unique(batch.y[mask_train])
        if labels_in_mask_train.size(0) == 1:
            # "Bug" in sklearn's LogisticRegressionClassifier: It can not fit with only one class in the training set
            # Therefore we "hardcode" a constant prediction of 1.0 for this class into the classifier
            # via its 'frozen_prediction' feature
            self.model.freeze_predictions(labels_in_mask_train[0].item())
        else:
            self.model.unfreeze_predictions()
            self.model.logistic_regression.fit(x.numpy(), batch.y[mask_train].numpy())
