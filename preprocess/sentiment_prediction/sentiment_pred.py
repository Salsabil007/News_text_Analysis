import pandas as pd
import numpy as np
from transformers import AutoModelForSequenceClassification, TFAutoModelForSequenceClassification, AutoTokenizer, AutoConfig
#from scipy.special import softmax
from torch.nn.functional import softmax
import torch
import scipy

class SentimentEstimate_final(object):
    def __init__(self, gpu = 'cpu'):

        if gpu == 'cuda':
          self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.gpu = gpu

        MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        if self.gpu == 'cuda':
          self.model = AutoModelForSequenceClassification.from_pretrained(MODEL).to(self.device)
        else:
          self.model = AutoModelForSequenceClassification.from_pretrained(MODEL)

        self.config = AutoConfig.from_pretrained(MODEL)

    def predict(self, text):
        encoded_input = self.tokenizer(text, return_tensors='pt')
        if self.gpu == 'cuda':
          encoded_input = {key: value.to(self.device) for key, value in encoded_input.items()}
        output = self.model(**encoded_input)
        if self.gpu == 'cuda':
          scores = output.logits.detach().cpu().numpy()
        else:
          scores = output[0][0].detach().numpy()
        #scores = softmax(scores)

        scores = torch.tensor(scores)  # Convert to PyTorch tensor
        #print(scores)
        if self.gpu == 'cuda':
          scores = softmax(scores, dim=1)
          scores = scores.numpy()
          #print(scores[0])
          print("in gpu")
          return scores[0][0],scores[0][1],scores[0][2]
        else:
          scores = softmax(scores, dim=0)
          scores = scores.numpy()

          #print(scores) #0 -> negative, 1 -> neutral,2 -> positive
          #print("in cpu")
          return scores[0],scores[1],scores[2]
