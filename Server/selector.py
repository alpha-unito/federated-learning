import logging
extra = {'actor_name':'SELECTOR'}

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
            
            if len(self.properties['connected_devices']) > 0:
                logging.info(f"Starting aggregation on {len(self.properties['connected_devices'])} devices...", extra=extra)

                ActorSystem(logDefs={}).ask(aggregator_instance, Message(MsgType.AGGREGATION, self.properties['connected_devices']), 1)
                self.properties['connected_devices'] = []
                
            else:
                logging.warning("No devices connected, skipping aggregation.", extra=extra)

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Init Selector')

    def __init__(self):
        super().__init__()
        self.properties = {'connected_devices': []}
        mqtt_listener = MqttListener('localhost', 1883, self.properties)
