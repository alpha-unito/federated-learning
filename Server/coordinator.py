from thespian.actors import *
from common import *
import time
from aggregator import aggregator_actor

class coordinator_actor(Actor):

    def receiveMessage(self, message: Message, sender):
        if message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Coordinator!')
            
            while True:
                for i in range(1,61):
                    print('Waiting {}...'.format(i))
                    time.sleep(1)

                # define a new aggregator instance and make a request to selector passing it
                aggregator_instance = ActorSystem().createActor(aggregator_actor)
                selector_instance = message.get_body()
                ActorSystem().ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)
                