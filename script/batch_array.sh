#!/bin/bash

budget=24
round=2

cd $(git rev-parse --show-toplevel)/script

# for seed in 31 41 52 94 318
for seed in 28 69 72 85 116 31 41 52 94 318
do
    for method in "oracle_uncertainty"
    do
        sbatch job.sh $seed $method $budget $round config/dataset/csbm-5.yaml config/model/bayes_optimal.yaml
    done
done
