import logging
extra = {'actor_name':'MODEL-UTILS'}

import time
import warnings
import numpy as np
np.random.seed(0)

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

    return averaged_weights
