from dataclasses import dataclass

import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.utils import load_results


@dataclass
class ResultPaths:
    name: str
    paths: list[str]


csbm1_random_budget7_round5 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-32e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-48ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:51-f4f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:54-280f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T16:21:54-c29f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:54-0b07/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:54-bd97/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:56-2e53/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:58-f37c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:01:58-fbf8/result.csv",
    ],
)

csbm1_us_budget7_round5 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:34:40-b41c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:34:48-cb4a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:35:06-8e6d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:35:15-bf5d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T16:38:35-6f83/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-3c3b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-8c2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-62a4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:02:22-8248/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T17:03:27-69f2/result.csv",
    ]
)

csbm1_uscp_budget7_round5 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-16b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-4539/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:51-f221/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:54-51ce/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T16:21:54-8974/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:54-ab8a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:56-54b7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:57-3b99/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:58-0c2e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:01:58-a81e/result.csv",
    ]
)

# CSBM-1, Budget=4, Round=9
csbm1_random_budget4_round9 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:12-9549/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-9073/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-c294/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:14-da24/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:15-dcc1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:15-f359/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-05c9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-70e3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-097f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T17:28:18-fac3/result.csv",
    ],
)

csbm1_us_budget4_round9 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:29:07-c0c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:29:07-c83e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-4b8e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-39ec/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-981e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-2597/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-e188/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:30:14-f976/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:46:37-8b7b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T17:46:49-2790/result.csv",
    ]
)

csbm1_uscp_budget4_round9 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:12-efbc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:14-14d6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:14-afa7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:15-51b0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:15-4440/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:16-4e87/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-76b6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-93a5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-2618/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T17:28:18-b575/result.csv",
    ]
)

# CSBM-2, Budget=7, Round=5
csbm2_random_budget7_round5 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-9c7a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-8929/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:44-afd3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:50:47-e2ee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:55:39-b99d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:56:51-1532/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:58:04-ffd7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T17:58:15-e95e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T18:00:59-bcfa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/random/2025-11-19T18:01:23-1845/result.csv",
    ],
)

csbm2_us_budget7_round5 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:01:43-c270/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-5e3c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-8b2a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:14-b6b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:22-79d5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:34-abe4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:35-060e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:36-58a0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:49-f4cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty/2025-11-19T18:02:50-3fbd/result.csv",
    ]
)

csbm2_uscp_budget7_round5 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-3d05/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-b80b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-cc45/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:50:44-f99b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:54:54-0f39/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:56:40-c2ba/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:57:07-301f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:58:11-b2e0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T17:58:35-7261/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/7/oracle_uncertainty_cp/2025-11-19T18:01:17-e010/result.csv",
    ]
)

# CSBM-2, Budget=4, Round=9
csbm2_random_budget4_round9 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-83b5/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-6354/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-b331/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-c9f0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-dabb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:17-ed93/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:20-01d1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:20-2eeb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:20-1973/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T20:00:20-4877/result.csv",
    ],
)

csbm2_us_budget4_round9 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-9bf8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-7922/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-8154/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-a7e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-dd8c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:01:48-f554/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:16:41-a697/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:20:13-98b3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:20:13-b55c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T20:20:13-d3cc/result.csv",
    ]
)

csbm2_uscp_budget4_round9 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:12-7faa/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:17-1f96/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:17-5c54/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:17-6d6b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:17-6fc9/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:17-7ebf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:20-976a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:20-3937/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:20-a4e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T20:00:20-e270/result.csv",
    ]
)

# CSBM-3, Budget=4, Round=10
csbm3_random_budget4_round10 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:26-14cf/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:26-122a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:28-6fcb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:29-12cd/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:29-84a3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:29-df66/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:32-7a74/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:32-8d5e/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:32-dd5c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T21:02:32-e92d/result.csv",
    ],
)

csbm3_us_budget4_round10 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-8ae6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-08c2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-5049/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-a2fb/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-ba37/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:03:30-c6e2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:10:53-9225/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:12:25-51be/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:12:55-7c53/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T21:12:55-9f19/result.csv",
    ]
)

csbm3_uscp_budget4_round10 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:24-04a3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:26-fc8f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:28-6883/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:28-ae0c/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:29-54c8/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:29-a31a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:32-4677/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:32-c5e1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:32-c6af/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T21:02:32-e892/result.csv",
    ]
)

# CSBM-3, Budget=8, Round=5
csbm3_random_budget8_round5 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:29:56-5a61/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:29:56-7b36/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:29:56-ae43/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:29:56-f9ed/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:29:59-3001/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:31:01-2fd0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:31:01-5e27/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:31:01-b77d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:35:26-51f6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/random/2025-11-19T21:35:26-d543/result.csv",
    ],
)

csbm3_us_budget8_round5 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:24-9800/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:30-48b3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:30-abc0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:30-c0a7/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:30-ed58/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:30-fd25/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:33-7010/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:33-ad68/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:33-b9e6/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty/2025-11-19T21:29:33-e33b/result.csv",
    ]
)

csbm3_uscp_budget8_round5 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:29:56-8e35/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:29:56-42ae/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:29:56-b3c3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:29:59-1037/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:29:59-a021/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:31:01-2aa1/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:31:01-b094/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:31:01-c87d/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:33:54-af92/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/8/oracle_uncertainty_cp/2025-11-19T21:35:26-cae7/result.csv",
    ]
)

csbm4_random_budget4_round9 = ResultPaths(
    name="Random",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:08:26-1dda/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:08:56-4835/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:09:57-68cc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:10:27-cca2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:10:58-6d31/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:11:58-b37a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:11:58-c533/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:12:27-64c2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:13:33-39d3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/random/2025-11-19T22:14:02-4090/result.csv",
    ]
)

csbm4_us_budget4_round9 = ResultPaths(
    name="Uncertainty",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:14:25-12e4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:14:31-f153/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:15:32-5a1b/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:17:58-2a5f/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:17:58-5a5a/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:18:27-eaf2/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:18:57-1f16/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:18:57-7d11/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:18:57-0733/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty/2025-11-19T22:18:57-c144/result.csv",
    ]
)

csbm4_uscp_budget4_round9 = ResultPaths(
    name="Uncertainty with CP",
    paths=[
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:08:26-45e0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:08:26-4590/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:08:56-24f3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:10:27-4aee/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:10:28-e2fc/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:10:58-f1d0/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:11:58-4ac3/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:12:28-add4/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:13:33-ee55/result.csv",
        "/home/members/ono/workspace/cp4bal/out/csbm/bayes_optimal/4/oracle_uncertainty_cp/2025-11-19T22:14:02-57b2/result.csv",
    ]
)

TARGET_RESULTS = [csbm4_random_budget4_round9, csbm4_us_budget4_round9, csbm4_uscp_budget4_round9]
FIG_NAME = "csbm4_budget4_round9.png"


def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, stds = load_results(result_paths)
        ax.plot(budgets, means, label=name, marker="o")
        # ax.fill_between(
        #     budgets,
        #     [m - s for m, s in zip(means, stds)],
        #     [m + s for m, s in zip(means, stds)],
        #     alpha=0.2,
        # )

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
