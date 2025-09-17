#!/bin/bash

acquisition_name="random"

for seed in 16 31 42 45 52 80 94 167 318 552
# for seed in 16
do
    uv run src/cp4bal/main.py --seed $seed --acquisition_name $acquisition_name --budget 1 --round 20
done
