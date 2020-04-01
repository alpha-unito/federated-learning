from thespian.actors import *
from common import *
from model_utils import federated_aggregation
import json
import numpy as np

class AggregatorActor(Actor):

    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)

    # -------- MQTT UTILS -----------------------

    def on_connect(client, userdata, flags, rc):
        print(f"Aggregator connected with result code {rc}")
        client.subscribe("topic/fl-update")

    def on_message(client, userdata, msg):
        pass
    # -------- END MQTT UTILS ------------------


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
            client.publish("topic/fl-broadcast", json.dumps(averaged_weights, cls=NumpyArrayEncoder));

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')


    def __init__(self, url: str, port: int, collector: dict, keep_alive: int = 60):
        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        client = mqtt.Client(userdata = collector)
        
        client.connect(url, port, keep_alive)

        client.on_connect = self.on_connect
        client.on_message = self.on_message