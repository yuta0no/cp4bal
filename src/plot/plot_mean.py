import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import (
    compute_auc_from_budgets_and_means,
    load_results,
    method_to_color,
    method_to_linestyle,
    method_to_marker,
    method_to_name,
)

TARGET_RESULTS = [
    coraml_b1_sgc_us_w_leftout,
    coraml_b1_sgc_us_wo_leftout,
]
FIG_NAME = "leftout_error.png"

SHOW_STD = False

LINESTYLES = ["-", "--", "-.", ":"]

def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, result_paths in enumerate(TARGET_RESULTS):
        name, budgets, means, stds = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        ax.plot(
            budgets, means,
            label=f"{method_to_name(result_paths.method)} (AUC: {auc:.4f})",
            # label=f"{result_paths.name} (AUC: {auc:.4f})",
            marker=method_to_marker(result_paths.method),
            markersize=8,
            color=method_to_color(result_paths.method),
            linestyle=method_to_linestyle(result_paths.method),
            # linestyle=LINESTYLES[i],
            linewidth=3,
        )
        if SHOW_STD:
            ax.fill_between(
                budgets,
                [m - s for m, s in zip(means, stds)],
                [m + s for m, s in zip(means, stds)],
                alpha=0.2,
            )

    ax.set_xlabel("#Annotation", fontsize=18)
    ax.set_ylabel("Accuracy", fontsize=18)
    ax.legend(fontsize=14)
    ax.tick_params(axis="both", labelsize=14)
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
