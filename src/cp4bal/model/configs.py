from dataclasses import dataclass, field

from .enums import ApproximationType, BayesianPrediction, ModelName
from .trainer.configs import TrainerConfig


@dataclass(kw_only=True)
class ModelConfig:
    name: ModelName = ModelName.MISSING
    trainer: TrainerConfig = field(default_factory=TrainerConfig)


@dataclass(kw_only=True)
class MultipleSampleModelConfig(ModelConfig):
    """Configuration to support drawing from multiple samples."""

    num_samples_train: int = 1
    num_samples_eval: int = 20


@dataclass(kw_only=True)
class MCDropoutModelConfig(MultipleSampleModelConfig):
    """Configuration for models that sample using MC dropout."""

    dropout_at_eval: bool = True
    dropout_p: float = 0.5


@dataclass(kw_only=True)
class BaseGCNConfig(ModelConfig):
    hidden_dims: list[int] = field(default_factory=lambda: (64,))
    add_self_loops: bool = True
    cached = True
    improved = False  # If True, sets self-weight to 2
    inplace: bool = False  # If True, uses inplace ReLU


@dataclass(kw_only=True)
class GCNConfig(MCDropoutModelConfig, BaseGCNConfig):
    name: ModelName = ModelName.GCN


@dataclass(kw_only=True)
class SGCConfig(BaseGCNConfig):
    name: ModelName = ModelName.SGC
    k: int = 2
    inverse_regularization_strength: float = 1.0
    balanced: bool = True


@dataclass(kw_only=True)
class BayesianLikelihoodConfig:
    use_features: bool = True
    use_adjacency: bool = True
    use_non_edges: bool = True


@dataclass(kw_only=True)
class BayesOptimalConfig(ModelConfig):
    name: ModelName = ModelName.BAYES_OPTIMAL
    approximation_type: ApproximationType = ApproximationType.VARIATIONAL_INFERENCE
    batch_size: int = 100_000  # How many samples (labelings) to process in one numpy array
    num_samples: int = 100
    importance_prob: float = 0.9
    normalized: bool = True
    cached: bool = True

    predict_train: bool = True  # if set, predicts with 100% confidence the true label for train nodes
    prediction: BayesianPrediction = BayesianPrediction.MARGINAL
    prediction_likelihood: BayesianLikelihoodConfig = field(default_factory=BayesianLikelihoodConfig)
    confidence_likelihood: BayesianLikelihoodConfig = field(default_factory=BayesianLikelihoodConfig)

    # Beam search parameters
    beam_width: int = 1000
    beam_search_num_iterations: int = 10

    # Variational inference parameters
    vi_max_iterations: int = 2000
    vi_convergence_tolerance: float = 1e-4
