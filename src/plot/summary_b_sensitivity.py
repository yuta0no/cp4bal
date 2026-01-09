import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from plot.constant import FIG_DIR
from plot.results import *  # noqa: F403
from plot.utils import (
    compute_auc_from_budgets_and_means,
    load_results_with_seed,
)

EXTS = ["png", "pdf"]

BASELINE_RESULTS = {
    1: auc_diff_csbm18_b1_us,
    2: auc_diff_csbm18_b2_us,
    4: auc_diff_csbm18_b4_us,
    8: auc_diff_csbm18_b8_us,
    12: auc_diff_csbm18_b12_us,
    16: auc_diff_csbm18_b16_us,
    24: auc_diff_csbm18_b24_us,
    32: auc_diff_csbm18_b32_us,
    48: auc_diff_csbm18_b48_us,
    96: auc_diff_csbm18_b96_us,
    # 192: auc_diff_csbm19_b192_us,
}

TARGET_RESULTS = {
    1: auc_diff_csbm18_b1_usp,
    2: auc_diff_csbm18_b2_usp,
    4: auc_diff_csbm18_b4_usp,
    8: auc_diff_csbm18_b8_usp,
    12: auc_diff_csbm18_b12_usp,
    16: auc_diff_csbm18_b16_usp,
    24: auc_diff_csbm18_b24_usp,
    32: auc_diff_csbm18_b32_usp,
    48: auc_diff_csbm18_b48_usp,
    96: auc_diff_csbm18_b96_usp,
    # 192: auc_diff_csbm18_b192_usp,
}


FIG_NAME = "csbm18-100"
SHOW_STD = True
SHOW_MINMAX = False

def main():
    fig_mean, ax_mean = plt.subplots(figsize=(8, 6))
    fig_swarm, ax_swarm = plt.subplots(figsize=(8, 6))

    auc_diff_values_all = {}
    auc_diff_mean_all = {}
    auc_diff_std_all = {}
    auc_diff_max_all = {}
    auc_diff_min_all = {}

    for budget_size, baseline_result_paths in BASELINE_RESULTS.items():
        baseline_results = load_results_with_seed(baseline_result_paths)
        target_results = TARGET_RESULTS[budget_size]
        auc_diff_list = []

        target_results = load_results_with_seed(target_results)
        for seed, target_data in target_results.items():
            baseline_data = baseline_results[seed]
            target_auc = compute_auc_from_budgets_and_means(
                target_data["num_labeled_nodes"].tolist(), target_data["accuracy"].tolist()
            )
            baseline_auc = compute_auc_from_budgets_and_means(
                baseline_data["num_labeled_nodes"].tolist(), baseline_data["accuracy"].tolist()
            )
            auc_diff = target_auc - baseline_auc
            auc_diff_list.append(auc_diff)

        auc_diff_values_all[budget_size] = auc_diff_list
        auc_diff_array = np.array(auc_diff_list)
        mean_auc_diff = np.mean(auc_diff_array)
        std_auc_diff = np.std(auc_diff_array)
        max_auc_diff = np.max(auc_diff_array)
        min_auc_diff = np.min(auc_diff_array)
        auc_diff_mean_all[budget_size] = mean_auc_diff
        auc_diff_std_all[budget_size] = std_auc_diff
        auc_diff_max_all[budget_size] = max_auc_diff
        auc_diff_min_all[budget_size] = min_auc_diff

    budget_sizes = sorted(auc_diff_mean_all.keys(), key=lambda x: x)
    mean_values = [auc_diff_mean_all[size] for size in budget_sizes]
    auc_diff_values_all_list = [auc_diff_values_all[size] for size in budget_sizes]
    std_values = [auc_diff_std_all[size] for size in budget_sizes]
    max_values = [auc_diff_max_all[size] for size in budget_sizes]
    min_values = [auc_diff_min_all[size] for size in budget_sizes]

    ax_mean.plot(
        budget_sizes,
        mean_values,
        marker="o",
        linestyle="-",
        color="blue",
        label="AUC Difference (Target - Baseline)",
        linewidth=3,
        markersize=8,
    )
    if SHOW_STD:
        ax_mean.fill_between(
            budget_sizes,
            np.array(mean_values) - np.array(std_values),
            np.array(mean_values) + np.array(std_values),
            color="blue",
            alpha=0.2,
        )
    if SHOW_MINMAX:
        ax_mean.fill_between(
            budget_sizes,
            min_values,
            max_values,
            color="red",
            alpha=0.1,
        )
    ax_mean.set_xlabel("Budget Size", fontsize=16)
    ax_mean.set_ylabel("AUC Difference", fontsize=16)
    # ax_mean.set_xticks(budget_sizes)
    # ax_mean.set_xticklabels(budget_sizes, fontsize=14)
    ax_mean.set_xticks([1, 8, 16, 24, 32, 48, 96, 192])
    ax_mean.set_xticklabels([1, 8, 16, 24, 32, 48, 96, 192], fontsize=14)
    ax_mean.tick_params(axis="y", labelsize=14)
    ax_mean.hlines(0, xmin=min(budget_sizes), xmax=max(budget_sizes), linestyle="--", color="black", linewidth=2)
    ax_mean.set_xlim(min(budget_sizes), max(budget_sizes))
    fig_mean.tight_layout()
    (FIG_DIR / "auc_diff").mkdir(parents=True, exist_ok=True)
    for ext in EXTS:
        fig_mean.savefig(FIG_DIR / "auc_diff" / f"{FIG_NAME}.{ext}", dpi=300)

    sns.stripplot(data=auc_diff_values_all_list, ax=ax_swarm, size=4, color="black")
    ax_swarm.plot(
        range(len(budget_sizes)),
        mean_values,
        marker="x",
        linestyle="-",
        color="blue",
        label="Mean AUC Difference",
        linewidth=3,
        markersize=8,
    )
    ax_swarm.fill_between(
        range(len(budget_sizes)),
        np.array(mean_values) - np.array(std_values),
        np.array(mean_values) + np.array(std_values),
        color="blue",
        alpha=0.2,
    )
    ax_swarm.set_xticks(range(len(budget_sizes)))
    ax_swarm.set_xticklabels(budget_sizes)
    ax_swarm.set_xlabel("Budget Size", fontsize=16)
    ax_swarm.set_ylabel("AUC Difference", fontsize=16)
    ax_swarm.tick_params(axis="y", labelsize=14)
    ax_swarm.hlines(0, xmin=-0.5, xmax=len(budget_sizes) - 0.5, linestyle="--", color="black", linewidth=2)
    fig_swarm.tight_layout()
    for ext in EXTS:
        fig_swarm.savefig(FIG_DIR / "auc_diff" / f"{FIG_NAME}_swarm.{ext}", dpi=300)

if __name__ == "__main__":
    main()
