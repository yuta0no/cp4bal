import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import compute_auc_from_budgets_and_means, get_n_continuous_colors, load_results

# Parameters
TARGET_RESULTS = [
    b_sensitivity_csbm5_b1_marginal,
    b_sensitivity_csbm5_b2_marginal,
    b_sensitivity_csbm5_b3_marginal,
    b_sensitivity_csbm5_b4_marginal,
    b_sensitivity_csbm5_b6_marginal,
    b_sensitivity_csbm5_b8_marginal,
    b_sensitivity_csbm5_b12_marginal,
    b_sensitivity_csbm5_b16_marginal,
    b_sensitivity_csbm5_b24_marginal,
]
FIG_NAME = "b_sensitivity_csbm5.png"

# Consants for plot
Y_MAX = 0.725
Y_MIN = 0.50

def main():
    fig, ax = plt.subplots()
    cs = get_n_continuous_colors(len(TARGET_RESULTS), cmap_name="coolwarm")
    for result_paths, color in zip(TARGET_RESULTS, cs):
        name, budgets, means, _ = load_results(result_paths)
        auc = compute_auc_from_budgets_and_means(budgets, means)
        name = f"{name} (AUC: {auc:.3f})"
        ax.plot(budgets, means, marker="o", label=name, color=color)

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.set_ylim(Y_MIN, Y_MAX)
    ax.legend()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
