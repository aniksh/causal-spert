#!/bin/sh
#SBATCH --job-name=medcaus-train-spert-neg10-span10-e20
#SBATCH -o logs/%x-%j.out
#SBATCH -p npl 
#SBATCH -N 1
# #SBATCH -c 144 
#SBATCH -t 06:00:00
#SBATCH -D /gpfs/u/home/SNTE/SNTEnksh/barn/projects/spert
# #SBATCH --gres=nvme
#SBATCH --gres=gpu:1
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=sahaa@rpi.edu

source activate pt

srun -u python exp.py train --label medcaus-batch8-epoch20-neg10-span10 \
                    --dataset medcaus \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 8 \
                    --neg_entity_count 10 \
                    --neg_relation_count 10 \
                    --epochs 20 \
                    --max_span_size 10 \
