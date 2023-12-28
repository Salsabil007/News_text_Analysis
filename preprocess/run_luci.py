from uncertainty.classifier import Classifier
import pandas as pd
import numpy as np
import ast

cls = Classifier(granularity = "sentence", binary = True)
text = pd.read_csv("interim.csv", converters={'sentence': ast.literal_eval})
text = text.head(5)

pred = []

for ind in text.index:
    lst = []
    for i in text['sentence'][ind]:
        a = cls.predict(i)
        lst.append(a)
    pred.append(lst)

text['sent_pred'] = pred
text.to_csv("pred.csv", index = False)




