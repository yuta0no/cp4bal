#!/bin/bash

budget=7
round=5

cd $(git rev-parse --show-toplevel)/script

for seed in 31 45 52 94 318
do
    for method in "oracle_uncertainty" "random"
    do
        sbatch job.sh $seed $method $budget $round
    done
done
