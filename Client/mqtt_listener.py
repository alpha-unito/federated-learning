import paho.mqtt.client as mqtt
import threading
import json


class MqttListener():


    @staticmethod
    def on_message(client, userdata, msg):
        print("\nNew model update received ")

        try:
            weights = json.loads(msg.payload)          
            
            print(f"Loading Weights from message ...")
            
            userdata['callback'].set_weights(weights)
            
            print("Model weights updated successfully.\n")

        except Exception as e:
            print('Error updating model:', e)


    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed to topic/fl-update")
    

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.subscribe("topic/fl-update")

        else:    
            print("Connection failed")
            
            print("Retrying ...")
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)
  


    def __init__(self, url: str, port: int, collector: dict, keep_alive: int = 60):
        print('Init client update MQTT listener', url, port, collector)

        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        client = mqtt.Client(userdata = collector)
        
        client.connect(url, port, keep_alive)

        client.on_connect = self.on_connect
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message

        client.loop_start()

        