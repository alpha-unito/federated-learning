import datetime
import json
import paho.mqtt.client as mqtt
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator
from json import JSONEncoder
import numpy
from mqtt_listener import MqttListener
import math

import time

MQTT_URL = 'localhost'
MQTT_PORT = 1883


IMAGENET_PATH = './res/'
TOTAL_IMAGES = 100
TARGET_SIZE = (224, 224)
BATCH_SIZE = 20
EPOCHS = 1


class FederatedTask():

    def training(self):
        self.model.summary()

        # Compile the model
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # create generator
        datagen = ImageDataGenerator()

        # prepare an iterators for each dataset
        train_path = "./res"
        train_it = datagen.flow_from_directory(train_path,
                                            target_size=TARGET_SIZE,
                                            class_mode='categorical',
                                            color_mode='rgb',
                                            batch_size=BATCH_SIZE)

        batchX, batchY = train_it.next()

        print("batchX shape: ", batchX.shape)
        print("batchY shape: ", batchY.shape)

        self.model.fit_generator(train_it, steps_per_epoch=math.ceil(TOTAL_IMAGES / BATCH_SIZE), epochs=EPOCHS)

        return self.model


    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)


    def device_connection_to_server(self):

        # select training data related to selected clients
        model_weights = self.model.get_weights()

        # build message object
        send_msg = {
            'device': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data': model_weights
        }

        # publishes on MQTT topic
        publication = self.client.publish("topic/fl-broadcast", json.dumps(send_msg, cls=self.NumpyArrayEncoder), qos=1);
        mid = publication[1]
        print(f"Result code: {publication[0]}")
        print(f"Request to send mid: {mid}")

        while publication[0] != 0:
            self.client.connect(MQTT_URL, MQTT_PORT, 60)
            publication = self.client.publish("topic/fl-broadcast", json.dumps(send_msg, cls=self.NumpyArrayEncoder), qos=1);
            print(f"Result code: {publication[0]}")


    def on_publish(client, userdata, mid):
        print(f"\npublished message to 'topic/fl-broadcast' with mid: {mid}")
        userdata['acks'].append(mid)


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.loop_start()

        else:    
            print("Connection failed")
            
            print("Retrying ...")
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)

    
    def __init__(self):
        self.model = keras.applications.mobilenet_v2.MobileNetV2()

        self.client = mqtt.Client()
        self.client.connect(MQTT_URL, MQTT_PORT, 60)
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish

        self.acks = []

        # MQTT init for model update
        properties = {'model': self.model, 'acks': self.acks}
        self.mqtt_listener = MqttListener(MQTT_URL, MQTT_PORT, properties)

