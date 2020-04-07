import paho.mqtt.client as mqtt
import threading
import json
from common import *
from thespian.actors import *


class MqttListener():
    

    @staticmethod
    def on_message(client, userdata, msg):
        print("\nDevice communication received ")

        try:            
            print('cast message obj to Device')
            msg_obj = json.loads(msg.payload)
            print('device: ', msg_obj['device'])

            new_device = Device(msg_obj['device'], msg_obj['data'])

        except:
            print('Unsupported Device X')

        for i in range(len(userdata['connected_devices'])):
            # replace with new weights
            if userdata['connected_devices'][i].get_id() == new_device.get_id():
                print("Device already present, replacing ...")
                userdata['connected_devices'][i] = new_device
                
            break
        
        # append new device
        if i == len(userdata['connected_devices']):
            print("Adding new device ...")
            userdata['connected_devices'].append(new_device)
    

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print("Subscribed to topic/fl-broadcast")


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            client.subscribe("topic/fl-broadcast")

        else:    
            print("Connection failed")
            
            print("Retrying ...")
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)


    @staticmethod
    def mqtt_listener(client):
        print("Start listening on MQTT channel ...")
        client.loop_forever()
        print("End listening on MQTT channel.")
    

    def __init__(self, url: str, port: int, collector: dict, keep_alive: int = 60):
        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        client = mqtt.Client(userdata = collector)
        
        client.connect(url, port, keep_alive)

        client.on_connect = self.on_connect
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message
        
        # START NEW THREAD WITH MQTT LISTENER
        thr = threading.Thread(target = self.mqtt_listener, args = [client])
        try:
            thr.start() # Will run thread
        except:
            print('error on thread')