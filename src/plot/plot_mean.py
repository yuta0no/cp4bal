import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from plot.constant import FIG_DIR
from plot.results import *  # noqa: F403
from plot.types_ import ActiveLearningMethod as ALM
from plot.utils import (
    compute_auc_from_budgets_and_means,
    load_results,
    method_to_color,
    method_to_linestyle,
    method_to_marker,
    method_to_name,
)

TARGET_RESULTS = [
    csbm18_b16_coreset_feature,
    csbm18_b16_coreset_graph,
    csbm18_b16_degree,
    csbm18_b16_energy,
    csbm18_b16_entropy,
    csbm18_b16_usp,
    csbm18_b16_random,
    csbm18_b16_least_confidence,
    csbm18_b16_margin,
]
EXTS = ["png", "pdf"]
FIG_NAME = "csbm18-b16"
SHOW_STD = False
SHOW_AUC = False

def main():
    fig = plt.figure(figsize=(12, 6))
    spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig, wspace=0.05, width_ratios=[8, 2])
    ax = fig.add_subplot(spec[0])
    handle_dict = {}
    for i, result_paths in enumerate(TARGET_RESULTS):
        name, budgets, means, stds = load_results(result_paths)
        label = method_to_name(result_paths.method)
        if SHOW_AUC:
            auc = compute_auc_from_budgets_and_means(budgets, means)
            label = f"{label} (AUC: {auc:.4f})"
        line = ax.plot(
            budgets, means,
            label=label,
            marker=method_to_marker(result_paths.method),
            markersize=12,
            color=method_to_color(result_paths.method),
            linestyle=method_to_linestyle(result_paths.method),
            linewidth=3,
        )
        handle_dict[result_paths.method] = line[0]
        if SHOW_STD:
            ax.fill_between(
                budgets,
                [m - s for m, s in zip(means, stds)],
                [m + s for m, s in zip(means, stds)],
                alpha=0.2,
                color=method_to_color(result_paths.method),
            )

    ax.set_xlabel("#Annotation", fontsize=20)
    ax.set_ylabel("Accuracy", fontsize=20)
    ax.set_xlim(budgets[0], budgets[-1])
    ax.set_xticks(np.linspace(budgets[0], budgets[-1], num=4))

    ax_legend = fig.add_subplot(spec[1])
    ax_legend.axis("off")
    handles = [handle_dict[key] for key in sort_legend_keys(handle_dict)]
    ax_legend.legend(
        handles=handles,
        handlelength=3.0,
        loc="center left",
        borderaxespad=0,
        fontsize=16,
        fancybox=False,
        edgecolor="gray"
    )
    ax.tick_params(axis="both", labelsize=16)
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig_name = FIG_NAME + ("_auc" if SHOW_AUC else "") + ("_std" if SHOW_STD else "")
    for ext in EXTS:
        fig.savefig(FIG_DIR / "accuracy" / f"{fig_name}_accuracy.{ext}", dpi=300)


def sort_legend_keys(handle_dict: dict[ALM, any]) -> list[ALM]:
    order = [
        ALM.ORACLE_UNCERTAINTY_CP,
        ALM.ORACLE_UNCERTAINTY,
        ALM.CORESET_FEATURE,
        ALM.CORESET_GRAPH,
        ALM.DEGREE,
        ALM.ENERGY,
        ALM.ENTROPY,
        ALM.LEAST_CONFIDENCE,
        ALM.MARGIN,
        ALM.RANDOM,
    ]
    return [method for method in order if method in handle_dict]


if __name__ == "__main__":
    main()
