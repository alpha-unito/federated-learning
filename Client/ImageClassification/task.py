from alex_net import AlexNet
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np


def load_images(path):
    """
    Read Image, and change to BGR

    im1 = (imread("./img/laska.png")[:,:,:3]).astype(float32)
    im1 = im1 - mean(im1)
    im1[:, :, 0], im1[:, :, 2] = im1[:, :, 2], im1[:, :, 0]
    """

    l = []
    for f in listdir(path):
        if isfile(join(path, f)):
        print "f: ",f
            l.append(join(path, f))
        else:
            l += listFile(join(path, f))

    return l


def pre_process(data):
    """
    Pre-process data for training
    """
    array=[]
    for im in data:
        a = (imread(im)[:,:,:3]).astype(float32)
        a = a - mean(a)
        a[:, :, 0], a[:, :, 2] = a[:, :, 2], a[:, :, 0]
        array.append(a)

    return array


def training(model, data):
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


def evaluate(model, data):
    # Evaluate the model on the test data using `evaluate`
    print('\n# Evaluate on test data')
    results = model.evaluate(x_test, y_test, batch_size=128)
    print('test loss, test acc:', results)


def predict(model, data):
    # Generate predictions (probabilities -- the output of the last layer)
    # on new data using `predict`
    print('\n# Generate predictions for 3 samples')
    predictions = model.predict(x_test[:3])
    print('predictions shape:', predictions.shape)


def if __name__ == "__main__":
    
    model = AlexNet()

    data = load_images('path')

    training_set = pre_process(data)

    train(model, training_set)
    
    evaluate(model, training_set)
    
    predict(model, training_set)
