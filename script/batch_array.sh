#!/bin/bash

budget=16
round=6

cd $(git rev-parse --show-toplevel)/script

for seed in 28 69 72 85 116 31 41 52 94 318
do
    for method in "coreset_feature" "degree" "energy" "entropy" "least_confidence" "margin"
    do
        sbatch job.sh $seed $method $budget $round config/dataset/csbm-18.yaml config/model/bayes_optimal.yaml
    done
done
