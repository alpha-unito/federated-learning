from thespian.actors import *
from datetime import datetime
from common import *
from main import aggregator_instance

class selector_actor(Actor):

    connected_devices = []
    
    def receiveMessage(self, message: Message, sender):
        if message.get_type() == MsgType.DEVICE:
            self.connected_devices.append("Device {}".format(datetime.now()))
            print(self.connected_devices)

        elif message.get_type() == MsgType.DEVICES_REQUEST:
            ActorSystem().ask(aggregator_instance, Message(MsgType.AGGREGATION, self.connected_devices), 1)            

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Selector!')