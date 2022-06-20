import numpy as np
from keras import models
from keras import layers
import data_prep as dp

if __name__ == "__main__":
    # network = models.Sequential()
    # network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
    # network.add(layers.Dense(4, activation='softmax'))
    #
    # network.compile(optimizer='rmsprop',
    #                 loss='categorical_crossentropy',
    #                 metrics=['accuracy'])

    train_data, train_label, test_data, test_label = dp.shapes()

    print(dp.shapes(d='dataset').shape)