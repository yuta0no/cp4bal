from copy import copy

from .types_ import ActiveLearningMethod as ALM
from .types_ import ResultPaths

csbm5_b4_random_marginal = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:00:57-3346/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:01:09-e8f3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:01:21-badf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:01:42-51b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:01:46-084c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:02:07-12ab/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:02:10-b04f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:02:20-19c2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:02:26-6bc3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/random/2025-12-06T15:02:43-3f26/result.csv",
    ]
)

csbm5_b4_us_marginal = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:00:57-3fc3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:00:57-69f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:01:11-56c4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:01:28-5fc4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:01:46-cfa2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:01:50-4c45/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:02:08-5251/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:02:18-4baf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:02:30-3429/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:02:43-1055/result.csv",
    ]
)

csbm5_b4_usp_marginal = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:27-d83d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:28-c3dd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:35-fd23/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:38-0c46/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:39-b033/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:42-74e8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:42-9927/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:42-d136/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:42-e42f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/4/oracle_uncertainty/2025-12-06T15:28:43-854b/result.csv",
    ]
)

csbm5_b8_random_marginal = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:02:59-2a42/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:00-37e1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:10-73f4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:19-229b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:27-220a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:28-81cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:40-816e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:51-c0a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:54-4b02/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/random/2025-12-06T15:03:58-e364/result.csv",
    ]
)

csbm5_b8_us_marginal = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:02:48-97a1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:02:57-8102/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:10-74df/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:14-10c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:28-5e67/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:30-ce76/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:36-de06/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:39-4675/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:52-4513/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty/2025-12-06T15:03:54-4606/result.csv",
    ]
)

csbm5_b8_usp_marginal = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:28:58-6554/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:28:59-7f9c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:28:59-8c56/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:28:59-a544/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:01-6d9a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:01-2663/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:01-e3c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:01-e611/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:02-69c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/8/oracle_uncertainty_cp/2025-12-06T00:29:02-768a/result.csv",
    ]
)

csbm5_b12_random_marginal = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:07-cae5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:17-9cf6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:19-e788/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:30-4150/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:34-1120/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:39-e3f3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:45-a52b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:53-bc32/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:57-f41c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/random/2025-12-06T15:04:58-8c01/result.csv",
    ]
)

csbm5_b12_us_marginal = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:01-1838/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:08-ebf0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:17-241d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:31-c54f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:34-4984/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:42-03d0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:44-c5f7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:47-fc09/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:52-5fa7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty/2025-12-06T15:04:58-6abc/result.csv",
    ]
)

csbm5_b12_usp_marginal = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:02-a4e8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:03-62ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:04-3f77/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:04-c61f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:05-a720/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:06-774f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:06-cdd8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:07-927a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:08-c97b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-5/bayes_optimal/12/oracle_uncertainty_cp/2025-12-06T00:29:08-ff01/result.csv",
    ]
)

coraml_b1_sgc_us_w_leftout = ResultPaths(
    name="with left-out nodes",
    method=ALM.APPROXIMATE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-09T23:01:52-e42d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-09T23:01:53-f8c6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-09T23:02:10-ae62/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-09T23:02:32-0373/result.csv",
    ]
)

coraml_b1_sgc_us_wo_leftout = ResultPaths(
    name="without left-out nodes",
    method=ALM.APPROXIMATE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-15T17:50:39-f0f4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-15T17:50:22-72fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-15T17:49:22-e14c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/cora_ml/sgc/1/approximate_uncertainty_cp/2025-12-15T17:49:22-c36c/result.csv",
    ]
)


from .results_b_sensitivity import (
    b_sensitivity_csbm10_b4,
    b_sensitivity_csbm10_b8,
    b_sensitivity_csbm10_b12,
    b_sensitivity_csbm10_b24
)
csbm10_b4_usp = copy(b_sensitivity_csbm10_b4)
csbm10_b4_usp.name = "uncertainty propagation"
csbm10_b8_usp = copy(b_sensitivity_csbm10_b8)
csbm10_b8_usp.name = "uncertainty propagation"
csbm10_b12_usp = copy(b_sensitivity_csbm10_b12)
csbm10_b12_usp.name = "uncertainty propagation"
csbm10_b24_usp = copy(b_sensitivity_csbm10_b24)
csbm10_b24_usp.name = "uncertainty propagation"


from .results_b_sensitivity import (
    b_sensitivity_csbm10_b4_wocp,
    b_sensitivity_csbm10_b8_wocp,
    b_sensitivity_csbm10_b12_wocp,
    b_sensitivity_csbm10_b24_wocp
)
csbm10_b4_us = copy(b_sensitivity_csbm10_b4_wocp)
csbm10_b4_us.name = "uncertainty"
csbm10_b8_us = copy(b_sensitivity_csbm10_b8_wocp)
csbm10_b8_us.name = "uncertainty"
csbm10_b12_us = copy(b_sensitivity_csbm10_b12_wocp)
csbm10_b12_us.name = "uncertainty"
csbm10_b24_us = copy(b_sensitivity_csbm10_b24_wocp)
csbm10_b24_us.name = "uncertainty"


csbm10_b4_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:43:58-6f08/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:43:59-334c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:43:59-f722/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:05-4646/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:05-ee7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:06-b78d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:08-6eb0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:13-1766/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:14-68aa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/4/random/2025-12-20T13:44:18-2721/result.csv",
    ]
)

csbm10_b8_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:17-83d2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:20-02b4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:20-9125/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:26-f4f1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:27-3fd1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:27-76a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:31-b7ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:33-fd6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:34-6e02/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/8/random/2025-12-20T13:44:35-c4ae/result.csv",
    ]
)

csbm10_b12_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:19-654d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:22-647a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:22-f575/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:26-1831/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:30-fd40/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:31-0bdb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:31-7cbc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:33-2f6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:40:36-820e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/12/random/2025-12-20T13:41:23-cc5c/result.csv",
    ]
)

csbm10_b24_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:13-ad4f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:13-c71f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:14-43f1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:21-9950/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:21-d928/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:22-1da7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:27-8432/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:28-037e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:12:28-ebb1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-10/bayes_optimal/24/random/2025-12-20T14:13:14-c2b9/result.csv",
    ]
)

csbm11_b1_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:43:47-97a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:43:53-83e3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:44:21-a573/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:44:31-3aa5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:45:30-2989/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:46:58-29b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:47:05-473b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:47:06-985b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:47:17-d10b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/random/2025-12-20T14:48:57-7295/result.csv",
    ]
)

csbm11_b2_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:40:25-75b8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:40:29-6fd0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:40:59-e089/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:41:21-6d25/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:41:42-128a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:41:57-b26e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:42:12-0db1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:42:35-90b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:42:51-7695/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/random/2025-12-20T14:43:10-2655/result.csv",
    ]
)

csbm11_b3_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:38:02-06c6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:38:06-4c64/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:38:17-3649/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:38:47-3362/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:39:11-8bb5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:39:12-476a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:39:17-121a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:39:37-fbbf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:39:54-8f74/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/random/2025-12-20T14:40:15-09f2/result.csv",
    ]
)

csbm11_b4_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:36:11-7744/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:36:22-52b9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:36:22-ef0e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:36:38-971f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:37:04-f442/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:37:06-9ac3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:37:15-9eff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:37:17-f385/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:37:48-d6d3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/random/2025-12-20T14:38:00-90bb/result.csv",
    ]
)

csbm11_b6_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:34:48-8caf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:34:56-8587/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:00-f73f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:03-90b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:29-4561/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:31-7210/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:33-5530/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:43-6517/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:35:47-a5d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/random/2025-12-20T14:36:09-d335/result.csv",
    ]
)

csbm11_b8_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:33:42-504f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:33:43-0294/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:33:52-82f3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:33:59-4e38/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:08-e3cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:15-4bab/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:16-f44b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:31-750e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:35-a28c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/random/2025-12-20T14:34:46-e929/result.csv",
    ]
)

csbm11_b12_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:32:40-608f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:32:47-ba50/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:32:50-5422/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:32:59-e773/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:05-e90b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:11-f5d4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:15-2d63/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:22-bc15/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:31-7b3e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/random/2025-12-20T14:33:31-75ba/result.csv",
    ]
)

csbm11_b16_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:31:44-1bb5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:31:48-3245/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:31:59-e74c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:03-a315/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:05-7908/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:19-b1e8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:23-af08/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:23-ecd5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:39-19cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/random/2025-12-20T14:32:40-3b5e/result.csv",
    ]
)

csbm11_b24_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:30:54-0d7f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:30:55-b7e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:30:56-029a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:11-162d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:15-7990/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:17-78ed/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:27-f442/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:32-67cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:40-8404/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/random/2025-12-20T14:31:59-ec4f/result.csv",
    ]
)


csbm11_b1_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:43:10-2175/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:43:46-a476/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:44:08-e2fb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:44:16-dbf3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:44:39-6799/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:46:17-792f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:46:59-35f8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:47:02-0c63/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:47:08-dbac/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty/2025-12-20T14:47:52-c9b3/result.csv",
    ]
)

csbm11_b2_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:40:15-7d6c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:40:27-8482/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:40:30-f0ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:40:59-8d00/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:41:21-0bbb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:41:45-6ead/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:42:07-fcc3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:42:17-acf3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:42:35-8929/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty/2025-12-20T14:43:00-ca3e/result.csv",
    ]
)

csbm11_b3_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:38:06-d5c5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:38:06-f058/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:38:06-f190/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:38:33-bf6a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:38:48-9469/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:39:11-08ea/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:39:13-b9ac/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:39:17-2156/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:39:49-52b9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty/2025-12-20T14:40:07-afe8/result.csv",
    ]
)

csbm11_b4_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:36:10-22e1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:36:10-bac5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:36:20-7b6f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:36:22-2519/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:36:43-e583/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:37:04-849d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:37:07-15ac/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:37:15-0111/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:37:19-9c29/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty/2025-12-20T14:37:55-7a0c/result.csv",
    ]
)

csbm11_b6_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:34:47-c02c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:34:50-8818/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:04-2a35/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:04-b889/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:12-0214/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:30-c1e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:31-39df/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:37-cc04/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:35:43-35e8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty/2025-12-20T14:36:02-7e7b/result.csv",
    ]
)

csbm11_b8_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:33:40-1b67/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:33:42-a47e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:33:46-942e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:33:52-54af/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:33:59-b721/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:34:10-3b81/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:34:15-6898/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:34:19-a965/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:34:31-1fe8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty/2025-12-20T14:34:35-b7eb/result.csv",
    ]
)

csbm11_b12_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:32:40-623c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:32:42-1679/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:32:48-4a64/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:00-91c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:04-db71/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:06-59dc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:13-e448/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:17-7cca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:23-490e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty/2025-12-20T14:33:29-6f24/result.csv",
    ]
)

csbm11_b16_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:31:40-1491/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:31:48-f6aa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:31:50-178d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:00-b071/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:06-4802/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:07-96bc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:20-25fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:23-184d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:27-2e0a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty/2025-12-20T14:32:40-bea0/result.csv",
    ]
)

csbm11_b24_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:30:55-79fb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:30:56-b9da/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:30:57-2be3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:11-5f18/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:12-9063/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:16-a177/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:21-43f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:27-19e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:33-58f2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty/2025-12-20T14:31:59-b8fb/result.csv",
    ]
)


csbm11_b1_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:43:17-4f81/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:43:49-ab38/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:44:08-dfdb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:44:21-56c4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:45:17-35a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:46:36-7c68/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:47:04-d1c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:47:06-566e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:47:21-1439/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/1/oracle_uncertainty_cp/2025-12-20T14:48:48-7517/result.csv",
    ]
)

csbm11_b2_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:40:17-fd2b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:40:28-0e1a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:40:42-dfca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:41:04-0267/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:41:17-2917/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:41:50-974d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:42:08-7155/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:42:26-d04a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:42:51-f8ad/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/2/oracle_uncertainty_cp/2025-12-20T14:43:10-42fb/result.csv",
    ]
)

csbm11_b3_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:38:01-29e3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:38:04-ab5f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:38:14-f8e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:38:42-434c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:38:55-61b4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:39:11-f2a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:39:15-744a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:39:29-a26e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:39:52-1ae4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/3/oracle_uncertainty_cp/2025-12-20T14:40:15-cd51/result.csv",
    ]
)

csbm11_b4_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:36:10-6c8e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:36:10-c1de/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:36:17-6619/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:36:33-4b6a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:02-5d6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:06-7d33/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:15-294a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:18-4b2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:27-703a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/4/oracle_uncertainty_cp/2025-12-20T14:37:55-efd3/result.csv",
    ]
)

csbm11_b6_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:34:48-c583/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:34:50-472c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:02-ee1f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:04-7f28/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:17-bf3d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:30-4994/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:33-9ce5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:43-363e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:35:45-0c79/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/6/oracle_uncertainty_cp/2025-12-20T14:36:05-8bb1/result.csv",
    ]
)

csbm11_b8_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:33:39-55c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:33:42-59bb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:33:47-814e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:33:58-43a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:08-c2a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:13-fe1a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:17-edfa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:22-02b3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:31-f307/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/8/oracle_uncertainty_cp/2025-12-20T14:34:35-2f99/result.csv",
    ]
)

csbm11_b12_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:32:40-8a5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:32:46-43b2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:32:50-de73/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:00-c455/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:04-8d51/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:11-7bb6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:15-45d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:20-bacc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:31-6e98/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/12/oracle_uncertainty_cp/2025-12-20T14:33:32-003e/result.csv",
    ]
)

csbm11_b16_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:31:41-0657/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:31:47-58b2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:31:52-a0d2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:02-1e0c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:05-eea4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:17-768e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:21-32be/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:24-aa3d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:28-e138/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/16/oracle_uncertainty_cp/2025-12-20T14:32:40-70d0/result.csv",
    ]
)

csbm11_b24_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:30:54-414f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:30:56-9469/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:30:57-e765/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:11-cd8d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:15-9132/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:17-95aa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:27-c8da/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:30-32fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:40-cf49/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-11/bayes_optimal/24/oracle_uncertainty_cp/2025-12-20T14:31:59-42e9/result.csv",
    ]
)

# CSBM-17
from .results_b_sensitivity import (
    b_sensitivity_csbm17_b8,
    b_sensitivity_csbm17_b8_wocp,
)
csbm17_b8_usp = copy(b_sensitivity_csbm17_b8)
csbm17_b8_usp.name = "uncertainty propagation"

csbm17_b8_us = copy(b_sensitivity_csbm17_b8_wocp)
csbm17_b8_us.name = "uncertainty"

csbm17_b8_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:53-22a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:57-4ab0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:57-4cfd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:57-7ef7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:57-3497/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:12:57-b00f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:13:12-88e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:14:00-94b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:14:00-534e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/degree/2025-12-29T16:14:00-fd44/result.csv",
    ]
)

csbm17_b8_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:14:58-7285/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:00-3ca7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:00-6bb7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:01-9140/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:01-b8fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:01-d3e6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:15:15-f2cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:16:04-31cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:16:04-9036/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/energy/2025-12-29T14:16:04-f419/result.csv",
    ]
)

csbm17_b8_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:34-1a11/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:36-7ee6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:36-ac03/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:37-0d43/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:37-3a72/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:37-22e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:40:37-e506/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:41:39-b50b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:41:39-de11/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/entropy/2025-12-29T11:42:04-41a4/result.csv",
    ]
)

csbm17_b8_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:42-b73e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:44-099f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:47-e00c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:50-233f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:51-6a7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:51-2729/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:55-5f19/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:56-61a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:57-7e45/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/random/2025-12-28T15:02:59-dfff/result.csv",
    ]
)

csbm17_b8_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:38:59-6fd4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:01-014b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:02-412d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:02-a115/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:02-f257/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:03-2034/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:06-bb92/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:39:17-b9bd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:40:04-47c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/least_confidence/2025-12-29T13:40:04-94b3/result.csv",
    ]
)

csbm17_b8_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:12-94c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:13-4018/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:14-a2bb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:16-3aba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:16-5f8b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:16-d0ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:17-e53e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:18-08f7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:18-62ec/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-17/bayes_optimal/8/margin/2025-12-29T12:07:31-877d/result.csv",
    ]
)
