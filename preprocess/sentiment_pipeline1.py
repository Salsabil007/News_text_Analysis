import pandas as pd
import numpy as np
import ast

text = pd.read_csv("interim_sentiment.csv", converters={'sentence': ast.literal_eval})
print(len(text))
print(text.dtypes)

text = text[text['sent_len'] >= 5]
text = text[text['sent_len'] <= 120]

print(len(text))

text = text.drop(columns = ['new_text'], axis = 1)

post_identifier = []
i = 0
for ind in text.index:
    post_identifier.append(i)
    i += 1

text['post_id'] = post_identifier
print(text['sent_len'].sum())

#print(text.head(1))
text_exploded = text.explode('sentence')
print(len(text_exploded))
print(text_exploded.iloc[0]['sentence'])

#print(text_exploded.dtypes)
text_exploded.to_csv("individual_sentence.csv", index = False)

tt = pd.read_csv("individual_sentence.csv")
print(tt.iloc[0]['sentence'])
#print(len(text_exploded))
#print(text.iloc[12]['sentence'])
#print(text.iloc[12]['URL'])




'''a = pd.DataFrame()
a['id'] = [1,2,3,4]
a['g'] = ['m','f','m','f']
a['sentence'] = [['i am salsabil', 'go to heaven'], ['i like it','i hate it'],['move it','no way','i like it'], ['get it', 'I want to say,\"X\".']]
a_exploded = a.explode('sentence')
print(a_exploded)'''