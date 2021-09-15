import json
import ast
import os
import sys
from argparse import ArgumentParser

import pandas as pd

def crest_to_spert(datapath):
    data = pd.read_csv(datapath)

    train_set = []
    dev_set = []
    test_set = []

    for i in range(len(data)):
        context = data['context'][i]
        example = {}
        example['tokens'] = context.split()
        
        span1 = ast.literal_eval(data['span1'][i])[0]
        span2 = ast.literal_eval(data['span2'][i])[0]
        idx = ast.literal_eval(data['idx'][i])

        # print(span1, '\n', span2, '\n', context, idx)
        # sys.exit(0)
        entities = []
        relations = []

        if span1 and span2:
            span1_start = len(context[:idx['span1'][0][0]].split())
            span1_end = span1_start + len(span1.split())
            span2_start = len(context[:idx['span2'][0][0]].split())
            span2_end = span2_start + len(span2.split())

            # Find direction
            if data['direction'][i] == 0:
                entities.append({"type": "Cause", "start": span1_start, "end": span1_end})
                entities.append({"type": "Effect", "start": span2_start, "end": span2_end})
            else:
                entities.append({"type": "Cause", "start": span2_start, "end": span2_end})
                entities.append({"type": "Effect", "start": span1_start, "end": span1_end})
        
        example['entities'] = entities

        if data['label'][i] == 1:
            relations.append({"type": "Cause-Effect", "head": 0, "tail": 1})
        
        example["relations"] = relations
    
        example["orig_id"] = i

        if data['split'][i] == 0:
            train_set.append(example)
        elif data['split'][i] == 1:
            dev_set.append(example)
        else:
            test_set.append(example)
    
    return train_set, dev_set, test_set


def main(args):
    train, dev, test = crest_to_spert(args.data)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    with open(os.path.join(args.output_dir, 'train.json'), 'w') as f:
        json.dump(train, f)
    
    if len(dev):
        with open(os.path.join(args.output_dir, 'dev.json'), 'w') as f:
            json.dump(dev, f)
    
    with open(os.path.join(args.output_dir, 'test.json'), 'w') as f:
        json.dump(test, f)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("data", type=str, help="Input file path")
    parser.add_argument("output_dir", type=str, help="Save directory")

    args = parser.parse_args()

    main(args)