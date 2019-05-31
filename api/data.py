import pickle
import numpy as np
import parser

def set_train_data():
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
        with open('data/articles' + str(i) + '.csv', encoding='utf-8') as csv_file:
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            for row in range(0, len(csv_reader), 3):
                counter += 1
                print("Getting training data: " + str(round(100*counter/50000, 2)) + '%', end='\r', flush=True)
                if csv_reader[row][3] in conservative:
                    train_bias.append([0,1])
                    train_freq.append(list(parser.parse_article(csv_reader[row][9]).values()))
                    train_text.append(list(parser.parse_article(csv_reader[row][9]).keys()))
                if csv_reader[row][3] in liberal:
                    train_bias.append([1,0])
                    train_freq.append(list(parser.parse_article(csv_reader[row][9]).values()))
                    train_text.append(list(parser.parse_article(csv_reader[row][9]).keys()))

    with open('data/train_text.pkl', 'wb') as tt:
        pickle.dump(train_text, tt)
    with open('data/train_bias.pkl', 'wb') as tb:
        pickle.dump(train_bias, tb)
    with open('tmp/train_freq.pkl', 'wb') as tf:
        pickle.dump(train_freq, tf)
    

def open_train_data():
    with open('data/train_text.pkl', 'rb') as tt:
        train_text = pickle.load(tt)
    with open('data/train_bias.pkl', 'rb') as tb:
        train_bias = pickle.load(tb)
    with open('data/train_freq.pkl', 'rb') as tf:
        train_freq = pickle.load(tf)
    return train_freq, train_bias, train_text


def get_unique():

    unique = list()

    total = list()

    for i in train_text:
        print(str(round(100*train_text.index(i)/len(train_text), 2)) + "%", end='\r', flush=True)
        total.extend(i)
    unique = list(set(total))


    with open('data/unique.pkl', 'wb') as ui:
        pickle.dump(unique, ui)

    print(len(unique))

def load_unique():

    # loads the unique words

    with open('data/unique.pkl', 'rb') as ui:
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

    # formats data into list of numpy arrays each containing the input values 
    # for that data sample and randomizes them before saving to pkl files

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
    with open('data/training_freq_formatted.pkl', 'wb') as tdf:
        pickle.dump(training_data_formatted, tdf)
    with open('data/training_bias_formatted.pkl', 'wb') as tbf:
        pickle.dump(train_bias, tbf)

def get_train_data():

    # loads training data from files

    with open('data/training_freq_formatted.pkl', 'rb') as tdf:
        freq = np.asarray(pickle.load(tdf))
    with open('data/training_bias_formatted.pkl', 'rb') as tbf:
        bias = np.asarray(pickle.load(tbf))
    return freq, bias