from uncertainty.classifier import Classifier
import pandas as pd
import numpy as np
import ast

cls = Classifier(granularity = "sentence", binary = True)
cls2 = Classifier(granularity = "sentence")
text = pd.read_csv("interim_dec29.csv", converters={'sentence': ast.literal_eval})
#text = text.head(5)

pred = []

pred2 = []

for ind in text.index:
    lst = []
    lst2 = []
    for i in text['sentence'][ind]:
        a = cls.predict(i)
        lst.append(a)

        a2 = cls2.predict(i)
        lst2.append(a2)

    pred.append(lst)
    pred2.append(lst2)

text['sent_pred'] = pred
text['sent_pred_nobin'] = pred2
text.to_csv("pred.csv", index = False)




