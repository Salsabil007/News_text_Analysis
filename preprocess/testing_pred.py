import pandas as pd
import numpy as np
import ast


text = pd.read_csv("pred.csv", converters={'sentence': ast.literal_eval,'sent_pred': ast.literal_eval})
#print(len(text))
#print(len(text.iloc[0]['sentence']))
#print(len(text.iloc[0]['sent_pred']))

#print(text.iloc[0]['sent_pred'][0])
#print(text.iloc[0]['sentence'][4])

#print(text['gender'].unique())



total_cnt = []
uncertain = []
G = []
for ind in text.index:
    total_cnt.append(len(text['sent_pred'][ind]))
    sum = 0
    for i in text['sent_pred'][ind]:
        if i == 'U':
            sum += 1
    uncertain.append(sum)

    if text['gender'][ind] == 'male' or text['gender'][ind] == 'M':
        G.append("Male")
    elif text['gender'][ind] == 'female' or text['gender'][ind] == 'F':
        G.append("Female")
     


    
text['total_cnt'] = total_cnt
text['uncertain'] = uncertain
text['G'] = G



text = text.drop(columns = ['URL','doi','new_text','word_count','gender'], axis = 1)

#print(text.head(5))



text['prop'] = text['uncertain']/text['total_cnt']

text = text[text['total_cnt'] > 5]
text = text[text['total_cnt'] < 100]

f = text[text['G'] == "Female"]
m = text[text['G'] == "Male"]
m = m.sample(n = len(f), replace = False, random_state=0)

print(f['prop'].mean()," ", m['prop'].mean())

#print(f['total_cnt'].mean()," ", m['total_cnt'].mean())
print(len(f)," ",len(m))





