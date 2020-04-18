import logging

# create logger
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

import fl_runtime
import time

client_id = int(time.time())


if __name__ == "__main__":
    
    logger.info(f"[CLIENT {client_id}]")

    task = fl_runtime.FederatedTask()
    task.training()

    task.send_local_update_to_server()
    
    task.wait_for_update_from_server()