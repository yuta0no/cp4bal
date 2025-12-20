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
