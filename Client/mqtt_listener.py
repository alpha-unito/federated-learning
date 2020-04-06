import paho.mqtt.client as mqtt
import threading
import json


class MqttListener():
    
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("\nConnected with result code {code} to topic 'topic/fl-update' \n".format(code = rc))
        print('subscribe', client.subscribe("topic/fl-update"))


    @staticmethod
    def on_message(client, userdata, msg):
        print("\nNew model update received ")

        try:
            weights = json.loads(msg.payload)          
            
            print(f"Loading Weights from message ...")
            
            userdata['model'].set_weights(weights)
            
            print("Model weights updated successfully.\n")

        except Exception as e:
            print('Error updating model:', e)
    

    @staticmethod
    def mqtt_listener(client):
        print("Start listening on MQTT channel ...")
        client.loop_forever()
        print("End listening on MQTT channel.")
    


    def __init__(self, url: str, port: int, collector: dict, keep_alive: int = 60):
        print('Init client update MQTT listener', url, port, collector)

        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        client = mqtt.Client(userdata = collector)
        
        client.connect(url, port, keep_alive)

        client.on_connect = self.on_connect
        client.on_message = self.on_message
        
        # START NEW THREAD WITH MQTT LISTENER
        thr = threading.Thread(target = self.mqtt_listener, args = [client])
        try:
            thr.start() # Will run thread
            print('thread started')
        except:
            print('error on thread')