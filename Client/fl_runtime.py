import paho.mqtt.client as mqtt
import tensorflow as tf
import tensorflow_federated as tff
import datetime
import warnings
import numpy as np
import six
import collections
import json

NUM_EPOCHS = 10
BATCH_SIZE = 20
SHUFFLE_BUFFER = 500



warnings.simplefilter('ignore')
tf.compat.v1.enable_v2_behavior()
np.random.seed(0)

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


"""
NOTE: The data sets returned by load_data() are instances of tff.simulation.ClientData, an interface that allows 
you to enumerate the set of users, to construct a tf.data.Dataset that represents the data of a particular 
user, and to query the structure of individual elements. Here's how you can use this interface to explore 
the content of the data set. Keep in mind that while this interface allows you to iterate over clients ids, 
this is only a feature of the simulation data. As you will see shortly, client identities are not used by 
the federated learning framework - their only purpose is to allow you to select subsets of the data for simulations.
"""

print('\nImporting test dataset...')
emnist_train, emnist_test = tff.simulation.datasets.emnist.load_data()

# example_dataset = emnist_train.create_tf_dataset_for_client(emnist_train.client_ids[0])
# preprocessed_example_dataset = preprocess(example_dataset)
# sample_batch = tf.nest.map_structure(lambda x: x.numpy(), iter(preprocessed_example_dataset).next())
print('Test dataset imported.\n')



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/fl-broadcast")



def on_message(client, userdata, msg):
    print("received")
    if msg.payload.decode() == "Hello world!":
        print("Yes!")
        client.disconnect()



# MQTT CLIENT CONNECTION TO MESSAGE BROKER
client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message



def device_connection_to_server():
    sample_client = emnist_train.client_ids[0] 

    # select training data related to selected clients
    federated_train_data = preprocess(emnist_train.create_tf_dataset_for_client(sample_client))
    print(federated_train_data)
    send_msg = {
        'device': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        #'data': federated_train_data
        'data': tf.nest.map_structure(lambda x: x.numpy().tolist(), iter(federated_train_data).next())
    }
    
    client.publish("topic/fl-broadcast", json.dumps(send_msg));
    # client.publish("topic/fl-broadcast", payload=json.dumps(send_msg), qos=2, retain=False);
    #client.publish("topic/fl-broadcast", "Hello from device");
    
    print("\npublished message to 'topic/fl-broadcast'")
    # client.loop_forever()
