#Import Dependencies
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.corpus import wordnet as wn
wn = nltk.WordNetLemmatizer()
import re
import strings
import sklearn
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle


file_name = "SPAM_CLASSIFICATION.pkl"
classifier1 = pickle.load(open(file_name, 'rb')

app = Flask(__name__)