import paho.mqtt.client as mqtt
from thespian.actors import *
from common import *
from model_utils import federated_aggregation
import json
from json import JSONEncoder
import time

import numpy as np

import logging
extra = {'actor_name':'AGGREGATOR'}

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
            devices = message.get_body()
            federated_train_data = [device.get_dataset() for device in devices]

            logging.info(f"Starting federated aggregation process on {len(federated_train_data)} devices.", extra=extra)

            averaged_weights = federated_aggregation(federated_train_data)

            # publishes on MQTT topic
            publication = self.client.publish("topic/fl-update", json.dumps(averaged_weights, cls=self.NumpyArrayEncoder), qos=1)
            logging.debug(f"Result code: {publication[0]} Mid: {publication[1]}", extra=extra)
            
            retries = 5
            while publication[0] != 0 and retries > 0:

                self.client.connect(MQTT_URL, MQTT_PORT, 60)
                publication = self.client.publish("topic/fl-update", json.dumps(averaged_weights, cls=self.NumpyArrayEncoder), qos=1)
                logging.debug(f"Result code: {publication[0]} Mid: {publication[1]}", extra=extra)
                retries -= 1
            
            logging.info("Sent update to 'topic/fl-update'", extra=extra)

            # print("Terminating aggregator...")
            # ActorSystem().tell(self, ActorExitRequest())

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
        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        collector = {}
        self.client = mqtt.Client(userdata = collector)
        self.client.connect(MQTT_URL, MQTT_PORT, 60)
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        
        self.client.loop_start()
