import logging
extra = {'actor_name':'MODEL-UTILS'}

import time
import math
import warnings
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator

from common import Singleton
from imagenet_classes import classes as in_classes

import re
import os
from os import listdir
from os.path import isfile, join
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import keras

TOTAL_VAL_IMAGES = 50000
TARGET_SIZE = (224, 224)
BATCH_SIZE = 32

class ModelUtils(metaclass = Singleton):

    def federated_aggregation(self, federated_weights: list):
        """
        ::param: federated_train_data   list containing client weights [W1, ... , Wn]
        """
        logging.info(f"Starting federated aggregation process on {len(federated_weights)} devices.", extra=extra)
                
        time_start = time.time()

        # FEDERATED AVERAGING
        averaged_weights = []
        for weights_list_tuple in zip(*federated_weights):
            averaged_weights.append(
                np.array([np.array(weights_).mean(axis=0) for weights_ in zip(*weights_list_tuple)]))

        logging.info(f"[AGGR-TIME] Completed federated aggregation in {time.time() - time_start} seconds.", extra=extra)

        # set new weights
        self.current_avg_weights = averaged_weights
        self.model.set_weights(self.current_avg_weights)
        logging.info(f"Set new weights.", extra=extra)
        
        # make test on validation iterator
        logging.info(f"evaluate model in {self.val_steps} steps")
        score = self.model.evaluate_generator(self.valid_it, steps=self.val_steps, use_multiprocessing=True, verbose=1)
        logging.info("Loss: ", score[0], "Accuracy: ", score[1])
        
        self.epoch += 1

        #SAVES CHECKPOINT
        self.save_checkpoint()
        
        #SAVES LOG
        self.save_log(len(federated_weights))
        
        return averaged_weights


    def save_log(self, nodes = 0):
        #log
        with open('./snapshots/log.csv', 'a') as fd:
            if self.epoch == 0:
                fd.write("epoch;nodes;validation_accuracy;validation_loss\n")

            fd.write(f"{self.epoch};{nodes}{logs.get('val_accuracy', '')};{logs.get('val_loss', '')}\n")

        logging.info(f"Saved log on 'snapshots/log.csv'.", extra=extra)


    def save_checkpoint(self):
        self.model.save_weights(f"snapshots/Averaged-Weights-MobileNetV2-{self.epoch}.hdf5")
        logging.info(f"Saved checkpoint 'Averaged-Weights-MobileNetV2-{self.epoch}.hdf5'.", extra=extra)


    def generate_validation_iterator(self):
        # IMAGES
        validation_images_path = './res/ILSVRC2012_img_val/val/'
        validations_labels_path = './res/ILSVRC2012_devkit_t12/data/ILSVRC2012_validation_ground_truth.txt'

        validation_x = [f for f in listdir(validation_images_path)
                        if isfile(join(validation_images_path, f))]
        validation_x.sort()

        # LABELS
        with open(validations_labels_path) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        validation_y = [in_classes[int(x.strip())][0] for x in content]

        # merge images and labels
        validation_sequence = [[validation_x[i], validation_y[i]] for i in range(0, len(validation_x))]
        validation_dataframe = pd.DataFrame(validation_sequence, columns = ['x', 'y'])

        # create generator
        datagen = ImageDataGenerator()

        valid_it = datagen.flow_from_dataframe(
            dataframe=validation_dataframe,
            directory=validation_images_path,
            x_col='x',
            y_col='y',
            target_size=TARGET_SIZE,
            class_mode="categorical",
            color_mode= 'rgb',
            batch_size=BATCH_SIZE)

        return valid_it


    def get_last_weights(self, path):
        weights = [join(path, f) for f in listdir(path)
                if isfile(join(path, f)) and 'Averaged-Weights' in f]

        weights.sort(reverse=True)

        return weights


    def __init__(self):
        try:
            os.mkdir("snapshots")
        except:
            pass

        self.model = keras.applications.mobilenet_v2.MobileNetV2()
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
        
        self.current_avg_weights = self.model.get_weights()

        """
        VALIDATION ITERATOR
        """
        logging.info(f"Generating train iterator from './res/ILSVRC2012_img_val/val/') ...")
        ts = time.time()

        self.valid_it = self.generate_validation_iterator()
        self.val_steps = math.ceil(TOTAL_VAL_IMAGES / BATCH_SIZE)

        te = time.time()

        logging.info(f"Train iterator finished in {te - ts} seconds ({(te - ts) / 60} minutes)\n")

