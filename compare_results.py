import csv
import os

def get_results(exp_paths, type='ner'):
  best_f1 = 0
  best_exp = ""
  
  for p in exp_paths:
    with open(os.path.join(p, "eval_valid.csv"), newline='') as f:
      resultreader = csv.DictReader(f, delimiter=";")

      row = next(resultreader, None)
      if row is not None:
        print("{} & {:.2f} & {:.2f} & {:.2f} \\\\".format(p[-2:], 
                                                          float(row['%s_prec_micro' %type]), 
                                                          float(row['%s_rec_micro' %type]), 
                                                          float(row['%s_f1_micro' %type])))
        f1 = float(row['%s_f1_micro' %type])
        if f1 > best_f1:
          best_f1 = f1
          best_exp = p
        
                
  return best_exp


def main():
  exps = ["/gpfs/u/home/SNTE/SNTEnksh/scratch/output/spert/log/because-batch8-epoch40-neg10-span{}".format(i) \
          for i in range(10,31,5)
          ]
  
  best_exps = get_results(exps, 'ner')
  print(best_exps)

main()
