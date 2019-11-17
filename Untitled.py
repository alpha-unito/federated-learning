#!/usr/bin/env python
# coding: utf-8

# In[3]:


#@test {"skip": true}

# NOTE: If you are running a Jupyter notebook, and installing a locally built
# pip package, you may need to edit the following to point to the '.whl' file
# on your local filesystem.

# NOTE: The high-performance executor components used in this tutorial are not
# yet included in the released pip package; you may need to compile from source.
get_ipython().system('pip install --quiet --upgrade tensorflow_federated')
get_ipython().system('pip install --quiet --upgrade tf-nightly')

# NOTE: Jupyter requires a patch to asyncio.
get_ipython().system('pip install -q --upgrade nest_asyncio')
import nest_asyncio
nest_asyncio.apply()


# In[4]:


from __future__ import absolute_import, division, print_function

import collections
import warnings
from six.moves import range
import numpy as np
import six
import tensorflow as tf
import tensorflow_federated as tff

warnings.simplefilter('ignore')

tf.compat.v1.enable_v2_behavior()

np.random.seed(0)

# NOTE: If the statement below fails, it means that you are
# using an older version of TFF without the high-performance
# executor stack. Call `tff.framework.set_default_executor()`
# instead to use the default reference runtime.
if six.PY3:
  tff.framework.set_default_executor(tff.framework.create_local_executor())

tff.federated_computation(lambda: 'Hello, World!')()


# In[5]:


#  download and prepare the dataset

emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()
print(len(emnist_train.client_ids))

emnist_train.output_types, emnist_train.output_shapes

example_dataset = emnist_train.create_tf_dataset_for_client(emnist_train.client_ids[0])

# select only one example and show label
example_element = iter(example_dataset).next()
example_element['label'].numpy()


# In[7]:


# OPTIONAL: show one example element

from matplotlib import pyplot as plt
plt.imshow(example_element['pixels'].numpy(), cmap='gray', aspect='equal')
plt.grid('off')
_ = plt.show()


# In[8]:


# HELPER PROCESS

NUM_CLIENTS = 10
NUM_EPOCHS = 10
BATCH_SIZE = 20
SHUFFLE_BUFFER = 500

def preprocess(dataset):

  def element_fn(element):
    return collections.OrderedDict([
        ('x', tf.reshape(element['pixels'], [-1])),
        ('y', tf.reshape(element['label'], [1])),
    ])

  return dataset.repeat(NUM_EPOCHS).map(element_fn).shuffle(
      SHUFFLE_BUFFER).batch(BATCH_SIZE)


# In[9]:


# preprocess data transforming images into lists
preprocessed_example_dataset = preprocess(example_dataset)

sample_batch = tf.nest.map_structure(lambda x: x.numpy(), iter(preprocessed_example_dataset).next())

sample_batch


# In[10]:


# CLIENT simulates federated data from clients
def make_federated_data(client_data, client_ids):
  return [preprocess(client_data.create_tf_dataset_for_client(x))
          for x in client_ids]


# In[11]:


#SERVER
# Selects clients
sample_clients = emnist_train.client_ids[0:NUM_CLIENTS]

# select training data related to selected clients
federated_train_data = make_federated_data(emnist_train, sample_clients)

len(federated_train_data), federated_train_data[0]


# In[12]:


#SERVER
# Creates basic model for image classification with Keras
def create_compiled_keras_model():
  model = tf.keras.models.Sequential([
      tf.keras.layers.Dense(
          10, activation=tf.nn.softmax, kernel_initializer='zeros', input_shape=(784,))])
  
  model.compile(
      loss=tf.keras.losses.SparseCategoricalCrossentropy(),
      optimizer=tf.keras.optimizers.SGD(learning_rate=0.02),
      metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
  return model


# In[13]:


# Transform linear model into a federated learning model (different optimization function)
def model_fn():
  keras_model = create_compiled_keras_model()
  return tff.learning.from_compiled_keras_model(keras_model, sample_batch)


# In[14]:


# SERVER
# Training the model over the collected federated data
iterative_process = tff.learning.build_federated_averaging_process(model_fn)


# In[15]:


str(iterative_process.initialize.type_signature)


# In[17]:


# Let's invoke the initialize computation to construct the server state.
state = iterative_process.initialize()


# In[19]:


"""
The second of the pair of federated computations, next, represents a single round of Federated Averaging, 
which consists of pushing the server state (including the model parameters) to the clients, on-device training 
on their local data, collecting and averaging model updates, and producing a new updated model at the server.

In particular, one should think about next() not as being a function that runs on a server, but rather being a 
declarative functional representation of the entire decentralized computation - some of the inputs are provided 
by the server (SERVER_STATE), but each participating device contributes its own local dataset.
"""

# SERVER_STATE, FEDERATED_DATA -> SERVER_STATE, TRAINING_METRICS
# Single user example execution
state, metrics = iterative_process.next(state, federated_train_data)
print('round  1, metrics={}'.format(metrics))


# In[20]:


"""
Let's run a few more rounds. As noted earlier, typically at this point you would pick a subset of your simulation 
data from a new randomly selected sample of users for each round in order to simulate a realistic deployment in which 
users continuously come and go
"""

for round_num in range(2, 11):
  state, metrics = iterative_process.next(state, federated_train_data)
  print('round {:2d}, metrics={}'.format(round_num, metrics))

