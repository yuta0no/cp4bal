import matplotlib.pyplot as plt

from plot.constant import FIG_DIR
from plot.results import *
from plot.utils import get_n_continuous_colors, load_results

TARGET_RESULTS = [
    b_sensitivity_csbm2_b1_marginal,
    b_sensitivity_csbm2_b2_marginal,
    b_sensitivity_csbm2_b3_marginal,
    b_sensitivity_csbm2_b4_marginal,
    b_sensitivity_csbm2_b6_marginal,
    b_sensitivity_csbm2_b8_marginal,
    b_sensitivity_csbm2_b12_marginal,
    b_sensitivity_csbm2_b16_marginal,
    b_sensitivity_csbm2_b24_marginal,
]
FIG_NAME = "b_sensitivity_csbm2.png"


def main():
    fig, ax = plt.subplots()
    cs = get_n_continuous_colors(len(TARGET_RESULTS), cmap_name="inferno")
    for result_paths, color in zip(TARGET_RESULTS, cs):
        name, budgets, means, _ = load_results(result_paths)
        ax.plot(budgets, means, marker="o", label=name, color=color)

    ax.set_xlabel("#annotation")
    ax.set_ylabel("accuracy")
    ax.legend()
    (FIG_DIR / "accuracy").mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / "accuracy" / FIG_NAME)


if __name__ == "__main__":
    main()
