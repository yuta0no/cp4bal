from enum import StrEnum
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

from plot.constant import FIG_DIR

# Constants
result_dir = Path("/home/members/ono/workspace/cp4bal/out/mean_field_error/")
exp_name = "csbm_n20_k2_snr1.2_d8_seed42"
EXP_DIR = result_dir / exp_name


class NodeLabel(StrEnum):
    LABELED = "L"
    QUERY = "Q"
    UNLABELED = ""


def main():
    fig_dir = FIG_DIR / "mean_field_error"
    fig_dir.mkdir(parents=True, exist_ok=True)

    result_dict = np.load(EXP_DIR / "results.npz")

    plot_scatter(
        log_Rs=result_dict["log_Rs"],
        mean_field_log_Rs=result_dict["mean_field_log_Rs"],
        fig_dir=fig_dir,
    )

    plot_graph_with_error(
        L_nodes=result_dict["L_nodes"],
        U_nodes=result_dict["U_nodes"],
        Q_nodes=result_dict["Q_nodes"],
        edges=np.load(EXP_DIR / "edge_indices.npy").T,
        gt_labels=np.load(EXP_DIR / "gt_labels.npy"),
        errors=result_dict["log_Rs"] - result_dict["mean_field_log_Rs"],
        fig_dir=fig_dir,
    )

    plot_graph_with_exact_logR(
        L_nodes=result_dict["L_nodes"],
        U_nodes=result_dict["U_nodes"],
        Q_nodes=result_dict["Q_nodes"],
        edges=np.load(EXP_DIR / "edge_indices.npy").T,
        gt_labels=np.load(EXP_DIR / "gt_labels.npy"),
        log_Rs=result_dict["log_Rs"],
        fig_dir=fig_dir,
    )


def plot_scatter(log_Rs, mean_field_log_Rs, fig_dir):
    fig, ax = plt.subplots()
    ax.scatter(log_Rs, mean_field_log_Rs, marker="o", s=49, alpha=1.0, color="blue", edgecolors="black", linewidths=0.5)
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

    fig.savefig(fig_dir / f"{exp_name}_corr.png", dpi=300)


def plot_graph_with_error(L_nodes, U_nodes, Q_nodes, edges, gt_labels, errors, fig_dir):
    import networkx as nx

    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(range(len(gt_labels)))

    node_class_0 = [i for i, label in enumerate(gt_labels) if label == 0]
    node_class_1 = [i for i, label in enumerate(gt_labels) if label == 1]
    abs_err_max = np.max(np.abs(errors))
    errors_all = np.zeros(len(gt_labels))
    for i, n in enumerate(U_nodes):
        errors_all[n] = errors[i]

    for n in Q_nodes:
        errors_all[n] = 0.0

    node_errors_0 = [abs(errors_all[n]) for n in node_class_0]
    node_errors_1 = [abs(errors_all[n]) for n in node_class_1]

    pos = nx.spring_layout(G, seed=42, k=0.5)

    plt.figure(figsize=(8, 8))
    node_labels = {}
    for node in G.nodes():
        if node in L_nodes:
            node_labels[node] = NodeLabel.LABELED.value
        elif node in Q_nodes:
            node_labels[node] = NodeLabel.QUERY.value
        else:
            node_labels[node] = NodeLabel.UNLABELED.value

    cmap = plt.cm.OrRd
    vmin = 0.0
    vmax = abs_err_max
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=node_class_0,
        node_color=node_errors_0,
        node_shape="o",
        edgecolors="black",
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        node_size=300,
    )
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=node_class_1,
        node_color=node_errors_1,
        edgecolors="black",
        node_shape="s",
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        node_size=300,
    )
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color="black")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=colors.Normalize(vmin=vmin, vmax=vmax))
    sm.set_array([])
    ax = plt.gca()
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("Abs Err", fontsize=18)
    cbar.ax.tick_params(labelsize=14)
    ax.set_axis_off()
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(fig_dir / f"{exp_name}_graph_error.png", dpi=300)


def plot_graph_with_exact_logR(L_nodes, U_nodes, Q_nodes, edges, gt_labels, log_Rs, fig_dir):
    import networkx as nx

    G = nx.Graph()
    G.add_edges_from(edges)
    G.add_nodes_from(range(len(gt_labels)))

    node_class_0 = [i for i, label in enumerate(gt_labels) if label == 0]
    node_class_1 = [i for i, label in enumerate(gt_labels) if label == 1]
    vmin = np.min(log_Rs)
    vmax = np.max(log_Rs)
    log_R_all = np.zeros(len(gt_labels))
    for i, n in enumerate(U_nodes):
        log_R_all[n] = log_Rs[i]

    for n in Q_nodes:
        log_R_all[n] = 0.0

    node_values_0 = [log_R_all[n] for n in node_class_0]
    node_values_1 = [log_R_all[n] for n in node_class_1]

    pos = nx.spring_layout(G, seed=42, k=0.5)

    plt.figure(figsize=(8, 8))
    node_labels = {}
    for node in G.nodes():
        if node in L_nodes:
            node_labels[node] = NodeLabel.LABELED.value
        elif node in Q_nodes:
            node_labels[node] = NodeLabel.QUERY.value
        else:
            node_labels[node] = NodeLabel.UNLABELED.value

    if vmax > 0 > vmin:
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=vmax)
    elif vmin >= 0:
        norm = colors.TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
    else:
        norm = colors.TwoSlopeNorm(vmin=vmin, vcenter=0, vmax=-vmin)
    cmap = plt.cm.RdBu
    node_colors_0 = [cmap(norm(v)) for v in node_values_0]
    node_colors_1 = [cmap(norm(v)) for v in node_values_1]

    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=node_class_0,
        node_color=node_colors_0,
        node_shape="o",
        edgecolors="black",
        node_size=300,
    )
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=node_class_1,
        node_color=node_colors_1,
        edgecolors="black",
        node_shape="s",
        node_size=300,
    )
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color="black")
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    ax = plt.gca()
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("exact log R", fontsize=18)
    cbar.ax.tick_params(labelsize=14)
    ax.set_axis_off()
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(fig_dir / f"{exp_name}_graph_logR.png", dpi=300)


if __name__ == "__main__":
    main()