# BiParse

BiParse is a Bipartisan Parsing extension powered by machine learning. In America, there is an increasing amount of political division as we are fed extremely polar perspectives on current events by the media. BiParse hopes to alleviate that problem, making the public aware of the biases the articles and blogs they read are feeding into as well as suggesting other perspectives on the issues of our time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

BiParse requires numpy, flask, tensorflow, pickle, requests, requests_html, csv, time, bs4, and urllib. The [all the articles](https://storage.googleapis.com/kaggle-datasets/1974/3493/all-the-news.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1559412413&Signature=ZBrO0PDkwXN9NSAbjwEwWg2W5fMVO7yo5oLcl71AsnePCkw1ApJbscwVUMaLCcmoQLTFgk3V9S%2FBmCDidaLKhgS4q3vpsL2AHFIYRdagtl6U3Q55rczOUP07dt1wehd0fcuIp%2ByyfEdThUlrpekOcolo1%2B8RDwMrgD%2BDjxjRS99eajY1cpae05krUTTAxS4xTgsHVc1bwBxpDwdikc1s%2B0MaLL%2FZq0yJ%2BqKiGaSwbfADpAkuUoUO1FvVqEUKNaClpc5pL%2Fp5l4Ds3ItT6GhdlvFzaN6BdExkssrRKpnFu%2B4Rc4f2OkJ%2FbaPSIFxslxAZJqmkgXENt%2FN5HdYAeLwsUA%3D%3D) dataset from kaggle is also necessary (it should be extracted to the /api/data project folder as individual .csv files)

### Installing

Upon installation of BiParse and its prerequisites, run setup.py to build the neural net and training data (setup.py will be very ram intensive for a period of time). Run train.py to train the net using the data generated. After that is completed, run biparse.py in order to run the flask server. You can open the chrome extension contained in the /app directory by enabling developer mode in chrome and opening the unpacked extension.

## Built With

* [Flask](http://flask.pocoo.org/) - The web server used
* [TensorFlow](https://www.tensorflow.org/) - The machine learning library used

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
