import os
import numpy as np
from PIL import Image


def shapes(d = 'dataset'):

    test_label = []
    test_data = []
    train_data = []
    train_label = []

    for file in os.listdir(d):
        if 'testing' in file:
            for i, test in enumerate(os.listdir(os.path.join(d,file))):
                for testing_data in os.listdir(os.path.join(d,file,test)):
                    if os.path.isfile(os.path.join(d,file,test,testing_data)):
                        try:
                            img = Image.open(os.path.join(d,file,test,testing_data))
                            test_data.append(np.asarray(img))
                            test_label.append(i)
                        except:
                            print(f'Invalid file {os.path.join(d,file,test, testing_data)}. Ignoring...')

        elif 'training' in file:
            for i, shapes in enumerate(os.listdir(os.path.join(d,file))):
                for shp_train in os.listdir(os.path.join(d,file,shapes)):
                    if os.path.isfile(os.path.join(d,file,shapes,shp_train)):
                        try:
                            img_train = Image.open(os.path.join(d,file,shapes,shp_train))
                            train_data.append(np.asarray(img_train))
                            train_label.append(i)
                        except:
                            print(f'Invalid file {os.path.join("dataset",file, shapes,shp_train)}. Ignoring...')


    return (train_data,train_label,test_data,test_label)


def clean(directory = os.getcwd()):
    for x in directory:
        if os.path.isfile(os.path.join(directory,x)) and x == '.DS_Store':
            os.remove(os.path.join(directory,x))
            print(f'removed {os.path.join(directory,x)}')
        else:
            if os.path.isdir(os.path.join(directory,x)):
                for y in os.listdir(os.path.join(directory,x)):
                    if os.path.isfile(os.path.join(directory, x, y)) and y == '.DS_Store':
                        os.remove(os.path.join(directory,x,y))
                        print(f'removed {os.path.join(directory,x,y)}')
                    else:
                        pass
