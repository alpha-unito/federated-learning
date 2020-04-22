import logging

# create logger
logger = logging.getLogger('custom_logger')

import datetime
import json
import paho.mqtt.client as mqtt
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator
from json import JSONEncoder
import numpy
import math

import time

MQTT_URL = 'localhost'
MQTT_PORT = 1883


IMAGENET_PATH = '/media/lore/EA72A48772A459D9/ILSVRC2012/ILSVRC2012_img_train/subset01'
TOTAL_IMAGES = 100
TARGET_SIZE = (224, 224)
BATCH_SIZE = 20
EPOCHS = 1


class FederatedTask():

    def wait_for_update_from_server(self):
        while True:
            time.sleep(10)

            if self.new_weights['update'] is not None:
                #  set new weights
                self.receive_update_from_server(self.new_weights['update'])
                
                # reset
                self.new_weights['update'] = None


    def receive_update_from_server(self, weights):
        logger.info("Updated weights received")

        self.model.set_weights(weights)

        logger.info("Model weights updated successfully.")

        self.training()

        self.send_local_update_to_server()


    def training(self):

        time_start = time.time()

        self.model.fit_generator(self.train_it, steps_per_epoch=math.ceil(TOTAL_IMAGES / BATCH_SIZE), epochs=EPOCHS)

        logger.info(f"[TRAIN-TIME] Completed local training in {time.time() - time_start / 60} minutes.")

        return self.model


    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)


    def send_local_update_to_server(self):

        # select training data related to selected clients
        model_weights = self.model.get_weights()

        # build message object
        send_msg = {
            'device': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': model_weights
        }

        # publishes on MQTT topic
        publication = self.client.publish("topic/fl-broadcast", json.dumps(send_msg, cls=self.NumpyArrayEncoder), qos=1);
        logger.debug(f"Result code: {publication[0]} Mid: {publication[1]}")

        while publication[0] != 0:
            self.client.connect(MQTT_URL, MQTT_PORT, 60)
            publication = self.client.publish("topic/fl-broadcast", json.dumps(send_msg, cls=self.NumpyArrayEncoder), qos=1);
            logger.debug(f"Result code: {publication[0]} Mid: {publication[1]}")


    @staticmethod
    def on_message(client, userdata, msg):
        logger.info("New model update received ")

        try:
            logger.info("Loading Weights from message ...")
            weights = json.loads(msg.payload)

            logger.info("Weights loaded successfully")

            userdata['new_weights']['update'] = weights

        except Exception as e:
            logger.warning(f'Error loading weights: {e}')


    @staticmethod
    def on_publish(client, userdata, mid):
        logger.info(f"published message to 'topic/fl-broadcast' with mid: {mid}")


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to broker")
            client.subscribe("topic/fl-update")

        else:    
            logger.info("Connection failed. Retrying in 1 second...")
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)


    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        logger.info("Subscribed to topic/fl-update")


    def __init__(self):
        # INIT MODEL
        self.model = keras.applications.mobilenet_v2.MobileNetV2()
        self.model.summary()
        # Compile the model
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        # create generator
        datagen = ImageDataGenerator()
        # prepare an iterators for each dataset
        self.train_it = datagen.flow_from_directory(IMAGENET_PATH,
                                            target_size=TARGET_SIZE,
                                            class_mode='categorical',
                                            color_mode='rgb',
                                            batch_size=BATCH_SIZE)

        # create mqtt client
        self.new_weights = {'update': None}

        self.client = mqtt.Client(userdata={'new_weights': self.new_weights})
        self.client.connect(MQTT_URL, MQTT_PORT, 60)
        # callbacks    
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_publish = self.on_publish
        self.client.on_message = self.on_message

        
        self.client.loop_start()
