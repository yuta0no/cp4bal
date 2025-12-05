#!/bin/bash
#SBATCH --output=/home/members/ono/workspace/cp4bal/jobs/job%j.out  # where to store the output (%j is the JOBID)
#SBATCH --error=/home/members/ono/workspace/cp4bal/jobs/job%j.err  # where to store error messages
#SBATCH --mem=40G
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#CommentSBATCH --gres=gpu:1
#SBATCH --exclude=yukhoe  # you can exclude specified nodes here
#SBATCH --partition=long
#CommentSBATCH --nodelist=habaki  # you can specify nodes where the job should be run; Ditto

seed=$1
acquisition_name=$2
budget=$3
round=$4
ds_config_file=$5
model_config_file=$6

cd $(git rev-parse --show-toplevel)/

uv run src/cp4bal/main.py --seed $seed --acquisition_name $acquisition_name --budget $budget --round $round --dataset_config_file $ds_config_file --model_config_file $model_config_file --propagation
