import re, string
from collections import Counter
import numpy as np
import csv
import sys
import pickle
import nltk
from nltk.corpus import stopwords


def parse_article(article):
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
    stripped = strip_punc(article)
    def remove_non_ascii(text):
        return ''.join(i for i in text if ord(i)<128)
    cleaned = remove_non_ascii(stripped)
    
    def to_counter(string):
        string = strip_punc(string).lower().split()
        return Counter(string)

    count = to_counter(cleaned)
    count_filtered = dict()

    for i, k in enumerate(count.keys()):
        if i > 40:
            break
        if k not in stop_words:
            count_filtered.update({k: count[k]})
            

    return count_filtered

