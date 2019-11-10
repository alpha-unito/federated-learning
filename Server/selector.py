from thespian.actors import *
from datetime import datetime
from common import *
# import requests 
# import asyncio
import paho.mqtt.client as mqtt
import threading

class selector_actor(Actor):

    # ********* MQTT COMMUNICATION **********************
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("topic/fl-broadcast")


    def on_message(client, userdata, msg):
        print("Device communication received ")
        if msg.payload.decode() == "Hello world!":
            print("Yes!")
            connected_devices.append("Device {}".format(datetime.now()))

    
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
            # pass
            ActorSystem().ask(aggregator_instance, Message(MsgType.AGGREGATION, self.connected_devices), 1)            

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Selector!')


    connected_devices = []

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