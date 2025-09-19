#!/bin/bash

acquisition_name="random"

for seed in 31 45 52 94 318
do
    uv run src/cp4bal/main.py --seed $seed --acquisition_name $acquisition_name --budget 1 --round 30
done
