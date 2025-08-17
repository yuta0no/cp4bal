from enum import StrEnum, unique


@unique
class ModelName(StrEnum):
    BAYES_OPTIMAL = "bayes_optimal"
    GCN = "gcn"
    SGC = "sgc"


@unique
class ApproximationType(StrEnum):
    BRUTE_FORCE = "brute_force"
    LIKELIHOOD_CACHE = "likelihood_cache"
    MONTE_CARLO = "monte_carlo"
    LAZY_MC = "lazy_monte_carlo"
    IMPORTANCE = "importance"
    BEAM_SEARCH = "beam_search"
    CACHED_BEAM_SEARCH = "cached_beam_search"
    VARIATIONAL_INFERENCE = "variational_inference"


@unique
class BayesianPrediction(StrEnum):
    # predict by maximzing p(y_i = c | Y_o, A, X) for each node independently
    MARGINAL = "marginal"

    # predict by maximizing p(y_u | Y_o, A, X) for all unobserved nodes jointly
    JOINT = "joint"

    # predict by maximizing p(y_u | Y_o, A, X) via beam search for all unobserved nodes jointly
    JOINT_BEAM_SEARCH = "joint_beam_search"

    # caches values of unique assignments per beam for a more precise approximation but at a higher memory overhead
    JOINT_CACHED_BEAM_SEARCH = "joint_cached_beam_search"

    # predict by maximizing p(y_u | Y_o, A, X) for all unobserved nodes jointly using the likelihood cache
    JOINT_CACHED_LIKELIHOOD = "joint_cached_likelihood"
