import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import compute_auc_from_budgets_and_means, load_results, method_to_color, method_to_linestyle

TARGET_RESULTS = [
    csbm5_b12_random_marginal,
    csbm5_b12_us_marginal,
    csbm5_b12_usp_marginal
]
FIG_NAME = "csbm5_budget12.png"

SHOW_STD = False


def main():
    fig, ax = plt.subplots()
    for result_paths in TARGET_RESULTS:
        name, budgets, means, stds = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        ax.plot(
            budgets, means,
            label=f"{name} (AUC: {auc:.4f})",
            marker="o",
            color=method_to_color(result_paths.method),
            linestyle=method_to_linestyle(result_paths.method)
        )
        if SHOW_STD:
            ax.fill_between(
                budgets,
                [m - s for m, s in zip(means, stds)],
                [m + s for m, s in zip(means, stds)],
                alpha=0.2,
            )

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
