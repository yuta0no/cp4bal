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

csbm18_b4_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:00:28-d2c1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:00:34-7064/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:00:42-45f1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:00:50-8ea4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:02-eada/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:11-bcf2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:16-2f39/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:33-91aa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:36-0471/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/degree/2025-12-29T17:01:46-4620/result.csv",
    ]
)

csbm18_b4_energy= ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:00:28-9b07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:00:34-56d2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:00:54-4726/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:00:55-ea13/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:04-ebbe/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:11-bd43/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:17-0415/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:33-1499/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:38-f7c5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/energy/2025-12-29T17:01:55-c8cf/result.csv",
    ]
)

csbm18_b4_entropy= ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:00:31-5fa5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:00:34-b119/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:00:49-baaf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:00:52-c48c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:06-7640/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:23-f95d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:24-fefd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:33-d5d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:38-2c56/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/entropy/2025-12-29T17:01:51-e4d0/result.csv",
    ]
)

csbm18_b4_least_confidence= ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:00:29-3e8c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:00:36-9149/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:00:50-921b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:00:54-53e5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:08-94da/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:15-ef89/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:27-d94f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:33-bf12/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:51-c1cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/least_confidence/2025-12-29T17:01:55-1d72/result.csv",
    ]
)

csbm18_b4_margin= ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:00:29-1025/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:00:40-f4a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:00:50-5eba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:00:55-21a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:11-01d8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:14-ab4b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:26-f70d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:36-493f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:43-a5be/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/margin/2025-12-29T17:01:55-a78b/result.csv",
    ]
)

csbm18_b4_us= ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:00-ab6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:06-736b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:06-eb57/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:21-7f47/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:23-ea33/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:24-ee03/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:30-aab8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:42-c5c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:46-afc8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty/2025-12-29T16:55:50-e79e/result.csv",
    ]
)

csbm18_b4_usp= ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:01-1c42/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:02-cb76/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:08-c4dd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:23-901b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:24-b502/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:26-3784/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:36-9c9b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:43-eccc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:46-d9d1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/oracle_uncertainty_cp/2025-12-29T16:55:47-92a9/result.csv",
    ]
)

csbm18_b4_random= ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:06-05ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:11-ad46/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:14-7081/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:23-6199/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:26-0c1a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:35-2773/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:43-9372/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:44-a1a0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:50-1d18/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/4/random/2025-12-29T16:55:50-d3ca/result.csv",
    ]
)

csbm18_b8_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:21-ad5c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:23-6dd3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:35-e3ff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:37-60b8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:47-a873/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T16:59:50-ca79/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T17:00:04-d2a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T17:00:09-3784/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T17:00:12-5d5a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/degree/2025-12-29T17:00:19-588b/result.csv",
    ]
)

csbm18_b8_energy= ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:22-8b96/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:24-667a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:35-cc0e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:40-7132/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:48-59b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T16:59:56-b084/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T17:00:01-7f59/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T17:00:06-1d80/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T17:00:12-21ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/energy/2025-12-29T17:00:20-fcad/result.csv",
    ]
)

csbm18_b8_entropy= ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:24-1b73/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:31-3b11/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:40-5df3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:47-0863/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:49-c52a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T16:59:56-74a6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T17:00:02-3c03/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T17:00:09-0013/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T17:00:15-9781/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/entropy/2025-12-29T17:00:22-842e/result.csv",
    ]
)

csbm18_b8_least_confidence= ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:22-7001/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:30-2ea9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:36-ae3f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:39-42d3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:47-5407/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T16:59:56-bdcf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T17:00:04-63e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T17:00:12-25b1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T17:00:15-b617/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/least_confidence/2025-12-29T17:00:33-6628/result.csv",
    ]
)

csbm18_b8_margin= ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:21-4a0c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:31-fca3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:36-9121/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:43-6f02/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:50-3c12/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T16:59:56-43ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T17:00:05-597c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T17:00:12-77ff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T17:00:19-c5f7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/margin/2025-12-29T17:00:24-8492/result.csv",
    ]
)

csbm18_b8_us= ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:04-3ca9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:08-9d99/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:08-5535/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:09-4f68/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:18-2439/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:18-e077/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:24-2bd4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:25-b2f1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:31-6c56/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty/2025-12-29T16:56:36-83d6/result.csv",
    ]
)

csbm18_b8_usp= ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:55:59-0b19/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:04-5051/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:11-017b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:11-793a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:17-5516/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:27-c4dd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:30-2eba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:31-b9e0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:33-0d40/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/oracle_uncertainty_cp/2025-12-29T16:56:38-68d1/result.csv",
    ]
)

csbm18_b8_random= ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:03-850f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:06-ed49/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:09-0811/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:13-3b69/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:16-c2de/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:23-7f79/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:30-dd22/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:32-0cca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:34-bad2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/8/random/2025-12-29T16:56:38-0025/result.csv",
    ]
)

csbm18_b12_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:01:53-4c16/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:04-2455/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:10-9333/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:14-e5c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:24-d796/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:31-9718/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:35-b4b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:38-f15f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:02:44-73e9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/degree/2025-12-29T17:03:03-ef4f/result.csv",
    ]
)

csbm18_b12_energy= ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:01:58-f9a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:04-79e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:14-1c50/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:17-7888/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:23-41bd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:31-063d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:34-9141/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:41-6235/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:44-56cb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/energy/2025-12-29T17:02:54-e959/result.csv",
    ]
)

csbm18_b12_entropy= ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:02-439c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:07-1dba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:14-233b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:17-1b72/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:24-bc1d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:30-2c90/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:34-aba8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:45-7d07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:47-0730/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/entropy/2025-12-29T17:02:52-170d/result.csv",
    ]
)

csbm18_b12_least_confidence= ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:02-3d28/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:16-721b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:17-1411/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:20-eee8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:27-9660/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:36-b667/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:43-e3a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:45-3d17/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:45-ed97/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/least_confidence/2025-12-29T17:02:55-ca0c/result.csv",
    ]
)

csbm18_b12_margin= ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:04-7f6f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:11-4c93/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:17-f62a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:23-ea1d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:31-ce07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:31-f714/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:39-e13f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:45-e2a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:51-43a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/margin/2025-12-29T17:02:55-733a/result.csv",
    ]
)

csbm18_b12_us= ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:45-0a2d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:45-bf9c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:45-eee7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:52-800a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:56-a4ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:56:58-e550/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:57:04-52a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:57:08-28dd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:57:12-1ad7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty/2025-12-29T16:57:12-c7af/result.csv",
    ]
)

csbm18_b12_usp= ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:42-985a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:46-4d67/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:46-eb6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:53-9b75/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:58-9e86/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:56:59-6dff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:57:03-a244/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:57:08-4df7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:57:13-757f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/oracle_uncertainty_cp/2025-12-29T16:57:20-777a/result.csv",
    ]
)

csbm18_b12_random= ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:43-c844/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:50-9857/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:55-b5e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:55-e376/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:58-ff3d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:56:59-a958/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:57:06-7e14/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:57:07-0d06/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:57:09-51d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/12/random/2025-12-29T16:57:11-9d0a/result.csv",
    ]
)

csbm18_b16_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:01-5382/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:04-141e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:06-d92a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:16-b682/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:24-cd1b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:27-7a24/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:28-b2e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:34-d2f9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:38-8989/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/degree/2025-12-29T17:03:43-fa83/result.csv",
    ]
)

csbm18_b16_energy= ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:01-7b68/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:05-9777/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:11-e506/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:12-0030/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:18-769e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:24-2de0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:36-f865/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:40-4827/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:44-b593/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/energy/2025-12-29T17:03:46-bca5/result.csv",
    ]
)

csbm18_b16_entropy= ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:01-b2c6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:05-c551/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:14-1200/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:15-6001/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:22-1ee3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:25-1715/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:33-3e96/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:37-86ec/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:37-a693/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/entropy/2025-12-29T17:03:47-62da/result.csv",
    ]
)

csbm18_b16_least_confidence= ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:00-d148/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:05-3d0f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:14-35b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:15-aa06/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:24-e6a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:27-38ea/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:31-760d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:40-aea2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:44-56b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/least_confidence/2025-12-29T17:03:50-6daf/result.csv",
    ]
)

csbm18_b16_margin= ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:02:59-5495/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:06-e0ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:14-71bd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:15-a861/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:25-90a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:27-bf7d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:34-aeb5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:40-2678/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:43-aa7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/margin/2025-12-29T17:03:55-73da/result.csv",
    ]
)

csbm18_b16_us= ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:16-dc02/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:19-4bec/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:24-55e7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:26-693e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:30-2d21/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:31-6843/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:36-f464/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:37-e4ac/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:41-a7d9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty/2025-12-29T16:57:48-4bfb/result.csv",
    ]
)

csbm18_b16_usp= ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:18-0862/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:19-016c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:26-b1c3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:28-3ec1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:34-5e8b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:40-2a36/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:40-57b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:40-ebd9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:42-b65d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/oracle_uncertainty_cp/2025-12-29T16:57:52-e82f/result.csv",
    ]
)

csbm18_b16_random= ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:18-33f8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:23-e09f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:27-302a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:30-0224/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:31-df94/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:40-5c82/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:40-e815/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:41-7672/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:44-3fdd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-18/bayes_optimal/16/random/2025-12-29T16:57:52-501c/result.csv",
    ]
)

csbm19_b1_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-07T23:53:48-e5a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-07T23:53:59-026a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T00:25:50-675d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T00:40:43-033a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T01:11:07-d370/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T01:26:15-b764/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T01:57:44-64c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T02:17:09-63d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T02:40:28-3894/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty/2026-01-08T02:58:34-1ef0/result.csv",
    ]
)

csbm19_b2_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T03:24:30-5a75/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T03:40:55-ec1d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T03:51:38-bf21/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:03:26-5d5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:14:00-9e5b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:24:52-2053/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:36:57-a8e8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:45:14-735c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T04:54:53-90bc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty/2026-01-08T05:06:22-3553/result.csv",
    ]
)

csbm19_b48_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:18:47-9d52/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:19:39-4356/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:20:19-60d7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:21:14-16c0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:21:41-e4de/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:22:07-6213/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:22:54-815a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:23:34-ea12/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:24:12-1ca0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty/2026-01-08T07:24:42-74bc/result.csv",
    ]
)

csbm19_b64_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:25:27-c169/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:26:02-1033/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:26:43-3539/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:27:14-94ab/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:27:55-fc2f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:28:17-1fff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:28:56-d9a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:29:28-17a6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:29:57-7447/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty/2026-01-08T07:30:27-75f3/result.csv",
    ]
)

csbm19_b96_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:31:05-57f7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:31:40-d676/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:32:08-6f74/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:32:27-38b8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:33:01-b0d0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:33:25-7803/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:33:53-6df7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:34:23-f1df/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:34:43-20f7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty/2026-01-08T07:35:13-c6ea/result.csv",
    ]
)

csbm19_b1_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-07T23:53:48-b524/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-07T23:53:59-e0eb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T00:29:14-66ce/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T00:42:05-436a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T01:15:54-eca0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T01:27:09-3d7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T01:59:20-c1fd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T02:18:01-55d3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T02:42:26-f7c3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/1/oracle_uncertainty_cp/2026-01-08T02:59:19-fb20/result.csv",
    ]
)

csbm19_b2_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T03:25:29-6e1b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T03:42:17-6151/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T03:51:47-5544/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:05:22-4b34/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:15:20-7040/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:25:22-3f2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:38:08-5763/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:46:29-f1b3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T04:56:13-d33f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/2/oracle_uncertainty_cp/2026-01-08T05:08:52-f3db/result.csv",
    ]
)

csbm19_b48_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:19:00-47e5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:19:48-3633/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:20:20-6732/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:21:02-0c66/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:21:46-f9d2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:22:12-20a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:23:06-3302/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:23:34-a222/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:24:22-c276/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/48/oracle_uncertainty_cp/2026-01-08T07:25:09-6b47/result.csv",
    ]
)

csbm19_b64_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:25:34-165c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:26:10-c58d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:26:45-6f5b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:27:15-f714/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:27:50-c900/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:28:21-b49d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:28:53-cf87/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:29:31-077e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:30:01-7d7f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/64/oracle_uncertainty_cp/2026-01-08T07:30:28-fff4/result.csv",
    ]
)

csbm19_b96_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:31:07-ca14/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:31:43-5313/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:32:13-1d6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:32:28-e7db/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:33:03-d2ed/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:33:29-6fe4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:33:56-3e22/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:34:26-e067/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:34:53-3e49/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/96/oracle_uncertainty_cp/2026-01-08T07:35:19-75b1/result.csv",
    ]
)

csbm19_b4_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:25:28-2f7a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:30:39-a878/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:38:21-5511/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:39:48-d8d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:46:46-abad/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:53:40-7b5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T05:56:03-7a3b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T06:02:50-0f87/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T06:06:46-ff1a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/degree/2026-01-08T06:12:19-4e79/result.csv",
    ]
)

csbm19_b4_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:24:28-031d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:29:59-4b68/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:35:44-2add/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:39:33-cf9a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:46:29-6dee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:50:20-49a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T05:55:53-b4c5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T06:03:01-091c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T06:06:26-141a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/energy/2026-01-08T06:11:53-5799/result.csv",
    ]
)

csbm19_b4_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:22:48-0fa3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:29:06-a59b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:34:01-8c01/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:39:14-b168/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:45:13-fe48/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:49:20-8069/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T05:55:42-527e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T06:01:21-b111/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T06:05:29-90b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/entropy/2026-01-08T06:11:01-560d/result.csv",
    ]
)

csbm19_b4_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:20:12-2112/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:28:05-d62f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:31:44-6f17/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:39:09-fac3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:43:56-905c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:48:52-f488/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:55:12-0b56/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T05:58:49-95a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T06:04:14-dbf9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/least_confidence/2026-01-08T06:09:15-8fee/result.csv",
    ]
)

csbm19_b4_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:21:49-3edf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:29:19-325a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:31:56-5691/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:39:10-4a85/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:44:10-d2d4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:49:11-4ea7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T05:55:37-9338/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T06:01:05-9277/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T06:05:10-e7ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/margin/2026-01-08T06:10:50-0bee/result.csv",
    ]
)

csbm19_b4_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:13:29-8fbf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:26:43-2580/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:30:41-30b4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:38:33-cd30/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:42:21-32ee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:46:52-a754/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:53:28-c23c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T05:56:06-0948/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T06:03:15-7ea0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty/2026-01-08T06:06:45-f382/result.csv",
    ]
)

csbm19_b4_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:14:31-1579/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:27:52-ea7f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:31:15-25a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:39:10-1552/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:42:24-a220/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:47:17-5a7a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:54:12-491d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T05:56:13-7d4a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T06:03:36-3a19/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/oracle_uncertainty_cp/2026-01-08T06:08:07-541c/result.csv",
    ]
)

csbm19_b4_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:18:35-51cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:28:04-7095/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:31:17-d7cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:39:08-6dbb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:42:32-43e1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:47:27-74d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:55:05-b29d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T05:58:10-e7b9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T06:03:51-c41e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/4/random/2026-01-08T06:08:48-e4ab/result.csv",
    ]
)

csbm19_b8_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:17:48-2c4b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:21:13-321f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:23:05-1fba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:25:56-6e38/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:29:09-9013/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:32:08-1275/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:33:59-96b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:37:31-a46d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:39:12-7a73/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/degree/2026-01-08T06:42:43-c344/result.csv",
    ]
)

csbm19_b8_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:17:03-9c09/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:20:37-df51/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:23:07-8f10/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:26:04-996e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:28:37-6077/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:31:43-f89a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:33:52-074c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:37:27-fc47/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:39:02-761d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/energy/2026-01-08T06:41:59-bbbb/result.csv",
    ]
)

csbm19_b8_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:16:02-e2f5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:19:48-3dd4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:22:38-016c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:25:35-1cb7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:28:50-12b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:31:11-7472/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:33:48-4f79/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:37:09-1831/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:39:02-f11a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/entropy/2026-01-08T06:41:54-740b/result.csv",
    ]
)

csbm19_b8_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:15:36-1e38/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:19:12-209b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:22:02-df26/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:25:26-2a13/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:27:49-49e5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:29:44-39c5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:33:38-ee80/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:35:47-1052/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:38:27-cfd7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/least_confidence/2026-01-08T06:41:48-f26e/result.csv",
    ]
)

csbm19_b8_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:16:08-84e5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:19:46-b86f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:22:11-e1bf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:25:32-10e6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:27:52-80bb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:30:41-e6ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:33:46-d3ea/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:36:14-b8b9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:38:33-6503/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/margin/2026-01-08T06:41:49-2852/result.csv",
    ]
)

csbm19_b8_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:13:24-2eb7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:18:01-b266/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:21:03-c651/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:23:28-689f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:26:02-d90b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:29:10-f758/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:32:46-42be/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:34:04-5492/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:37:52-76e6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty/2026-01-08T06:39:51-6dae/result.csv",
    ]
)

csbm19_b8_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:13:11-7589/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:18:31-42d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:21:40-36d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:24:46-808e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:26:14-0591/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:29:10-b069/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:32:53-dac3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:34:38-5622/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:38:21-2d8b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/oracle_uncertainty_cp/2026-01-08T06:39:46-45da/result.csv",
    ]
)

csbm19_b8_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:13:56-fb27/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:19:11-29c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:21:47-16de/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:24:50-e540/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:27:27-31ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:29:24-1b5c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:33:02-7681/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:35:35-5d59/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:38:21-a558/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/8/random/2026-01-08T06:41:33-aa78/result.csv",
    ]
)

csbm19_b16_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:45:22-3b5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:46:57-ac5a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:48:13-67c1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:50:10-171f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:51:19-fd2e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:53:01-36d0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:54:56-0fc2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:55:40-0dc2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:57:34-e4c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/degree/2026-01-08T06:58:23-8dc5/result.csv",
    ]
)

csbm19_b16_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:44:59-9c30/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:46:45-849c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:48:13-8afe/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:49:35-a267/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:51:35-1dd7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:52:59-6a7e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:54:16-8b4a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:55:26-efaf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:57:30-1369/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/energy/2026-01-08T06:58:14-9016/result.csv",
    ]
)

csbm19_b16_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:44:58-99e9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:46:26-b30e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:48:30-9cf2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:49:29-8437/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:51:04-453b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:52:26-fc6c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:54:12-e355/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:55:25-60c1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:57:31-5c85/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/entropy/2026-01-08T06:58:12-77b2/result.csv",
    ]
)

csbm19_b16_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:44:22-4013/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:46:08-fdbb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:48:00-590a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:49:09-8afe/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:51:05-4c3e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:51:49-9a73/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:54:01-d89e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:55:12-4ecc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:56:35-8d60/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/least_confidence/2026-01-08T06:58:08-34cd/result.csv",
    ]
)

csbm19_b16_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:44:32-efe3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:46:12-e304/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:48:14-80a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:49:12-d96b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:51:05-cef1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:52:12-a7f1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:54:04-b07e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:55:20-6bc6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:56:50-cb8f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/margin/2026-01-08T06:58:05-de6e/result.csv",
    ]
)

csbm19_b16_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:42:43-bccb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:45:17-6862/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:47:08-39e6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:48:20-26d1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:50:06-5069/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:51:28-0e42/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:53:21-fe9d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:54:46-da6a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:55:48-47ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty/2026-01-08T06:57:39-d77c/result.csv",
    ]
)

csbm19_b16_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:43:26-2842/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:45:29-aff1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:47:24-b1c7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:48:31-e3fb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:50:20-7799/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:51:37-ec46/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:53:21-6cb4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:55:01-5326/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:56:25-b2a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/oracle_uncertainty_cp/2026-01-08T06:57:39-1932/result.csv",
    ]
)

csbm19_b16_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:44:03-a81c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:45:50-c56a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:47:57-81f0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:48:36-d4b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:50:28-4222/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:51:48-8145/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:53:21-86b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:55:06-4777/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:56:24-1750/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/16/random/2026-01-08T06:58:06-3134/result.csv",
    ]
)

csbm19_b24_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:00:24-31ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:01:21-3924/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:02:34-a6a6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:03:36-44ca/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:04:54-7f45/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:06:02-0b2c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:06:52-2940/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:08:04-5d25/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:08:33-8db7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/degree/2026-01-08T07:09:57-3917/result.csv",
    ]
)

csbm19_b24_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:00:23-0f32/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:01:18-95a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:02:10-6aa2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:03:24-55fd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:04:28-1d4b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:05:32-4d29/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:06:41-f43d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:07:50-8ac2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:08:33-25c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/energy/2026-01-08T07:09:34-4c95/result.csv",
    ]
)

csbm19_b24_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T06:59:56-a0c5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:01:12-baed/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:02:24-d247/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:03:40-e33a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:04:14-1a18/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:05:07-201b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:06:34-84c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:07:25-1ecc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:08:32-742c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/entropy/2026-01-08T07:09:32-87b6/result.csv",
    ]
)

csbm19_b24_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T06:59:33-3e58/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:01:07-3ca4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:01:54-5128/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:03:08-fae3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:04:00-751e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:05:01-4b61/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:06:24-f03b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:07:05-1ea5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:08:23-f01e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/least_confidence/2026-01-08T07:09:21-4800/result.csv",
    ]
)

csbm19_b24_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T06:59:50-43ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:01:03-8fd3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:01:59-88a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:03:08-7236/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:04:10-03fe/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:05:04-aa89/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:06:34-9115/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:07:12-8422/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:08:28-9ce9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/margin/2026-01-08T07:09:19-a75a/result.csv",
    ]
)

csbm19_b24_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T06:58:51-518b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:00:24-7c90/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:01:29-89f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:02:32-5e8a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:03:48-2233/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:04:40-8c37/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:06:13-c712/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:07:14-1ddf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:08:23-1a7a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty/2026-01-08T07:09:10-e975/result.csv",
    ]
)

csbm19_b24_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T06:59:03-1434/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:01:05-a57e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:01:38-2eb9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:02:45-81a8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:03:58-7d58/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:04:42-ef3f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:06:12-43d4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:07:02-f919/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:08:18-46d3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/oracle_uncertainty_cp/2026-01-08T07:09:13-3f8e/result.csv",
    ]
)

csbm19_b24_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T06:59:52-63fc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:00:53-7967/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:01:48-a553/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:02:57-81fa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:04:00-6c3a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:05:01-fc14/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:06:17-6cbb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:07:01-c446/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:08:18-0768/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/24/random/2026-01-08T07:09:37-928b/result.csv",
    ]
)

csbm19_b32_degree = ResultPaths(
    name="degree",
    method=ALM.DEGREE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:11:07-50ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:11:55-746f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:12:49-6edf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:13:38-1b94/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:14:33-7268/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:15:24-32ff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:16:02-1b35/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:17:07-77df/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:17:47-cbcb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/degree/2026-01-08T07:18:33-14fe/result.csv",
    ]
)

csbm19_b32_energy = ResultPaths(
    name="energy",
    method=ALM.ENERGY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:10:52-5f21/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:11:49-da54/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:12:43-0dc6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:13:35-257d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:14:07-87ea/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:15:37-1cf3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:15:56-276b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:17:04-bce1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:17:38-edcd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/energy/2026-01-08T07:18:31-70a6/result.csv",
    ]
)

csbm19_b32_entropy = ResultPaths(
    name="entropy",
    method=ALM.ENTROPY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:11:11-53d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:11:48-80b3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:12:23-8810/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:13:33-eec8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:14:25-1ab2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:15:15-f6d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:15:51-2c69/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:16:50-e0b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:17:36-7623/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/entropy/2026-01-08T07:18:31-5559/result.csv",
    ]
)

csbm19_b32_least_confidence = ResultPaths(
    name="least_confidence",
    method=ALM.LEAST_CONFIDENCE,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:10:43-a5ff/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:11:35-4937/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:12:11-889f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:13:21-169e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:13:55-4e74/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:14:44-75af/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:15:47-b9be/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:16:35-a053/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:17:38-eb04/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/least_confidence/2026-01-08T07:18:18-4c4d/result.csv",
    ]
)

csbm19_b32_margin = ResultPaths(
    name="margin",
    method=ALM.MARGIN,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:10:39-0bc1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:11:37-dc6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:12:17-e4e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:13:23-c34d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:13:59-3231/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:15:07-bb5b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:15:49-f636/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:16:49-4563/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:17:27-510d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/margin/2026-01-08T07:18:37-1706/result.csv",
    ]
)

csbm19_b32_us = ResultPaths(
    name="uncertainty",
    method=ALM.ORACLE_UNCERTAINTY,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:09:58-da19/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:11:11-9199/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:12:15-57d1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:12:53-948f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:13:50-d92c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:14:34-7fcd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:15:33-ce95/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:16:44-6ec4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:17:07-b2ab/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty/2026-01-08T07:18:04-d8bd/result.csv",
    ]
)

csbm19_b32_usp = ResultPaths(
    name="uncertainty propagation",
    method=ALM.ORACLE_UNCERTAINTY_CP,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:10:13-7ff4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:11:20-9f5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:12:04-e851/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:13:17-3023/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:13:52-39a2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:14:41-455c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:15:40-241b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:16:28-aee1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:17:10-c6b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/oracle_uncertainty_cp/2026-01-08T07:18:08-4726/result.csv",
    ]
)

csbm19_b32_random = ResultPaths(
    name="random",
    method=ALM.RANDOM,
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:10:25-30e9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:11:33-1c62/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:12:12-3362/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:13:11-45ee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:13:52-bd01/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:14:41-9f0a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:15:40-7e7f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:16:34-1e9a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:17:25-f700/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm-19/bayes_optimal/32/random/2026-01-08T07:18:14-c8ae/result.csv",
    ]
)
