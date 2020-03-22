from __future__ import absolute_import, division, print_function, unicode_literals
from alex_net import alex_net
import tensorflow as tf
import numpy as np
from imagenet_classes import classes as in_classes
from keras.preprocessing import image as image_utils

from keras.preprocessing.image import ImageDataGenerator
import keras
from keras.callbacks import ModelCheckpoint

import pandas as pd

from os import listdir
from os.path import isfile, join

import math

import time

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

#IMAGENET_PATH = './res/'
IMAGENET_PATH = '/media/lore/B6C8D9F4C8D9B33B/Users/lorym/Downloads'

VALIDATION_LABELS = './res/ILSVRC2012_devkit_t12/data/ILSVRC2012_validation_ground_truth.txt'

TOTAL_IMAGES = 961832
#TOTAL_IMAGES = 100

TARGET_SIZE = (224, 224)

BATCH_SIZE = 32
EPOCHS = 1

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
try: 
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
except: 
    print("Invalid device or cannot modify virtual devices once initialized. ")
    pass 
"""
# NB:
def predict(model, x_val):
    test_generator.reset()
    pred=model.predict_generator(test_generator,
                                    steps=STEP_SIZE_TEST,
                                    verbose=1)
    predicted_class_indices=np.argmax(pred,axis=1)
    labels = (train_generator.class_indices)
    labels = dict((v,k) for k,v in labels.items())
    predictions = [labels[k] for k in predicted_class_indices]
"""

def generate_train_iterator():
    # create generator
    datagen = ImageDataGenerator()

    #train_path = join(IMAGENET_PATH, 'ILSVRC2012_img_train_75_100/')
    train_path = join(IMAGENET_PATH, 'ILSVRC2012_img_train/')
    train_it = datagen.flow_from_directory(train_path,
                                           target_size=TARGET_SIZE,
                                           class_mode='categorical',
                                           color_mode='rgb',
                                           batch_size=BATCH_SIZE)


    # confirm the iterator works
    batchX, batchy = train_it.next()

    print(f'Batch x shape={batchX.shape}')
    print(f'Batch y shape={batchy.shape}')
    print('Batch y: ',len(batchy[0]), batchy[0])

    return train_it


def generate_validation_dataset():
    validation_images_path = join(IMAGENET_PATH, 'ILSVRC2012_img_val/val/')

    images_paths = [join(validation_images_path, f) for f in listdir(validation_images_path)
                    if isfile(join(validation_images_path, f))]

    validation_x = []

    for i in range(len(images_paths)):
        print(f"{i + 1} / 50000")
        image = image_utils.load_img(images_paths[i], target_size=(224, 224))
        image = image_utils.img_to_array(image)
        image = np.expand_dims(image, axis=0)
        validation_x.append(image)

    with open(VALIDATION_LABELS) as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    validation_y = [int(x.strip()) for x in content]

    validation_sequence = [(validation_x[i], validation_y[i]) for i in range(0, len(validation_x))]

    return np.array(validation_x), np.array(validation_y), np.array(validation_sequence)


def generate_validation_iterator():
    # IMAGES
    validation_images_path = join(IMAGENET_PATH, 'ILSVRC2012_img_val/val/')
    validation_x = [f for f in listdir(validation_images_path)
                    if isfile(join(validation_images_path, f))]

    # LABELS
    with open(VALIDATION_LABELS) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    validation_y = [int(x.strip()) for x in content]

    in_classes_lists = list(in_classes.keys())
    for i in range(len(validation_y)):
        class_index = validation_y[i] - 1
        validation_y[i] = in_classes_lists[class_index]

    validation_sequence = [[validation_x[i], validation_y[i]] for i in range(0, len(validation_x))]
    validation_dataframe = pd.DataFrame(validation_sequence, columns = ['x', 'y'])

    print(validation_dataframe)

    # create generator
    datagen = ImageDataGenerator()

    valid_it = datagen.flow_from_dataframe(
        dataframe=validation_dataframe,
        directory=join(IMAGENET_PATH, 'ILSVRC2012_img_val/val'),
        x_col='x',
        y_col='y',
        target_size=TARGET_SIZE,
        class_mode="categorical",
        color_mode= 'rgb',
        batch_size=BATCH_SIZE)

    # confirm the iterator works
    batchX, batchy = valid_it.next()

    print(f'Batch x shape={batchX.shape}')
    print(f'Batch y shape={batchy.shape}')
    print('Batch y: ', len(batchy[0]), batchy[0])

    return valid_it


if __name__ == "__main__":

    model = keras.applications.mobilenet_v2.MobileNetV2()
    model.summary()

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    #filepath = "MobileNetV2-75-100-{epoch:02d}-{val_accuracy:.2f}.hdf5"
    filepath = "MobileNetV2-75-100-{epoch:02d}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=False, mode='auto', period=1)

    """
    TRAIN
    """
    ts = time.time()

    train_it = generate_train_iterator()

    te = time.time()

    print(f"Train iterator finished in {te - ts} seconds ({(te - ts) / 60} minutes)")
    
    ts = time.time()

    steps = math.ceil(TOTAL_IMAGES / BATCH_SIZE)
    model.fit_generator(train_it, steps_per_epoch=steps, epochs=EPOCHS, use_multiprocessing=True, callbacks=[checkpoint])

    te = time.time()

    print(f"Epoch of train iterator finished in {te - ts} seconds ({(te - ts) / 60} minutes)")

    '''
    """
    VALIDATION
    """

    valid_it = generate_validation_iterator()

    steps = math.ceil(50000 / BATCH_SIZE)
    print(f"evaluate model in {steps} steps")

    score = model.evaluate_generator(valid_it, steps=steps, use_multiprocessing=True, verbose=1, callbacks=[checkpoint])
    print("Loss: ", score[0], "Accuracy: ", score[1])
    '''
