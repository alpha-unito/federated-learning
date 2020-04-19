import logging
extra = {'actor_name':'MODEL-UTILS'}

import time
import warnings
import numpy as np
from common import Singleton
import keras

class ModelUtils(metaclass = Singleton):

    @staticmethod
    def federated_aggregation(federated_weights: list):
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

        self.current_weights = averaged_weights

        return averaged_weights


    def save_checpoint(self):
        self.model.set_weights(self.current_weights)
        logging.info(f"Set new weights.", extra=extra)
        
        self.epoch += 1
        self.model.save_weights(f"Averaged-Weights-MobileNetV2-{self.epoch}.hdf5")
        logging.info(f"Saved checkpoint 'Averaged-Weights-MobileNetV2-{self.epoch}.hdf5'.", extra=extra)


    def __init__(self):
        self.model = keras.applications.mobilenet_v2.MobileNetV2()
        self.current_weights = []
        self.epoch = 0
