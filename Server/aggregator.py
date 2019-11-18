from thespian.actors import *
from common import *
from model_utils import build_test_clients, federated_aggregation


class aggregator_actor(Actor):

    def receiveMessage(self, message, sender):
        if message.get_type() == MsgType.AGGREGATION:
            print("\n**Aggregation process**\n")
            devices = message.get_body()
            
            federated_train_data = [device.get_dataset() for device in devices]

            federated_aggregation(federated_train_data)

        elif message.get_type() == MsgType.GREETINGS:
            self.send(sender, 'Hello, World from Aggregator!')