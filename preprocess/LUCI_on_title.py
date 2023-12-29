from uncertainty.classifier import Classifier
import pandas as pd
import numpy as np
import ast

cls = Classifier(granularity = "sentence", binary = True)
cls2 = Classifier(granularity = "sentence")
text = pd.read_csv("interim_title.csv")


pred1, pred2 = [],[]

for ind in text.index:
    a = cls.predict(text['Title'][ind])
    pred1.append(a)
    a2 = cls2.predict(text['Title'][ind])
    pred2.append(a2)


text['title_pred_bin'] = pred1
text['title_pred_nobin'] = pred2
text.to_csv("pred_title.csv", index = False)




