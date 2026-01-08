import traceback
from itertools import product
from logging import getLogger
from pathlib import Path

import numpy as np

from cp4bal.dataset.configs import CommonDatasetConfig, CSBMConfig, DatasetConfig, EdgeProbabilityType
from cp4bal.dataset.factory import DatasetFactory
from cp4bal.util.logger import init_stream_logger
from cp4bal.util.seed import set_seed

logger = getLogger(__name__)
OUT_DIR = Path(__file__).parent.parent.parent / "out" / "mean_field_error"


def main():
    # dataset
    N = 16  # num nodes
    K = 3  # num classes
    SNR = 3.0  # signal to noise ratio
    D = 4  # expected degree
    for seed in [13, 42, 89, 1942, 2001]:
        set_seed(seed)
        init_stream_logger()
        logger.info("started")
        logger.info("seed: %d", seed)
        output_dir = OUT_DIR / f"csbm_n{N}_k{K}_snr{SNR}_d{D}_seed{seed}"
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info("output_dir: %s", output_dir.resolve())
        config = DatasetConfig(
            common=CommonDatasetConfig(
                name="csbm",
                val_size=0,
                test_size=0,
            ),
            detail=CSBMConfig(
                seed=seed,
                num_nodes=N,
                num_classes=K,
                dim_features=5,
                feature_sigma=1.0,
                feature_class_mean_distance=1.0,
                edge_p_type=EdgeProbabilityType.BY_SNR_AND_DEGREE,
                p_edge_intra=None,
                p_edge_inter=None,
                edge_p_snr=SNR,
                expected_degree=D,
            ),
        )
        base_ds = DatasetFactory.create(config=config)
        x = base_ds.node_features
        gt_labels = base_ds.labels
        np.save(output_dir / "gt_labels.npy", gt_labels.numpy())
        np.save(output_dir / "node_features.npy", x.numpy())
        np.save(output_dir / "edge_indices.npy", base_ds.edge_indices)

        # logger.info(f"CSBM Graph created: {base_ds.edge_indices}")
        logger.info("labels: %s", gt_labels.tolist())

        labeled_nodes = {0, 1, N - 2, N - 1}  # L
        Q_nodes = {2, 3, N - 3}  # Q
        unlabeled_nodes = set(range(N)) - labeled_nodes  # U

        q_ids = []
        R_denominators = []
        R_numerators = []
        log_Rs = []
        mean_field_log_Rs = []
        logger.info(f"{base_ds.p_edge_inter=}")
        logger.info(f"{base_ds.p_edge_intra=}")

        mean_field_log_R_const = _calculate_log_R_constant_term(
            labels=gt_labels,
            p_inter=base_ds.p_edge_inter,
            p_intra=base_ds.p_edge_intra,
            K=K,
            Q_nodes=list(Q_nodes),
            L_nodes=list(labeled_nodes),
            edges=base_ds.edge_indices.clone().cpu().T.tolist(),
        )

        for q in unlabeled_nodes:
            print("Processing node:", q)
            q_ids.append(q)
            T_nodes = unlabeled_nodes - Q_nodes - {q}
            # S_nodes = labeled_nodes | {q}
            QT_nodes = Q_nodes | T_nodes

            T_nodes = list(T_nodes)
            QT_nodes = list(QT_nodes)

            labels_SQ = gt_labels.clone().unsqueeze(0).numpy()
            labels_S = gt_labels.clone().unsqueeze(0).numpy()

            v_d = 0.0
            v_n = 0.0

            for allocation in product(list(range(K)), repeat=len(Q_nodes) + len(T_nodes)):
                allocation = np.array(allocation, dtype=int)
                labels_SQ[0, T_nodes] = allocation[: len(T_nodes)]  # for P(A | y_S, y_Q)
                labels_S[0, QT_nodes] = allocation  # for P(A | y_S)

                v_n += np.exp(
                    base_ds.conditional_log_likelihood(
                        y=labels_SQ, x=x, use_adjacency=True, use_features=False, use_non_edges=True
                    )
                ) / (K ** (len(Q_nodes) + len(T_nodes)))
                v_d += np.exp(
                    base_ds.conditional_log_likelihood(
                        y=labels_S, x=x, use_adjacency=True, use_features=False, use_non_edges=True
                    )
                ) / (K ** (len(Q_nodes) + len(T_nodes)))

            log_R_q = (np.log(v_n) - np.log(v_d)).item()
            R_numerators.append(v_n.item())
            R_denominators.append(v_d.item())
            log_Rs.append(log_R_q)

            mean_field_log_R_q = (
                _calculate_log_R_by_mean_field_approximation(
                    labels=gt_labels,
                    p_inter=base_ds.p_edge_inter,
                    p_intra=base_ds.p_edge_intra,
                    K=K,
                    Q_nodes=list(Q_nodes),
                    i=q,
                    edges=base_ds.edge_indices.clone().cpu().T.tolist(),
                )
                + mean_field_log_R_const
            )
            mean_field_log_Rs.append(mean_field_log_R_q)

            logger.debug(f"q: {q}, log_R_q: {log_R_q}, mean_field_log_R_q: {mean_field_log_R_q}, v_n: {v_n}, v_d: {v_d}")
            logger.debug(f"error: {log_R_q - mean_field_log_R_q}")

        np.savez(
            file=output_dir / "results.npz",
            q=np.array(q_ids),
            R_numerators=np.array(R_numerators),
            R_denominators=np.array(R_denominators),
            log_Rs=np.array(log_Rs),
            mean_field_log_Rs=np.array(mean_field_log_Rs),
            U_nodes=np.array(list(unlabeled_nodes)),
            Q_nodes=np.array(list(Q_nodes)),
            L_nodes=np.array(list(labeled_nodes)),
        )


def _calculate_log_R_constant_term(*, labels, p_inter, p_intra, K, Q_nodes, L_nodes, edges):
    """compute the constant term in log R"""
    ret = 0
    for i in L_nodes:
        ret += _calculate_log_R_by_mean_field_approximation(
            labels=labels,
            p_inter=p_inter,
            p_intra=p_intra,
            K=K,
            Q_nodes=Q_nodes,
            i=i,
            edges=edges,
        )
    return ret


def _calculate_log_R_by_mean_field_approximation(*, labels, p_inter, p_intra, K, Q_nodes, i, edges):
    p = p_intra
    q = p_inter

    log_p = np.log(p)
    log_1mp = np.log(1 - p)
    log_q = np.log(q)
    log_1mq = np.log(1 - q)
    expected_pq = np.log((p + (K - 1) * q) / K)
    expected_1mpq = np.log(((1 - p) + (K - 1) * (1 - q)) / K)

    # edges: Int[Tensor, "e 2"] = dataset.base.edge_indices.clone().cpu().T.tolist()
    edge_set = set(tuple(e) for e in edges) | set(tuple(e) for e in edges[::-1])
    u_label = labels[i]
    a_same = 0  # connected and same label
    a_diff = 0  # connected and different label
    b_same = 0  # not connected and same label
    b_diff = 0  # not connected and different label
    for v in Q_nodes:
        v_label = labels[v]
        has_edge = (i, v) in edge_set
        if v_label == u_label:
            if has_edge:
                a_same += 1
            else:
                b_same += 1
        else:
            if has_edge:
                a_diff += 1
            else:
                b_diff += 1

    cp_value = (
        a_same * log_p
        + b_same * log_1mp
        + a_diff * log_q
        + b_diff * log_1mq
        - (a_same + a_diff) * expected_pq
        - (b_same + b_diff) * expected_1mpq
    )
    return cp_value


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e

    logger.info("finished")
