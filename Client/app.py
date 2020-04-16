import fl_runtime
import time

client_id = int(time.time())

if __name__ == "__main__":
    
    task = fl_runtime.FederatedTask()

    print(f"[CLIENT {client_id}]")

    task.training()

    task.send_local_update_to_server()
    