from certainty_estimator.predict_certainty import CertaintyEstimator
import pandas as pd
import numpy as np
import ast
from tqdm import tqdm
import sys

def func(n,lim):
    estimator = CertaintyEstimator('sentence-level')
    


    text = pd.read_csv("individual_sentence.csv")
    #print("length of text before ",len(text))
    
    text = text.tail(len(text) - n)
    text = text.head(lim)
    #print("length of text after ",len(text))

    i = 1
    pred = []
    for ind in text.index:
        lst = estimator.predict(text['sentence'][ind])
        pred.append(lst)
        #print(i)
        i += 1


    text['sent_pred'] = pred
    text.to_csv("jiaxin_pred_sh_2.csv", index = False)

    d1 = pd.read_csv("jiaxin_pred_sh_1.csv")
    #print("len of d1 ", len(d1))
    d2 = pd.read_csv("jiaxin_pred_sh_2.csv")
    #print("len of d2 ", len(d2))
    d = pd.concat([d1, d2], ignore_index=True)
    #print("len of d ",len(d))
    #print(d['post_id'].nunique())
    d.to_csv("jiaxin_pred_sh_1.csv", index = False)
    print("complete***** len of d {} and post {}".format(len(d),d['post_id'].nunique()))

if __name__ == "__main__":
    n = int(sys.argv[1])
    func(n,5000)


'''import pandas as pd


a = pd.read_csv("tt2.csv")

tt = pd.read_csv("tt.csv")
d = pd.concat([tt, a], ignore_index=True)
d.to_csv("tt.csv", index = False)'''
