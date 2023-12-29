import pandas as pd
import numpy as np
import ast

text = pd.read_csv("pred_title.csv")
print(len(text))
print(text['gender'].unique())


G = []
for ind in text.index:
    if text['gender'][ind] == 'male' or text['gender'][ind] == 'M':
        G.append("Male")
    elif text['gender'][ind] == 'female' or text['gender'][ind] == 'F':
        G.append("Female")

text['G'] = G

a1 = text[text['title_pred_bin'] == 'C']
a2 = text[text['title_pred_bin'] == 'U']


a1f = a1[a1['G'] == "Female"]
a2f = a2[a2['G'] == "Female"]

print(len(a1f)/len(a1)," ",len(a2f)/len(a2))

print(len(text[text['G'] == "Female"])/len(text))