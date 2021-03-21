import numpy as np 
import pandas as pd

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# Tokenize text
# @param data: Dataframe
# @param main_col : String
# @param cols : Array<String>
# @param MAX_NUM_WORDS: int
# @param MAX_LEN: int
#
# return Array
def tokenization_padding(data, main_col, cols, MAX_NUM_WORDS, MAX_LEN):
    input_tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
    
    input_tokenizer.fit_on_texts(data[main_col])
    input_integer_seq = input_tokenizer.texts_to_sequences(data[main_col])
    
    df_pad = pad_sequences(input_integer_seq, maxlen=MAX_LEN)
    
    for col in cols:
        input_tokenizer.fit_on_texts(data[col])
        input_integer_seq = input_tokenizer.texts_to_sequences(data[col])
        df_pad = df_pad + pad_sequences(input_integer_seq, maxlen=MAX_LEN)
    
    
    return df_pad


# © Laëtitia CONSTANTIN 2021