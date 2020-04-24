import logging
extra = {'actor_name':'COORDINATOR'}

from thespian.actors import *
from common import *
import time

from aggregator import AggregatorActor
from selector import SelectorActor

SLEEP_TIME = 60 * 120 
#SLEEP_TIME = 60 

class CoordinatorActor(Actor):
    

    def receiveMessage(self, message: Message, sender):
        if message.get_type() == MsgType.GREETINGS:
        
            # self.send(sender, 'Init global Coordinator')
            logging.info('Init global Coordinator', extra=extra)

            #selector
            selector_instance = ActorSystem(logDefs={}).createActor(SelectorActor)
            ActorSystem(logDefs={}).ask(selector_instance, Message(MsgType.GREETINGS, 'hi'), 1)
            
            # aggregator
            aggregator_instance = ActorSystem(logDefs={}).createActor(AggregatorActor)
            ActorSystem(logDefs={}).ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)

            while True:
                
                for i in range(0, SLEEP_TIME):
                    #if i % 10 == 0:
                    if i % (60 * 10) == 0:
                        #logging.info(f'Minutes until aggregation: {(SLEEP_TIME - i) / 60}', extra=extra)
                        logging.info(f'Seconds until aggregation: {(SLEEP_TIME - i)}', extra=extra)
                    time.sleep(1)

                # define a new aggregator instance and make a request to selector passing it
                logging.info("Creating aggregator", extra=extra)

                
                ActorSystem(logDefs={}).ask(selector_instance, Message(MsgType.DEVICES_REQUEST, aggregator_instance), 1)
