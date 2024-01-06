import pandas as pd
import numpy as np
import ast


text = pd.read_csv("vader_pred_fulltext.csv", converters={'sentence': ast.literal_eval})
print(len(text))
#print(text['gender'].unique())


G = []
for ind in text.index:
    if text['gender'][ind] == 'male' or text['gender'][ind] == 'M':
        G.append("Male")
    elif text['gender'][ind] == 'female' or text['gender'][ind] == 'F':
        G.append("Female")

text['G'] = G

text['total_cnt'] = text['sentence'].apply(lambda x: len(x))

text = text[text['total_cnt'] < 100]

print(len(text))

print("mean positive sentiment ",text['positive'].mean()," negative ",text['negative'].mean()," neutral ",text['neutral'].mean()," compound ",text['compound'].mean())

f = text[text['G'] == "Female"]
m = text[text['G'] == "Male"]

print("female mean positive sentiment ",f['positive'].mean()," negative ",f['negative'].mean()," neutral ",f['neutral'].mean()," compound ",f['compound'].mean())

print("male mean positive sentiment ",m['positive'].mean()," negative ",m['negative'].mean()," neutral ",m['neutral'].mean()," compound ",m['compound'].mean())