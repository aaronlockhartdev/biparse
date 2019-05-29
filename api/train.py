import neural_net
import data

def main():
    model = neural_net.load_model()
    train_freq, train_bias = data.get_train_data()
    neural_net.train_model(train_freq, train_bias, model)

if __name__ == '__main__'