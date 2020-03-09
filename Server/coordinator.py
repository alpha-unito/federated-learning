from thespian.actors import *
from common import *
import time
from aggregator import AggregatorActor

class CoordinatorActor(Actor):

    def receiveMessage(self, message: Message, sender):
        if message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Coordinator!')
            """
            wait = 60
            #while True:
            for i in range(1, wait + 1):
                if (i + 1) % 10 == 0:
                    print('{} seconds until aggregation...'.format(wait - i))
                
                time.sleep(1)
            """

            # define a new aggregator instance and make a request to selector passing it
            aggregator_instance = ActorSystem().createActor(AggregatorActor)
            selector_instance = message.get_body()
            ActorSystem().ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)
