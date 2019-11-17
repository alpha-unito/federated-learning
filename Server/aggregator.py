from thespian.actors import *
from common import *
import datetime
import tensorflow as tf
import tensorflow_federated as tff
from model_utils import get_model

class aggregator_actor(Actor):

    def receiveMessage(self, message, sender):
        if message.get_type() == MsgType.AGGREGATION:
            print("\n**Aggregation process**\n")

            # Training the model over the collected federated data
            iterative_process = tff.learning.build_federated_averaging_process(get_model())
            
            # Let's invoke the initialize computation to construct the server state.
            state = iterative_process.initialize()
            
            """
            TODO: Let's run a New learning round. At this point you would pick a subset of your simulation 
            data from a new randomly selected sample of users for each round.
            """
            state, metrics = iterative_process.next(state, federated_train_data)
            print('round  {0}, metrics={1}'.format(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), metrics))

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')