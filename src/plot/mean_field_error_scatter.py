from enum import StrEnum
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from plot.constant import FIG_DIR

# Constants
result_dir = Path("/home/members/ono/workspace/cp4bal/out/mean_field_error/")
exp_names = [
    "csbm_n16_k3_snr3.0_d4_seed13",
    "csbm_n16_k3_snr3.0_d4_seed42",
    "csbm_n16_k3_snr3.0_d4_seed89",
    "csbm_n16_k3_snr3.0_d4_seed1942",
    "csbm_n16_k3_snr3.0_d4_seed2001",
]
EXTS = ["png", "pdf"]
cmap = plt.get_cmap("tab10")


class NodeLabel(StrEnum):
    LABELED = "L"
    QUERY = "Q"
    UNLABELED = ""


def main():
    fig_dir = FIG_DIR / "mean_field_error"
    fig_dir.mkdir(parents=True, exist_ok=True)

    plot_scatter_with_multiple_seeds(exp_names=exp_names, fig_dir=fig_dir)


def plot_scatter_with_multiple_seeds(exp_names, fig_dir):
    fig, ax = plt.subplots()
    for i, exp_name in enumerate(exp_names):
        result_dict = np.load(result_dir / exp_name / "results.npz")
        log_Rs = result_dict["log_Rs"]
        mean_field_log_Rs = result_dict["mean_field_log_Rs"]
        ax.scatter(log_Rs, mean_field_log_Rs, marker="o", s=49, alpha=1.0, color=cmap(i), edgecolors="black", linewidths=0.5)
        ax.set_xlabel("Exact log R")
        ax.set_ylabel("Approximate log R")
        lims = [
            np.min([ax.get_xlim(), ax.get_ylim()]),
            np.max([ax.get_xlim(), ax.get_ylim()]),
        ]
        ax.plot(lims, lims, color="black", linestyle="-", alpha=0.75, zorder=0)
    ax.set_aspect("equal")
    ax.set_xlim(lims)
    ax.set_ylim(lims)

    fig_name = exp_names[0].split("_seed")[0] + "_seed" + "_".join(s.split("_seed")[1] for s in exp_names)
    for ext in EXTS:
        fig.savefig(fig_dir / f"{fig_name}_corr.{ext}", dpi=300)


if __name__ == "__main__":
    main()