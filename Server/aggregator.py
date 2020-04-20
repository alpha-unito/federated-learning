import logging
extra = {'actor_name':'AGGREGATOR'}

import paho.mqtt.client as mqtt
from thespian.actors import *
from common import *
from model_utils import ModelUtils
import json
from json import JSONEncoder
import sys

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

        if message.get_type() == MsgType.AGGREGATION:
            # PERFORM AGGREGATION ON DEVICES CONTAINED IN THE MESSAGE
            devices = message.get_body()
            averaged_weights = self.model_utils.current_avg_weights

            if len(devices) > 0:
                federated_train_data = [device.get_dataset() for device in devices]

                averaged_weights = self.model_utils.federated_aggregation(federated_train_data)

                #SAVES CHECKPOINT
                self.model_utils.save_checkpoint()

            # publishes on MQTT topic
            total_bytes = 0
            for layer_weights in averaged_weights:
                total_bytes += layer_weights.nbytes

            publication = self.client.publish("topic/fl-update", json.dumps(averaged_weights, cls=self.NumpyArrayEncoder), qos=1)
            logging.debug(f"Result code: {publication[0]} Mid: {publication[1]} PayloadWeight: {sys.getsizeof(total_bytes)}", extra=extra)
            
            
            while publication[0] != 0:

                self.client.connect(MQTT_URL, MQTT_PORT, 60)
                publication = self.client.publish("topic/fl-update", json.dumps(averaged_weights, cls=self.NumpyArrayEncoder), qos=1)
                logging.debug(f"Result code: {publication[0]} Mid: {publication[1]}", extra=extra)
            
            logging.info("Sent update to 'topic/fl-update'", extra=extra)

        elif message.get_type() == MsgType.GREETINGS:
            logging.info("Init selector actor", extra=extra)


    @staticmethod
    def on_publish(client, userdata, mid):
        logging.info(f"Published message to 'topic/fl-update' with mid: {mid}", extra=extra)


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected to broker", extra=extra)

        else:    
            logging.warning("Connection failed. Retrying in 1 second...", extra=extra)
            
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)


    def __init__(self, keep_alive: int = 60):
        self.model_utils = ModelUtils()

        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        collector = {}
        self.client = mqtt.Client(userdata = collector)
        self.client.connect(MQTT_URL, MQTT_PORT, 60)
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        
        self.client.loop_start()
