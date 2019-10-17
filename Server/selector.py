from thespian.actors import *

class selector_actor(Actor):

    def receiveMessage(self, message, sender):
        self.send(sender, 'Hello, World from Selector!')