import collections
import warnings
import numpy as np
import six
import tensorflow as tf
import tensorflow_federated as tff
import datetime
import keras

NUM_CLIENTS = 5
NUM_EPOCHS = 10
BATCH_SIZE = 20
SHUFFLE_BUFFER = 500

warnings.simplefilter('ignore')
tf.compat.v1.enable_v2_behavior()
np.random.seed(0)

print('\nEAGERLY: ', tf.executing_eagerly())

"""
NOTE: If the statement below fails, it means that you are
using an older version of TFF without the high-performance
executor stack. Call `tff.framework.set_default_executor()`
instead to use the default reference runtime.
"""
if six.PY3:
  tff.framework.set_default_executor(tff.framework.create_local_executor())


def preprocess(dataset):
    """
    helper preprocess for building federated data
    """
    def element_fn(element):
        return collections.OrderedDict([
            ('x', tf.reshape(element['pixels'], [-1])),
            ('y', tf.reshape(element['label'], [1])),
        ])

    return dataset.repeat(NUM_EPOCHS).map(element_fn).shuffle(
        SHUFFLE_BUFFER).batch(BATCH_SIZE)


def model_fn():
    """
    Transform linear model into a federated learning model (different optimization function)
    """
    keras_model = tf.keras.applications.mobilenet_v2.MobileNetV2()

    # Compile the model
    #keras_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    x = np.zeros(shape=(1, 224, 224, 3))
    y = np.zeros(shape=(1, 1000))

    print('x', x)
    dummy_batch = collections.OrderedDict(x=x, y=x)

    #keras_model_clone = tf.keras.models.clone_model(keras_model)

    return tff.learning.from_keras_model(
        keras_model,
        dummy_batch=dummy_batch,
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[tf.keras.metrics.CategoricalAccuracy()])


def federated_aggregation(federated_train_data: list):
    """
    ::param: federated_train_data   list containing client weights [W1, ... , Wn]
    """
    global model

    # Training the model over the collected federated data
    fed_avg = tff.learning.build_federated_averaging_process(model_fn=model_fn)

    # Let's invoke the initialize computation to construct the server state.
    state = fed_avg.initialize()
    
    """
    TODO: Let's run a New learning round. At this point you would pick a subset of your simulation 
    data from a new randomly selected sample of users for each round.
    """
    state, metrics = fed_avg.next(state, federated_train_data)
    print('round  {0}, metrics={1}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), metrics))


model = model_fn()