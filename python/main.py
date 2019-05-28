from article_parse import open_train_data, parse_article
from neural_net import train_model, load_model
from scraper import parse_links
import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
from article_scraper import scrape_article, scrape_article_headline
from pprint import pprint


# to get and format train data, article_parse.get_train_data(), get_unique_in(), format_training_data()

train_freq, train_bias, train_text = open_train_data()


def get_unique_in():

    unique = list()

    total = list()

    for i in train_text:
        print(str(round(100*train_text.index(i)/len(train_text), 2)) + "%", end='\r', flush=True)
        total.extend(i)
    unique = list(set(total))


    with open('tmp/unique_in.pkl', 'wb') as ui:
        pickle.dump(unique, ui)

    print(len(unique))

def load_unique():

    with open('tmp/unique_in.pkl', 'rb') as ui:
        unique = pickle.load(ui)

    return unique

def format_data(data, unique):
    formatted = np.zeros((len(unique)))
    for t in data.keys():
        try:
            formatted[unique.index(t)] = data[t]
        except:
            pass
    return np.asarray([formatted])

def format_training_data():
    unique = load_unique()
    training_data_formatted = list()
    for i, t in enumerate(train_text):
        formatted = np.zeros((len(unique)))
        print(str(round(100*i/len(train_text), 2)) + "%", end='\r', flush=True)
        for i1, t1 in enumerate(t):
            formatted[unique.index(t1)] = train_freq[i][i1]
        training_data_formatted.append(formatted)
    combined = list(zip(training_data_formatted, train_bias))
    random.shuffle(combined)
    training_data_formatted[:], train_bias[:] = zip(*combined)
    with open('tmp/training_data_formatted.pkl', 'wb') as tdf:
        pickle.dump(training_data_formatted, tdf)
    with open('tmp/train_bias_formatted.pkl', 'wb') as tbf:
        pickle.dump(train_bias, tbf)

def get_final_training_data():
    with open('tmp/training_data_formatted.pkl', 'rb') as tdf:
        freq = np.asarray(pickle.load(tdf))
    with open('tmp/train_bias_formatted.pkl', 'rb') as tbf:
        bias = np.asarray(pickle.load(tbf))
    return freq, bias

# final_training_freq, final_training_bias = get_final_training_data()
# print("Loaded training data, initializing neural net")
# train_model(final_training_freq, final_training_bias

model = load_model()
unique = load_unique()


print(model.summary())

def get_data(url):

    m = model.predict(format_data(parse_article(scrape_article(url)), unique))
    print(m)
    return m[0].astype(np.float64)

def get_links(url):

    threshold = 0.7

    cons = None
    lib = None
    mid = None

    for p in parse_links(scrape_article_headline(url)):
        data = get_data(str(p))
        if data[0] > threshold and lib is None:
            lib = str(p)
        elif data[1] > threshold and cons is None:
            cons = str(p)
        elif mid is None:
            mid = str(p)
        if lib is not None and cons is not None and mid is not None:
            break

    return cons, lib, mid





from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin, CORS
print("DONE")

app = Flask(__name__)
app.config()
cors = CORS(app, resources={r"/*": {"origins": "chrome-extension://*"}})
url = ''
@app.route('/output', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def output():
    global url
    url = request.get_json(force=True).get('url')
    print("URL")
    print(url)
    return 'OK', 200

        

@app.route('/input', methods=['GET'])
def input():
    global url
    try:
        data = get_data(url)
    except:
        data = [0, 0]
    # cons, lib, mid = get_links(url)
    # , 'right_link': cons, 'left_link': lib, 'mid_link': mid
    message = {'right': data[1], 'left': data[0]}
    print(message)
    j = jsonify(message)
    print(j)
    return j
	

if __name__ == '__main__':
	app.run("0.0.0.0", "5000", debug=True)


