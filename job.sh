#!/bin/sh
#SBATCH --job-name=because-crest-train-spert-neg10-span40-e40
#SBATCH -o logs/%x-%j.out
#SBATCH -p npl 
#SBATCH -N 1
# #SBATCH -c 144 
#SBATCH -t 03:00:00
#SBATCH -D /gpfs/u/home/SNTE/SNTEnksh/barn/projects/spert
# #SBATCH --gres=nvme
#SBATCH --gres=gpu:1
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=sahaa@rpi.edu

source activate pt

srun -u python exp.py train --dataset fincausal \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 4 \
                    --neg_entity_count 10 \
                    --neg_relation_count 5 \
                    --epochs 40 \
                    --max_span_size 20 \
                    --learn_span_size
