import fl_runtime
import time

client_id = int(time.time())

if __name__ == "__main__":
    
    task = fl_runtime.FederatedTask()

    while True:
        print(f"[CLIENT {client_id}]")
        print(" - Insert 1 for start learning task")
        print(" - Insert 2 for communicate the result to the FL server")

        choice = input()

        if choice == '1':
            task.training()
        elif choice == '2':
            task.device_connection_to_server()
        else:
            print("Invalid option.\n")
