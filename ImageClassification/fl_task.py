from __future__ import absolute_import, division, print_function, unicode_literals
from alex_net import alex_net
import tensorflow as tf
import tensorflow_federated as tff

import time
import numpy as np
from imagenet_classes import classes as in_classes
import collections

from keras.preprocessing.image import ImageDataGenerator
import keras
import six


IMAGENET_PATH = '/media/lore/6B6223601B584A05/IMAGENET/'
# TOTAL_IMAGES = 1300 * 1000
TOTAL_IMAGES = 100
TARGET_SIZE = (224, 224)
BATCH_SIZE = 100
EPOCHS = 3
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

NUM_CLIENTS = 10
NUM_EPOCHS = 5
SHUFFLE_BUFFER = 100
PREFETCH_BUFFER=10

def model_fn(keras_model, batch):
    """
    # We _must_ create a new model here, and _not_ capture it from an external
    # scope. TFF will call this within different graph contexts.
    """
    return tff.learning.from_keras_model(
      keras_model,
      dummy_batch=batch,
      loss=tf.keras.losses.SparseCategoricalCrossentropy(),
      metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])


def preprocess(dataset):

    def batch_format_fn(element):
        """Flatten a batch `pixels` and return the features as an `OrderedDict`."""
        return collections.OrderedDict(
            x=tf.reshape(element['pixels'], [-1, 784]),
            y=tf.reshape(element['label'], [-1, 1]))

    return dataset.repeat(NUM_EPOCHS).shuffle(SHUFFLE_BUFFER).batch(
      BATCH_SIZE).map(batch_format_fn).prefetch(PREFETCH_BUFFER)


def load_sample_dataset():
    # Load simulation data.
    emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()

    example_dataset = emnist_train.create_tf_dataset_for_client(
        emnist_train.client_ids[0])

    preprocessed_example_dataset = preprocess(example_dataset)

    sample_batch = tf.nest.map_structure(lambda x: x.numpy(),
                                         next(iter(preprocessed_example_dataset)))

    return sample_batch


def fl_evaluate(train_data, num_rounds=10):
    state = trainer.initialize()
    for _ in range(num_rounds):
        t1 = time.time()
        state, metrics = trainer.next(state, train_data)
        t2 = time.time()
        print('loss {}, round time {}'.format(metrics.loss, t2 - t1))


def load_dataset():
    # create generator
    datagen = ImageDataGenerator()

    # prepare an iterators for each dataset
    # train_path = f'{IMAGENET_PATH}/ILSVRC2012_img_train/'
    train_path = "../res/train"
    train_it = datagen.flow_from_directory(train_path,
                                           target_size=TARGET_SIZE,
                                           class_mode='categorical',
                                           color_mode='rgb',
                                           batch_size=BATCH_SIZE)
    ret = train_it.next()

    return collections.OrderedDict(
        x=ret[0],
        y=ret[1])


if __name__ == "__main__":
    # sample_train_data = load_sample_dataset()
    # print(sample_train_data)

    train_data = load_dataset()
    print(train_data)

    keras_model = keras.applications.mobilenet_v2.MobileNetV2()
    tf_model = tf.keras.models.Model(keras_model)
    model = model_fn(tf_model, train_data)

    model.summary()


    trainer = tff.learning.build_federated_averaging_process(
        model_fn,
        client_optimizer_fn=lambda: tf.keras.optimizers.SGD(learning_rate=0.02))
    fl_evaluate(train_data)

