import logging

# create logger
logger = logging.getLogger('custom_logger')


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

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
import re
import os
from os import listdir
from os.path import isfile, join

MQTT_URL = '172.20.8.119'
MQTT_PORT = 1883


IMAGENET_PATH = '/mnt/dataset/subset'
TOTAL_IMAGES = 82000
TARGET_SIZE = (224, 224)
BATCH_SIZE = 32
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

        train_history = self.model.fit_generator(self.train_it, steps_per_epoch=math.ceil(TOTAL_IMAGES / BATCH_SIZE), epochs=EPOCHS)

        logger.info(f"[TRAIN-TIME] Completed local training in {(time.time() - time_start) / 60} minutes.")

        self.epoch += 1

        #SAVES CHECKPOINT
        self.save_checkpoint()
        
        #SAVES LOG
        print(train_history.history)
        self.save_log(train_history.history['loss'][-1], train_history.history['accuracy'][-1], (time.time() - time_start))
        
        return self.model


    def save_log(self, loss, accuracy, time):
        #log
        with open('./snapshots/log.csv', 'a') as fd:
            if self.epoch == 0:
                fd.write("epoch;accuracy;loss;time\n")

            fd.write(f"{self.epoch};{accuracy};{loss};{time}\n")

        logger.info(f"Saved log on 'snapshots/log.csv'.")


    def save_checkpoint(self):
        self.model.save_weights("snapshots/Local-Weights-node01-MobileNetV2-{epoch:02d}.hdf5".format(epoch=self.epoch))
        logger.info("Saved checkpoint 'Local-Weights-node01-MobileNetV2-{epoch:02d}.hdf5'.".format(epoch=self.epoch))


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
            'device': self.client_id,
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


    def get_last_weights(self, path):
        weights = [join(path, f) for f in listdir(path)
                if isfile(join(path, f)) and 'Averaged-Weights' in f]

        weights.sort(reverse=True)

        return weights


    def __init__(self, client_id=-1):

        self.client_id = client_id

        try:
            os.mkdir("snapshots")
        except:
            pass

        # INIT MODEL
        self.model = keras.applications.mobilenet_v2.MobileNetV2()
        self.model.summary()
        # Compile the model
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        weights_checkpoints = self.get_last_weights('./snapshots')
        self.epoch = 0

        if len(weights_checkpoints) > 0:
            logging.info(f"Loading Weights from {weights_checkpoints[0]} ...", extra=extra)
            self.model.load_weights(weights_checkpoints[0])
            logging.info("Done.\n", extra=extra)

            # get last epoch number
            p = re.compile("-(\w+).hdf5")
            result = p.search(weights_checkpoints[0])
            self.epoch = int(result.group(1))

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
