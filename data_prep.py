import os
import numpy as np
from PIL import Image


def shapes():

    test_data = []
    train_data = []
    train_label = []

    for file in os.listdir('dataset'):
        if 'testing' in file:
            for test in os.listdir(os.path.join('dataset',file)):
                try:
                    img = Image.open(os.path.join('dataset',file,test))
                    test_data.append(np.asarray(img))
                except:
                    print(f'Invalid file {os.path.join("dataset",file,test)}. Ignoring...')

        elif 'training' in file:
            for i, shapes in enumerate(os.listdir(os.path.join('dataset',file))):
                for shp_train in os.listdir(os.path.join('dataset',file,shapes)):
                    try:
                        img_train = Image.open(os.path.join('dataset',file,shapes,shp_train))
                        train_data.append(np.asarray(img_train))
                        train_label.append(i)
                    except:
                        print(f'Invalid file {os.path.join("dataset",file, shapes,shp_train)}. Ignoring...')


    return (train_data,test_data,test_data)