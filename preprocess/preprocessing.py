import pandas as pd
import numpy as np
import pycld2 as cld2
import argparse
import regex
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import ast
from collections import OrderedDict


def remove_bad_chars(text):
    RE_BAD_CHARS = regex.compile(r"[\p{Cc}\p{Cs}]+")
    return RE_BAD_CHARS.sub("", text)

def extract_sentences_and_word_count(paragraph):
    pattern = re.compile(r'(\s+[A-Z])\.')

    # Replace the pattern with a space and the matched uppercase letter
    paragraph = pattern.sub(r'\1 ', paragraph)

    sentences = sent_tokenize(paragraph)
    sentences_with_word_count = []

    for sentence in sentences:
        words = word_tokenize(sentence)
        word_count = len(words)
 
        sentences_with_word_count.append((sentence, word_count))

    lst = []

    add = ["subscribe", "sign up", "image credit", "ad blocker", "ad blockers", "advertise", "advertisement"] #continue reading
    # Print the extracted sentences and word count
    for i, (sentence, word_count) in enumerate(sentences_with_word_count, start=1):
        flag = 1
        if sentence != "\"X\".":
            #print(f"Sentence {i}: {sentence}\nWord Count: {word_count}\n")
            for j in add:
                if j in sentence.lower():
                    flag = 0
                    break
            if flag == 1:        
                lst.append(sentence)

    res = list(OrderedDict.fromkeys(lst))
    return res
    


class data_process():
    
    def __init__(self, text):
        self.text = text

    '''def print_len(self):
        print(len(self.text))'''

    def deduplicate(self):
        #drop duplicate rows
        self.text = self.text.drop_duplicates()
        #self.text = self.text.drop_duplicates(subset = ['doi','media'])
        self.text = self.text.drop_duplicates(subset = ['Text'])
        self.text = self.text.dropna(subset = ['Text'])
        self.text['Text'] = self.text['Text'].astype(str)

    def remove_non_english_bad_characters(self):
        #remove bad characters e.g., \t, \t, and special characters from text
        self.text['new_text'] = self.text['Text'].apply(lambda x:remove_bad_chars(x))

        #detect the language of the text and remove non-english text
        self.text['lang'] = self.text['new_text'].apply(lambda x:cld2.detect(x)[2][0][0])
        self.text = self.text[self.text['lang'] == 'ENGLISH']

        #remove extra white space
        self.text['new_text'] = self.text['new_text'].apply(lambda x: regex.sub(r'\s+',' ',x))

        

        

    def wordlimit(self):
        self.text['word_count'] = self.text['new_text'].apply(lambda x: len(x.split()))
        self.text = self.text[self.text['word_count'] >= 100]

    def replace_and_add_fullstop(self):
        # Use a regular expression to find and replace content within quotation marks
        #cleaned_text = re.sub(r'["“]([^"”]*?)([.,;?!]*)["”]', r'"X"\2', text)
        self.text['new_text'] = self.text['new_text'].apply(lambda x: re.sub(r'["“]([^"”]*?)([.,;?!]*)["”]', r'"X"\2', x))
        #add space after punctuation if there is none
        self.text['new_text'] = self.text['new_text'].apply(lambda x: re.sub(r'([.,;?!])(?!\s|$)', r'\1 ', x))
        #print(self.text)
        #return cleaned_text

        return self.text
        
    def extract_sentence(self):
        self.text['sentence'] = self.text['new_text'].apply(lambda x: extract_sentences_and_word_count(x))
        
        

        

    '''def select_valid_only(self):
        self.text = self.text[self.text['lang'] == 'ENGLISH']
        self.text = self.text[self.text['word_count'] >= 130]'''

    def pipeline(self):
        self.deduplicate()
        self.remove_non_english_bad_characters()
        self.wordlimit()
        self.replace_and_add_fullstop()
        self.extract_sentence()
        return self.text



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str, default="data/news_text_dec29.csv") #data/news_text.csv
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    filepath = args.filepath
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {filepath} is empty")
    
    processor = data_process(data)

    # Call the print_len method
    #processor.print_len()
    '''processor.remove_non_english_bad_characters()
    processor.replace_and_add_fullstop()
    text = processor.extract_sentence()'''
    #print(text)
    text = processor.pipeline()
    #text = text.drop(columns = ['Title','Text','Keywords','doi','media','gender','text','lang'], axis = 1)
    text = text.drop(columns = ['Title','Text','Keywords','lang'], axis = 1)
    text.to_csv("interim_dec29.csv", index = False)
    text = pd.read_csv("interim_dec29.csv", converters={'sentence': ast.literal_eval})
    print(len(text))
    '''
    #df_rea = pd.read_csv('sample_data.csv', converters={'column_name': ast.literal_eval})
    l = len(text.iloc[1]['sentence'])
    print(l)
    l = len(text.iloc[2]['sentence'])
    print(l)
    l = len(text.iloc[3]['sentence'])
    print(l)'''
    l = len(text.iloc[0]['sentence'])
    print(l)
    print(text.iloc[0]['sentence'][0],"\n")
    print(text.iloc[0]['sentence'][1],"\n")
    print(text.iloc[0]['sentence'][2],"\n")
    print(text.iloc[0]['sentence'][3],"\n")
    print(text.iloc[0]['sentence'][4],"\n")
    print(text.iloc[0]['sentence'][5],"\n")
    print(text.iloc[0]['sentence'][6],"\n")
    print(text.iloc[0]['sentence'][7],"\n")
    print(text.iloc[0]['sentence'][8],"\n")
    print(text.iloc[0]['sentence'][l-7],"\n")
    print(text.iloc[0]['sentence'][l-6],"\n")
    print(text.iloc[0]['sentence'][l-5],"\n")
    print(text.iloc[0]['sentence'][l-4],"\n")
    print(text.iloc[0]['sentence'][l-3],"\n")
    print(text.iloc[0]['sentence'][l-2],"\n")
    print(text.iloc[0]['sentence'][l-1],"\n")
    #print(len(text))
    #print(text.dtypes)
    #print(text.iloc[0]['new_text'])
    
#there could be repeated lines, so we should deduplicate the list of sentence