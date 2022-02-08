#!/bin/sh
#SBATCH --job-name=medcaus-crest-train-spert-neg10-span0const-e40
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
export TOKENIZERS_PARALLELISM=false

srun -u \
python exp.py eval --dataset because-crest \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 16 \
                    --neg_entity_count 10 \
                    --neg_relation_count 5 \
                    --epochs 40 \
                    --max_span_size 34 \
                    # --learn_span_size
