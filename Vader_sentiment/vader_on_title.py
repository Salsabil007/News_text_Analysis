from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import ast

def sentiment_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
     
    #print("Overall sentiment dictionary is : ", sentiment_dict)
    #print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    #print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    return sentiment_dict['pos'], sentiment_dict['neg'], sentiment_dict['neu'], sentiment_dict['compound']



text = pd.read_csv("interim_title_dec29.csv")



pos, neg, com, neu = [],[],[],[]

for ind in text.index:
    a,b,c,d = sentiment_scores(text['Title'][ind])
    pos.append(a)
    neg.append(b)
    neu.append(c)
    com.append(d)
    


text['positive'] = pos
text['negative'] = neg
text['neutral'] = neu
text['compound'] = com
text.to_csv("vader_pred_title.csv", index = False)




