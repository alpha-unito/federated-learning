import warnings
import numpy as np
import tensorflow as tf

warnings.simplefilter('ignore')
tf.compat.v1.enable_v2_behavior()
np.random.seed(0)

print('\nEAGERLY: ', tf.executing_eagerly())


def federated_aggregation(federated_weights: list):
    """
    ::param: federated_train_data   list containing client weights [W1, ... , Wn]
    """
    averaged_weights = []
    for weights_list_tuple in zip(*federated_weights):
        averaged_weights.append(
            np.array([np.array(weights_).mean(axis=0) for weights_ in zip(*weights_list_tuple)]))

    return averaged_weights
