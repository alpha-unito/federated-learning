from thespian.actors import *

class coordinator_actor(Actor):

    def receiveMessage(self, message, sender):
        self.send(sender, 'Hello, World from Coordinator!')