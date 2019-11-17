from thespian.actors import *
from common import *
import time

class coordinator_actor(Actor):

    def receiveMessage(self, message, sender):
        if message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Coordinator!')
            
            time.sleep(30)

            # define a new aggregator instance and make a request to selector passing it
            aggregator_instance = ActorSystem().createActor(aggregator_actor)
            ActorSystem().ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)
            