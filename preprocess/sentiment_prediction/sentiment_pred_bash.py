from sentiment_pred import SentimentEstimate_final
import pandas as pd
import numpy as np
import sys

    
    
def func(n,lim):
    estimator = SentimentEstimate_final()



    text = pd.read_csv("individual_sentence.csv")
    #print("length of text before ",len(text))

    text = text.tail(len(text) - n)
    text = text.head(lim)
    #print("length of text after ",len(text))

    i = 1
    neg, neu, pos = [],[],[]
    for ind in text.index:
        #print("i ",i)
        #if i == 3519:
        #    ng,nu,ps = -1,-1,-1
        #else:
        #    ng,nu,ps = estimator.predict(text['sentence'][ind])
        ng,nu,ps = estimator.predict(text['sentence'][ind])
        neg.append(ng)
        neu.append(nu)
        pos.append(ps)
        #print(i)
        i += 1


    text['negative'] = neg
    text['neutral'] = neu
    text['positive'] = pos
    text.to_csv("sentiment_pred_sh_2.csv", index = False)

    d1 = pd.read_csv("sentiment_pred_sh_1.csv")
    #print("len of d1 ", len(d1))
    d2 = pd.read_csv("sentiment_pred_sh_2.csv")
    #print("len of d2 ", len(d2))
    d = pd.concat([d1, d2], ignore_index=True)
    #print("len of d ",len(d))
    #print(d['post_id'].nunique())
    d.to_csv("sentiment_pred_sh_1.csv", index = False)
    print("complete***** len of d {} and post {}".format(len(d),d['post_id'].nunique()))

if __name__ == "__main__":
    n = int(sys.argv[1])
    func(n,5000)
