from __future__ import absolute_import, division, print_function
import collections
import warnings
from six.moves import range
import numpy as np
import six
import tensorflow as tf
import tensorflow_federated as tff

NUM_CLIENTS = 5
NUM_EPOCHS = 10
BATCH_SIZE = 20
SHUFFLE_BUFFER = 500

MODEL = None

print('\nImporting test dataset...')
emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()
print('Test dataset imported.\n')


warnings.simplefilter('ignore')
tf.compat.v1.enable_v2_behavior()
np.random.seed(0)

"""
NOTE: If the statement below fails, it means that you are
using an older version of TFF without the high-performance
executor stack. Call `tff.framework.set_default_executor()`
instead to use the default reference runtime.
"""
if six.PY3:
  tff.framework.set_default_executor(tff.framework.create_local_executor())



def init_model():
    global MODEL

    print('\nInitializing model...')
    model = create_compiled_keras_model()
    MODEL = keras_model_to_fn(model)
    print('Model initialized.\n')


def get_model():
    global MODEL
    return MODEL

def create_compiled_keras_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(
            10, activation=tf.nn.softmax, kernel_initializer='zeros', input_shape=(784,))])
    
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.SGD(learning_rate=0.02),
        metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

    return model



def keras_model_to_fn(keras_model):
    """
    Transform linear model into a federated learning model (different optimization function)
    """
    example_dataset = emnist_train.create_tf_dataset_for_client(emnist_train.client_ids[0])
    preprocessed_example_dataset = preprocess(example_dataset)

    sample_batch = tf.nest.map_structure(lambda x: x.numpy(), iter(preprocessed_example_dataset).next())
    
    return tff.learning.from_compiled_keras_model(keras_model, sample_batch)



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


def make_federated_data(client_data, client_ids):
    """
    CLIENT simulates federated data from clients
    """
    return [preprocess(client_data.create_tf_dataset_for_client(x))
            for x in client_ids]


def build_test_clients():
    # Selects clients
    sample_clients = emnist_train.client_ids[0:NUM_CLIENTS]

    # select training data related to selected clients
    federated_train_data = make_federated_data(emnist_train, sample_clients)

    return sample_clients, federated_train_data