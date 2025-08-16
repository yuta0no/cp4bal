from cp4bal.dataset import CSBM


def main():
    csbm = CSBM()
    print(csbm.class_means)
    print(csbm.edge_indices.shape)


if __name__ == "__main__":
    main()
