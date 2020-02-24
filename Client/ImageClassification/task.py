from alex_net import AlexNet
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
from imagenet_classes import classes as in_classes

from os import listdir
from os.path import isfile, join


def load_images(path: str, res = {}) -> dict:
    """
    Read Image

    ::return:   {path: [image0, ..., imageN]} 
    """

    for f in listdir(path):
        sub_path = join(path, f) 
        
        if isfile(sub_path):
            res[path].append(get_image(sub_path))
        else:
            res[sub_path] = []
            load_images(sub_path, res)
    
    return res


def get_image(path):
    """
    """
    
    img = (imread(im)[:,:,:3]).astype(float32)
    
    # pre-processing
    img = img - mean(img)
    # a[:, :, 0], a[:, :, 2] = a[:, :, 2], a[:, :, 0] # Pre-process data changing to RGB to BGR (maybe useless)
        
    return img


def training(model, x_train, y_train):
    """
    Training
    """
    print('# Fit model on training data')
    # model.fit(x, y, batch_size=64, epochs=1, verbose=1, validation_split=0.2, shuffle=True)
    history = model.fit(x_train, y_train,
                        batch_size=64,
                        epochs=3,
                        # We pass some validation for
                        # monitoring validation loss and metrics
                        # at the end of each epoch
                        validation_data=(x_val, y_val))

    print('\nhistory dict:', history.history)


def evaluate(model, x_test, y_test):
    # Evaluate the model on the test data using `evaluate`
    print('\n# Evaluate on test data')
    results = model.evaluate(x_test, y_test, batch_size=128)
    print('test loss, test acc:', results)


def predict(model, x_val):
    # Generate predictions (probabilities -- the output of the last layer)
    # on new data using `predict`
    print('\n# Generate predictions for 3 samples')
    predictions = model.predict(x_val[:3])
    print('predictions shape:', predictions.shape)


def if __name__ == "__main__":
    
    model = AlexNet()

    training_set = load_images('./res/train') # {path: [image0, ..., imageN]} 


    # manipulate training set and divide images from labels
    x_train = []
    y_train = []

    for label, images in training_set.items():
        for image in images:
            x_train.append(image)
            y_train.append(label)


    train(model, x_train, y_train)
    
    evaluate(model, x_train, y_train)
    
    # predict(model, training_set)
