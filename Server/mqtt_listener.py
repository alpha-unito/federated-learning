import paho.mqtt.client as mqtt
import threading
import json
from common import *
from thespian.actors import *


class MqttListener():
    
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("\nConnected with result code {code}\n".format(code = rc))
        client.subscribe("topic/fl-broadcast")


    @staticmethod
    def on_message(client, userdata, msg):
        print("\nDevice communication received ")

        try:            
            print('cast message obj to Device')
            msg_obj = json.loads(msg.payload)
            print('device: ', msg_obj['device'])

            device = Device(msg_obj['device'], msg_obj['data'])
            
            userdata['connected_devices'].append(device)

        except:
            print('Unsupported Device X')
    

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
        client.on_message = self.on_message
        
        # START NEW THREAD WITH MQTT LISTENER
        thr = threading.Thread(target = self.mqtt_listener, args = [client])
        try:
            thr.start() # Will run thread
        except:
            print('error on thread')