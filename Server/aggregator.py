from thespian.actors import *
from common import *

class aggregator_actor(Actor):

    def receiveMessage(self, message, sender):
        if message.get_type() == MsgType.DEVICES_REQUEST:
            # aggregation process
            print("aggregation process")
            pass
        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')