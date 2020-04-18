import logging
extra = {'actor_name':'MQTT-LISTENER'}

import paho.mqtt.client as mqtt
import threading
import json
from common import *
from thespian.actors import *


class MqttListener():
    

    @staticmethod
    def on_message(client, userdata, msg):
        logging.info("Device communication received", extra=extra)

        try:            
            msg_obj = json.loads(msg.payload)
            logging.info(f"device: {msg_obj['device']}", extra=extra)

            new_device = Device(msg_obj['device'], msg_obj['data'])

        except:
            logging.warning(f"Unsupported device message.", extra=extra)

        i = 0
        while i < len(userdata['connected_devices']):
            # replace with new weights
            if userdata['connected_devices'][i].get_id() == new_device.get_id():
                logging.warning("Device already present, replacing ...", extra=extra)
    
                userdata['connected_devices'][i] = new_device
                break
            i+=1
        
        # append new device
        if i == len(userdata['connected_devices']):
            logging.info("Adding new device ...", extra=extra)    
            userdata['connected_devices'].append(new_device)

        logging.info("Device successfully added.", extra=extra)


    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        logging.info("Subscribed to topic/fl-broadcast", extra=extra)


    @staticmethod
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected to broker", extra=extra)
            client.subscribe("topic/fl-broadcast")

        else:    
            logging.info("Connection failed. Retrying in 1 second...", extra=extra)
            
            time.sleep(1)
            self.client.connect(MQTT_URL, MQTT_PORT, 60)


    def __init__(self, url: str, port: int, collector: dict, keep_alive: int = 60):
        # MQTT CLIENT CONNECTION TO MESSAGE BROKER
        client = mqtt.Client(userdata = collector)
        #client.enable_logging(logging)
        
        client.connect(url, port, keep_alive)

        client.on_connect = self.on_connect
        client.on_subscribe = self.on_subscribe
        client.on_message = self.on_message
        
        client.loop_start()
