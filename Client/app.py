import fl_runtime
import time

import logging

client_id = int(time.time())

if __name__ == "__main__":
    
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)

    logging.info(f"[CLIENT {client_id}]")

    task = fl_runtime.FederatedTask()
    task.training()

    task.send_local_update_to_server()
    
    task.wait_for_update_from_server()