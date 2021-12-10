import argparse
import os

from args import train_argparser, eval_argparser, predict_argparser
from spert import input_reader
from spert.spert_trainer import SpERTTrainer


def _train(args):
    arg_parser = train_argparser()
    run_args, _ = arg_parser.parse_known_args()
    run_args_dict = vars(run_args)
    for k, v in vars(args).items():
      if k in run_args_dict:
        run_args_dict[k] = v

    print("-" * 50)
    print(run_args_dict)
    
    trainer = SpERTTrainer(run_args)
    trainer.train(train_path=run_args.train_path, valid_path=run_args.valid_path,
                  types_path=run_args.types_path, input_reader_cls=input_reader.JsonInputReader)


def _eval(args):
    arg_parser = eval_argparser()
    run_args, _ = arg_parser.parse_known_args()
    run_args_dict = vars(run_args)
    for k, v in vars(args).items():
      if k in run_args_dict:
        run_args_dict[k] = v

    print("-" * 50)
    print(run_args_dict)
    
    trainer = SpERTTrainer(run_args)
    trainer.eval(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                 input_reader_cls=input_reader.JsonInputReader)


def _predict(args):
    arg_parser = predict_argparser()
    run_args, _ = arg_parser.parse_known_args()
    print(vars(args))



def __predict(run_args):
    trainer = SpERTTrainer(run_args)
    trainer.predict(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                    input_reader_cls=input_reader.JsonPredictionInputReader)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('mode', type=str, help="Mode: 'train' or 'eval'")
    arg_parser.add_argument('--dataset', type=str, default=None)
    arg_parser.add_argument('--model_path', type=str, default=None)
    arg_parser.add_argument('--tokenizer_path', type=str, default=None)
    arg_parser.add_argument('--train_batch_size', type=int, default=4)
    arg_parser.add_argument('--neg_entity_count', type=int, default=10)
    arg_parser.add_argument('--neg_relation_count', type=int, default=10)
    arg_parser.add_argument('--epochs', type=int, default=20)
    arg_parser.add_argument('--max_span_size', type=int, default=10)
    args, _ = arg_parser.parse_known_args()

    # Set default values
    args.label = "{}-batch{}-epoch{}-neg{}-span{}".format(args.dataset,
                                                          args.train_batch_size,
                                                          args.epochs,
                                                          args.neg_entity_count,
                                                          args.max_span_size)
    args.train_path = "data/datasets/%s/train.json" % args.dataset
    args.valid_path = "data/datasets/%s/test.json" % args.dataset
    args.dataset_path = "data/datasets/%s/test.json" % args.dataset
    args.types_path = "data/datasets/%s/types.json" % args.dataset
    args.eval_batch_size = 1
    args.store_predictions = True
    # args.store_examples = True
    args.final_eval = True
    # args.max_pairs = 100
    args.log_path = "/gpfs/u/home/SNTE/SNTEnksh/scratch/output/spert/log"
    args.save_path = "/gpfs/u/home/SNTE/SNTEnksh/scratch/output/spert/save"
    if args.mode != "train":
      args.model_path = os.path.join(args.save_path, args.label, "final_model")
      args.tokenizer_path = args.model_path
    
    if args.mode == 'train':
        _train(args)
    elif args.mode == 'eval':
        _eval(args)
    elif args.mode == 'predict':
        _predict(args)
    else:
        raise Exception("Mode not in ['train', 'eval', 'predict'], e.g. 'python spert.py train ...'")
