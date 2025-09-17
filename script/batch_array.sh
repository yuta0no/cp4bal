#!/bin/bash

budget=1
round=35

cd $(git rev-parse --show-toplevel)/script

for method in "random" "approximate_uncertainty"
do
    for seed in 31 45 52 94 318
    do
        sbatch job.sh $seed $method $budget $round
    done
done
