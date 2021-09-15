import csv
import os

def get_results(exp_paths):
  best_ner_f1 = 0
  best_ner_exp = ""
  best_rel_f1 = 0
  best_rel_exp = ""
  for p in exp_paths:
    with open(os.path.join(p, "eval_valid.csv"), newline='') as f:
      resultreader = csv.DictReader(f, delimiter=";")

      row = next(resultreader, None)
      if row is not None:
        print("{} & {} & {} \\\\".format(row['ner_prec_micro'], row['ner_rec_micro'], row['ner_f1_micro']))
        print("{} & {} & {} \\\\".format(row['rel_prec_micro'], row['rel_rec_micro'], row['rel_f1_micro']))
        
        ner_f1 = float(row['ner_f1_micro'])
        if ner_f1 > best_ner_f1:
          best_ner_f1 = ner_f1
          best_ner_exp = p
        
        rel_f1 = float(row['rel_f1_micro'])
        if rel_f1 > best_rel_f1:
          best_rel_f1 = rel_f1
          best_rel_exp = p
        
        
  return [best_ner_exp, best_rel_exp]


def main():
  exps = ["data/log/medcaus_train/2021-09-07_01:26:56.861847",
          "data/log/medcaus_train/2021-09-07_09:22:56.098667"
          ]
  
  best_exps = get_results(exps)
  print(best_exps)

main()