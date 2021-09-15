python exp.py train --label medcaus-batch4-epoch2-neg10-span10 \
                    --dataset medcaus \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 4 \
                    --neg_entity_count 10 \
                    --neg_relation_count 10 \
                    --epochs 2 \
                    --max_span_size 10 \