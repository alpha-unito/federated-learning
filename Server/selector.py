from thespian.actors import *
from datetime import datetime
from common import *
# import requests 
# import asyncio
import paho.mqtt.client as mqtt
import threading
import json
import collections
import numpy as np
from numpy import array

#TODO: REMOVE
from aggregator import aggregator_actor

class selector_actor(Actor):

    connected_devices = []

    # ********* MQTT COMMUNICATION **********************
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("topic/fl-broadcast")

    def on_message(client, userdata, msg):
        print("\nDevice communication received ")

        try:            

            msg_obj = json.loads(msg.payload)
            print('device: ', msg_obj['device'])

            data = collections.OrderedDict([
                (key, np.asarray(value, dtype=np.float32))
                for key, value in msg_obj['data'].items()
            ])                
            
            print(data)
            device = Device(msg_obj['device'], data)
            ActorSystem().ask(ActorSystem().createActor(aggregator_actor), Message(MsgType.AGGREGATION, [device]), 1)
        
        except expression as identifier:
            print('Unsupported Device X', identifier)
    
    def mqtt_listener(client):
        print("loop forever")
        client.loop_forever()
        print("finished loop forever")
    
    # ***************************************************

    def receiveMessage(self, message: Message, sender):
        """
        Actor for devices selection and aggregation call
        """
        if message.get_type() == MsgType.DEVICES_REQUEST:
            aggregator_instance = message.get_body()
            
            if len(self.connected_devices) > 0:
                print("\nStarting aggregation...\n")
                ActorSystem().ask(aggregator_instance, Message(MsgType.AGGREGATION, self.connected_devices), 1)
            else:
                print("\nNo devices connected, skipping aggregation. \n")

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Selector!')


    # MQTT CLIENT CONNECTION TO MESSAGE BROKER
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)

    client.on_connect = on_connect
    client.on_message = on_message
    
    # START NEW THREAD WITH MQTT LISTENER
    thr = threading.Thread(target=mqtt_listener, args=[client])
    thr.start() # Will run thread
    # thr.is_alive() # Will return whether foo is running currently
    # thr.join() # Will wait till "foo" is done