from thespian.actors import *

class aggregator_actor(Actor):

    def receiveMessage(self, message, sender):
        self.send(sender, 'Hello, World from Aggregator!')