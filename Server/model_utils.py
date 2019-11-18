from __future__ import absolute_import, division, print_function
import collections
import warnings
import numpy as np
import six
from six.moves import range
import tensorflow as tf
import tensorflow_federated as tff
import datetime


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


print('\nImporting test dataset...')
emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()

example_dataset = emnist_train.create_tf_dataset_for_client(emnist_train.client_ids[0])
preprocessed_example_dataset = preprocess(example_dataset)
sample_batch = tf.nest.map_structure(lambda x: x.numpy(), iter(preprocessed_example_dataset).next())
print('Test dataset imported.\n')



def create_compiled_keras_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(
            10, activation=tf.nn.softmax, kernel_initializer='zeros', input_shape=(784,))])
    
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.SGD(learning_rate=0.02),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

    return model



def model_fn():
    """
    Transform linear model into a federated learning model (different optimization function)
    """
    model = create_compiled_keras_model()

    global sample_batch
    return tff.learning.from_compiled_keras_model(model, sample_batch)



def federated_aggregation(federated_train_data):
    # Training the model over the collected federated data
    iterative_process = tff.learning.build_federated_averaging_process(model_fn)
    
    # Let's invoke the initialize computation to construct the server state.
    state = iterative_process.initialize()
    
    """
    TODO: Let's run a New learning round. At this point you would pick a subset of your simulation 
    data from a new randomly selected sample of users for each round.
    """
    state, metrics = iterative_process.next(state, federated_train_data)
    print('round  {0}, metrics={1}'.format(
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), metrics))