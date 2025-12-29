#!/bin/bash

budget=8
round=6

cd $(git rev-parse --show-toplevel)/script

for seed in 28 69 72 85 116 31 41 52 94 318
do
    for method in "least_confidence"
    do
        sbatch job.sh $seed $method $budget $round config/dataset/csbm-17.yaml config/model/bayes_optimal.yaml
    done
done
