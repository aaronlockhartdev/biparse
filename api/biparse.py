import data
import neural_net
import parser
import scraper
import time
import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin, CORS

dataset = dict()
unique = data.load_unique()
model = neural_net.load_model()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "chrome-extension://*"}})
finished = False

@app.route('/', methods=['POST', 'GET'])
@cross_origin(origin='localhost', headers=['Content- Type','Authorization'])
def main():
    global dataset
    global finished
    ip = request.url_root
    if request.method == 'POST':
        url = request.get_json(force=True).get('url')
        try:
            content = scraper.scrape_article(url)
            parsed = parser.parse_article(content)
            formatted = data.format_data(parsed, unique)
            dat = model.predict(formatted)[0]
            dat = dat.astype(np.float64)
        except:
            dat = [0, 0]
            print("ERR GETTING MODEL PREDICTION")
        try:
            dataset[ip] = dat
        except:
            dataset.update({ip: dat})
        print("DATA: " + str(dataset[request.url_root]))

        print("URL: " + str(url))
        finished = True
        return 'OK', 200
    elif request.method == 'GET':
        x = 0
        while not finished:
            pass
        try:
            dat = dataset[ip]
        except:
            dat = [0, 0]
            print("ERR GETTING DATABASE")
        dataset.pop(ip)

        finished = False
        message = {'left': dat[0], 'right': dat[1]}
        print(message)
        json = jsonify(message)
        print(json)
        print("DATABASE LENGTH: " + str(len(dataset)))
        return json

if __name__ == '__main__':
    app.run("0.0.0.0", "5000", threaded=False, debug=True)
