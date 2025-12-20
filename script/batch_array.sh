#!/bin/bash

budget=12
round=4

cd $(git rev-parse --show-toplevel)/script

# for seed in 31 41 52 94 318
for seed in 28 69 72 85 116 31 41 52 94 318
do
    for method in "oracle_uncertainty" "oracle_uncertainty_cp" "random"
    do
        sbatch job.sh $seed $method $budget $round config/dataset/csbm-11.yaml config/model/bayes_optimal.yaml
    done
done
