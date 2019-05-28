import re, string
from collections import Counter
import numpy as np
import csv
import sys
import pickle
import nltk
from nltk.corpus import stopwords


def parse_article(WordsAny):
    stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 
                'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'not', 'its', 'yours', 'such', 'into', 
                'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 
                'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'done', 'nor', 'me', 'were', 
                'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 
                'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 
                'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 
                'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 
                'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 
                'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    punc_regex = re.compile('[{}]'.format(re.escape(string.punctuation)))

    def strip_punc(corpus):
        return punc_regex.sub('', corpus)
    StripedWords = strip_punc(WordsAny)
    def remove_non_ascii(text):
        return ''.join(i for i in text if ord(i)<128)
    StripedWordss = remove_non_ascii(StripedWords)
    
    def to_counter(string):
        string = strip_punc(string).lower().split()
        return Counter(string)

    Count = to_counter(StripedWordss)
    count_filtered = dict()

    for i, k in enumerate(Count.keys()):
        if i > 40:
            break
        if k not in stop_words:
            count_filtered.update({k: Count[k]})
            

    return count_filtered

def get_train_data():
    csv.field_size_limit(100000000)
    train_text = list()
    train_freq = list()
    train_bias = list()
    liberal = ['New York Times', 'Buzzfeed News', 'Vox', 'Atlantic', 'Talking Points Memo', 
                'Guardian', 'NPR', 'Washington Post', 'CNN']
    conservative = ['Fox News', 'Breitbart', 'National Review', 'New York Post']
    sources = list()
    counter = 0
    for i in range(1, 4):
        with open('articles' + str(i) + '.csv', encoding='utf-8') as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            for row in range(0, len(csv_reader), 3):
                counter += 1
                print("Getting training data: " + str(round(100*counter/50000, 2)) + '%', end='\r', flush=True)
                if csv_reader[row][3] in conservative:
                    train_bias.append([0,1])
                    train_freq.append(list(parse_article(csv_reader[row][9]).values()))
                    train_text.append(list(parse_article(csv_reader[row][9]).keys()))
                if csv_reader[row][3] in liberal:
                    train_bias.append([1,0])
                    train_freq.append(list(parse_article(csv_reader[row][9]).values()))
                    train_text.append(list(parse_article(csv_reader[row][9]).keys()))

    with open('tmp/train_text.pkl', 'wb') as tt:
        pickle.dump(train_text, tt)
    with open('tmp/train_bias.pkl', 'wb') as tb:
        pickle.dump(train_bias, tb)
    with open('tmp/train_freq.pkl', 'wb') as tf:
        pickle.dump(train_freq, tf)
    

def open_train_data():
    with open('tmp/train_text.pkl', 'rb') as tt:
        train_text = pickle.load(tt)
    with open('tmp/train_bias.pkl', 'rb') as tb:
        train_bias = pickle.load(tb)
    with open('tmp/train_freq.pkl', 'rb') as tf:
        train_freq = pickle.load(tf)
    return train_freq, train_bias, train_text

# get_train_data()