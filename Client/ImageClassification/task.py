from alex_net import alex_net
import tensorflow as tf
import numpy as np
from imagenet_classes import classes as in_classes
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from keras.preprocessing.image import ImageDataGenerator

from os import listdir
from os.path import isfile, join

IMAGENET_PATH = '/media/lore/6B6223601B584A05/IMAGENET/'
TOTAL_IMAGES = 1300 * 1000
BATCH_SIZE = 512
EPOCHS = 1


def evaluate(model, x_test, y_test):
    # Evaluate the model on the test data using `evaluate`
    print('\n# Evaluate on test data')
    # results = model.evaluate(x_test, y_test, batch_size=128)
    
    results = model.evaluate_generator(test_it, steps=24)
    print('test loss, test acc:', results)


def predict(model, x_val):
    # Generate predictions (probabilities -- the output of the last layer)
    # on new data using `predict`
    print('\n# Generate predictions for 3 samples')
    # predictions = model.predict(x_val[:3])
    
    predictions = model.predict_generator(predict_it, steps=24)
    print('predictions shape:', predictions.shape)


if __name__ == "__main__":
    
    model = alex_net()

    #training_set = load_images(f'{IMAGENET_PATH}/ILSVRC2012_img_train/') # {path: [image0, ..., imageN]} 

    # create generator
    datagen = ImageDataGenerator()
    """
    # construct the training image generator for data augmentation
    aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
        width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
        horizontal_flip=True, fill_mode="nearest")
    """

    # prepare an iterators for each dataset
    train_it = datagen.flow_from_directory(f'{IMAGENET_PATH}/ILSVRC2012_img_train/', class_mode='binary')
    
    # val_it = datagen.flow_from_directory('data/validation/', class_mode='binary')
    
    # test_it = datagen.flow_from_directory('data/test/', class_mode='binary')

    # confirm the iterator works
    batchX, batchy = train_it.next()

    print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))


    # steps = total_images / batch_size 
    # model.fit_generator(train_it, steps_per_epoch=2540, validation_data=val_it, validation_steps=8, epochs = EPOCHS)
    model.fit_generator(train_it, steps_per_epoch=2540, epochs = EPOCHS)


    # train(model, x_train, y_train)
    
    # evaluate(model, x_train, y_train)
    
    # predict(model, training_set)
