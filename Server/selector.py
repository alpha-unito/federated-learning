from thespian.actors import *
from datetime import datetime
from common import *

from mqtt_listener import MqttListener


class SelectorActor(Actor):

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


    def __init__(self):
        super().__init__()
        self.properties = {'connected_devices': []}
        mqtt_listener = MqttListener('localhost', 1883, self.properties)
