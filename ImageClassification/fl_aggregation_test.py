import collections
import time

import tensorflow as tf
tf.compat.v1.enable_v2_behavior()

import tensorflow_federated as tff

source, _ = tff.simulation.datasets.emnist.load_data()


def map_fn(example):
  return collections.OrderedDict(
      x=tf.reshape(example['pixels'], [-1, 784]), y=example['label'])


def client_data(n):
  ds = source.create_tf_dataset_for_client(source.client_ids[n])
  return ds.repeat(10).shuffle(500).batch(20).map(map_fn)


train_data = [client_data(n) for n in range(10)]
batch = tf.nest.map_structure(lambda x: x.numpy(), next(iter(train_data[0])))


def model_fn():
  model = tf.keras.models.Sequential([
      tf.keras.layers.Input(shape=(784,)),
      tf.keras.layers.Dense(units=10, kernel_initializer='zeros'),
      tf.keras.layers.Softmax(),
  ])
  return tff.learning.from_keras_model(
      model,
      dummy_batch=batch,
      loss=tf.keras.losses.SparseCategoricalCrossentropy(),
      metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])


trainer = tff.learning.build_federated_averaging_process(model_fn)


def evaluate(num_rounds=10):
  state = trainer.initialize()
  for _ in range(num_rounds):
    t1 = time.time()
    state, metrics = trainer.next(state, train_data)
    t2 = time.time()
    print('loss {}, round time {}'.format(metrics.loss, t2 - t1))