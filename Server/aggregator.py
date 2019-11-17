from thespian.actors import *
from common import *
from model_utils import MODEL as model_fn

class aggregator_actor(Actor):

    def receiveMessage(self, message, sender):
        if message.get_type() == MsgType.DEVICES_REQUEST:
            print("aggregation process")
            # Training the model over the collected federated data
            iterative_process = tff.learning.build_federated_averaging_process(model_fn)
            # Let's invoke the initialize computation to construct the server state.
            state = iterative_process.initialize()
            
            """
            TODO: Let's run a New learning round. At this point you would pick a subset of your simulation 
            data from a new randomly selected sample of users for each round.
            """
            pass
        
        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')