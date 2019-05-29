import data
import neural_net

def main():
    data.set_train_data()
    data.get_unique()
    data.format_training_data()

    neural_net.create_model()
    
if __name__ == '__main__':
    main()