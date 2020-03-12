import collections
import numpy as np
import tensorflow as tf
import tensorflow_federated as tff
import datetime


def model_fn():
    """
    Transform linear model into a federated learning model (different optimization function)
    """
    keras_model = tf.keras.applications.mobilenet_v2.MobileNetV2()
    keras_model.trainable = True

    print(f"\n *** {type(keras_model)}\n")

    # Compile the model
    # keras_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    x = np.zeros(shape=(1, 224, 224, 3))
    y = np.zeros(shape=(1, 1000))

    dummy_batch = collections.OrderedDict(x=x, y=x)

    # keras_model_clone = tf.keras.models.clone_model(keras_model)

    tff_model = tff.learning.from_keras_model(
        keras_model,
        dummy_batch=dummy_batch,
        loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        metrics=[tf.keras.metrics.CategoricalAccuracy()])

    keras_model.summary()
    print(tff_model)

    return tff_model


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


def custom_federated_aggregation(federated_weights: list):
    """
    Perform custom averagin between federated weights
    """
    averaged_weights = []
    for weights_list_tuple in zip(*federated_weights):
        averaged_weights.append(
            np.array([np.array(weights_).mean(axis=0) for weights_ in zip(*weights_list_tuple)]))

    return averaged_weights


model = tf.keras.applications.mobilenet_v2.MobileNetV2()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

x = [np.full(w.shape, 0) for w in model.get_weights()]
y = [np.full(w.shape, 1) for w in model.get_weights()]

model.set_weights(custom_federated_aggregation([x, y]))
#print("weights set")

print(model.get_weights())

"""
# TEST WITH RANDOM WEIGHTS
weights = [np.random.rand(*w.shape) for w in model.get_weights()]
model.set_weights(weights)
print("random weights set")
"""
# federated_aggregation(tf.keras.applications.mobilenet_v2.MobileNetV2().get_weights())