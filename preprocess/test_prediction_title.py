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

print("proportion of title with uncertainty ",len(a2)/len(text))


a1f = a1[a1['G'] == "Female"]
a2f = a2[a2['G'] == "Female"]
a2m = a2[a2['G'] == "Male"]

print("propor of female in certain title group ",len(a1f)/len(a1)," prop of female in certain group ",len(a2f)/len(a2))

print("proportion of female in the entire set",len(text[text['G'] == "Female"])/len(text))


nf = text[text['G'] == "Female"]
nm = text[text['G'] == "Male"]

nfu = nf[nf['title_pred_bin'] == 'U']
nmu = nm[nm['title_pred_bin'] == 'U']


print(len(text)," male: ",len(nm)," female: ",len(nf))
print(nf['title_pred_nobin'].value_counts().reset_index())
print(nm['title_pred_nobin'].value_counts().reset_index())


print("c ",1386/1540," E ",144/len(nfu)," I ",3/len(nfu)," U ",3/len(nfu)," N ",3/len(nfu)," D ",1/len(nfu))
print("c ",3891/4316," E ",372/len(nmu)," I ",10/len(nmu)," U ",4/len(nmu)," N ",31/len(nmu)," D ",8/len(nmu))

print(a2['Title'])