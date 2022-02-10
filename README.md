# SpERT (Span-based Entity and Relation Transformer) for Causal Relation Extraction
PyTorch code of SpERT (Span-based Entity and Relation Transformer) for Causal Relation Extraction. 

## Setup
### Requirements
- Required
  - Python 3.5+
  - PyTorch (tested with version 1.4.0)
  - transformers (+sentencepiece, e.g. with 'pip install transformers[sentencepiece]', tested with version 4.1.1)
  - scikit-learn (tested with version 0.24.0)
  - tqdm (tested with version 4.55.1)
  - numpy (tested with version 1.17.4)
- Optional
  - jinja2 (tested with version 2.10.3) - if installed, used to export relation extraction examples
  - tensorboardX (tested with version 1.6) - if installed, used to save training process to tensorboard
  - spacy (tested with version 3.0.1) - if installed, used to tokenize sentences for prediction

### Process data
Create data directory and extract datasets
```
bash preprocess.sh
```

## Usage
### Training 
Train on BeCauSE dataset:
```
python exp.py train --dataset because-crest \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 16 \
                    --neg_entity_count 10 \
                    --neg_relation_count 5 \
                    --epochs 40 \
                    --max_span_size 34 \
```

### Evaluation
Evaluate the trained model on BeCauSE dataset:
```
python exp.py eval --dataset because-crest \
                    --model_path bert-base-cased \
                    --tokenizer_path bert-base-cased \
                    --train_batch_size 16 \
                    --neg_entity_count 10 \
                    --neg_relation_count 5 \
                    --epochs 40 \
                    --max_span_size 34 \
```

Set `max_span_size` to 0 to learn sample negative examples using constituency parse.
``
