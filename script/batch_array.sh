#!/bin/bash

budget=1
round=7

cd $(git rev-parse --show-toplevel)/script

for seed in 31 41 52 94 318
# for seed in 28 69 72 85 116 31 41 52 94 318
do
    for method in "approximate_uncertainty" "random"
    do
        sbatch job.sh $seed $method $budget $round config/dataset/cora_ml.yaml config/model/sgc.yaml
    done
done
