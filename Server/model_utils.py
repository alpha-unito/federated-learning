import logging
extra = {'actor_name':'MODEL-UTILS'}

import time
import warnings
import numpy as np
from common import Singleton
import re
import os
from os import listdir
from os.path import isfile, join
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import keras

class ModelUtils(metaclass = Singleton):

    def federated_aggregation(self, federated_weights: list):
        """
        ::param: federated_train_data   list containing client weights [W1, ... , Wn]
        """
        logging.info(f"Starting federated aggregation process on {len(federated_weights)} devices.", extra=extra)
                
        time_start = time.time()

        averaged_weights = []
        for weights_list_tuple in zip(*federated_weights):
            averaged_weights.append(
                np.array([np.array(weights_).mean(axis=0) for weights_ in zip(*weights_list_tuple)]))

        logging.info(f"[AGGR-TIME] Completed federated aggregation in {time.time() - time_start} seconds.", extra=extra)

        self.current_avg_weights = averaged_weights

        return averaged_weights


    def save_checkpoint(self):
        self.model.set_weights(self.current_avg_weights)
        logging.info(f"Set new weights.", extra=extra)
        
        self.epoch += 1
        self.model.save_weights(f"snapshots/Averaged-Weights-MobileNetV2-{self.epoch}.hdf5")
        logging.info(f"Saved checkpoint 'Averaged-Weights-MobileNetV2-{self.epoch}.hdf5'.", extra=extra)


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
        
        self.current_avg_weights = []
