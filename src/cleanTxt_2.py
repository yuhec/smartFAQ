import numpy as np 
import pandas as pd
from time import time 
import re as re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

# Remove HTML code from a text
# @param txt: Array<string>
#
# return Array<string>
def remove_HTML_code(txt):
    return [re.sub('(<\s*\w[^>]*>)|<\s*\/\s*\w[^>]*>', ' ', str(row)).lower() for row in txt]

# Remove HTML code from a text
# @param txt: Array<string>
#
# return Array<string>
def remove_characters(txt):
    return [re.sub("[^A-Za-z']+", ' ', str(row)).lower() for row in txt]


# Remove HTML Code, characters et remove stopwords 
# @param df : Dataframe
# @param str_cols : Array<string>
#
# return string
def brief_cleaning(df, str_cols):
    t = time()
    for col in str_cols:
        sentences = []
        for sentence in df[col]:
            sentence = re.sub('(<\s*\w[^>]*>)|<\s*\/\s*\w[^>]*>', ' ', sentence)
            sentence = re.sub("[^A-Za-z']+", ' ', sentence)
            sentence = remove_stop_words(sentence)
            sentence = " ".join(sentence)
            
            sentences.append(sentence)
        df[col] = sentences
    print('Time to clean up everything: {} mins'.format(round((time() - t) / 60, 2)))
    return df

# © Laëtitia CONSTANTIN 2021