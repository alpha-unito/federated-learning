from thespian.actors import *
from common import *
import time
from aggregator import AggregatorActor
from selector import SelectorActor

import logging
extra = {'actor_name':'COORDINATOR'}

SLEEP_TIME = 60

class CoordinatorActor(Actor):
    
    def receiveMessage(self, message: Message, sender):
        if message.get_type() == MsgType.GREETINGS:

            # self.send(sender, 'Init global Coordinator')
            logging.info('Init global Coordinator', extra=extra)

            selector_instance = ActorSystem().createActor(SelectorActor)
            ActorSystem().ask(selector_instance, Message(MsgType.GREETINGS, 'hi'), 1)
            
            while True:
                """
                for i in range(1, wait + 1):
                    
                    if (i + 1) % 10 == 0:
                        logging.info('{} seconds until aggregation...'.format(wait - i), extra=extra)

                    time.sleep(1)
                """

                logging.info("60 seconds to aggregation...", extra=extra)
                time.sleep(30)

                logging.info("30 seconds to aggregation...", extra=extra)
                time.sleep(30)

                # define a new aggregator instance and make a request to selector passing it
                logging.info("Creating aggregator", extra=extra)

                aggregator_instance = ActorSystem().createActor(AggregatorActor)
                ActorSystem().ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)
