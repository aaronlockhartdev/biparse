# BiParse

BiParse is a Bipartisan Parsing extension powered by machine learning. In America, there is an increasing amount of political division as we are fed extremely polar perspectives on current events by the media. BiParse hopes to alleviate that problem, making the public aware of the biases the articles and blogs they read are feeding into as well as suggesting other perspectives on the issues of our time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

BiParse requires numpy, flask, tensorflow, pickle, requests, requests_html, csv, time, bs4, and urllib.

### Installing

Upon installation of BiParse and its prerequisites, run setup.py to build the neural net and training data (setup.py will be very ram intensive for a period of time). Run train.py to train the net using the data generated. After that is completed, run biparse.py in order to run the flask server. You can open the chrome extension contained in the 'app' directory by enabling developer mode in chrome and opening the unpacked extension.

## Built With

* [Flask](http://flask.pocoo.org/) - The web server used
* [TensorFlow](https://www.tensorflow.org/) - The machine learning library used

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

