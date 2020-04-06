import paho.mqtt.client as mqtt
from thespian.actors import *
from common import *
from model_utils import federated_aggregation
import json
from json import JSONEncoder

import numpy as np

MQTT_URL = 'localhost'
MQTT_PORT = 1883


class AggregatorActor(Actor):

    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)

    def receiveMessage(self, message, sender):
        print('aggregator receive message')

        if message.get_type() == MsgType.AGGREGATION:
            print("\n**Aggregation process**\n")
            devices = message.get_body()
            
            federated_train_data = [device.get_dataset() for device in devices]

            print("federated aggregation")

            averaged_weights = federated_aggregation(federated_train_data)

            """
            DISTRIBUTE THE MODEL
            """
            # publishes on MQTT topic
            self.client.publish("topic/fl-update", json.dumps(averaged_weights, cls=self.NumpyArrayEncoder));

            print("\npublished update to 'topic/fl-update'")

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')


    def on_connect(client, userdata, flags, rc):
            print(f"Connected with result code {rc}")
            client.subscribe("topic/fl-broadcast")

    def __init__(self, keep_alive: int = 60):
        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        collector = {}
        self.client = mqtt.Client(userdata = collector)
        self.client.connect(MQTT_URL, MQTT_PORT, 60)
        self.client.on_connect = self.on_connect
        