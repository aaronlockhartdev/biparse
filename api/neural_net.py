import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

tf.enable_eager_execution()

def create_model():
    model = keras.Sequential([
            keras.layers.Dense(5000,activation=tf.nn.sigmoid, input_shape=(57553,)),
            keras.layers.Dropout(0.5, noise_shape=None, seed=None),
            keras.layers.Dense(1000,activation=tf.nn.sigmoid),
            keras.layers.Dropout(0.5, noise_shape=None, seed=None),
            keras.layers.Dense(500,activation=tf.nn.sigmoid),
            keras.layers.Dropout(0.5, noise_shape=None, seed=None),
            keras.layers.Dense(120,activation=tf.nn.sigmoid),
            keras.layers.Dropout(0.5, noise_shape=None, seed=None),
            keras.layers.Dense(2,activation=tf.nn.softmax)

        ])
    model.compile(optimizer=keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

    model.save_weights("tmp/model.h5")
    with open("tmp/model.json", "w") as json_file:
        json_file.write(model_json)


def train_model(train_freq, train_bias, model):
    tf.logging.set_verbosity(1)
    model.summary()

    model.fit(train_freq, train_bias, epochs=3)
    model.evaluate(train_freq, train_bias)
    model.save_weights("tmp/model.h5")

    model_json = model.to_json()
    

def load_model():
    json_file = open("tmp/model.json", "r")
    model_json = json_file.read()
    json_file.close()
    model = keras.models.model_from_json(model_json)
    model.load_weights("tmp/model.h5")
    model.compile(optimizer=keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False),
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])
    return model

