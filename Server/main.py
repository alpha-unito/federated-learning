from coordinator import coordinator_actor
from aggregator import aggregator_actor
from selector import selector_actor

from flask import Flask, request
from flask_restful import Resource, Api
import json

from thespian.actors import *
from common import *

# ACTORS
coordinator_instance = ActorSystem().createActor(coordinator_actor)
selector_instance = ActorSystem().createActor(selector_actor)

class Selector(Resource):
    def get(self):
        print("get received")
        print(ActorSystem().ask(s, Message(MsgType.DEVICE, {'key':'value'}), 1))

# API
app = Flask(__name__)
api = Api(app)
api.add_resource(Selector, '/selector') # Route_1

if __name__ == "__main__":
    print(ActorSystem().ask(coordinator_instance, Message(MsgType.GREETINGS, 'hi'), 1))
    print(ActorSystem().ask(aggregator_instance, Message(MsgType.GREETINGS, 'hi'), 1))
    print(ActorSystem().ask(selector_instance, Message(MsgType.GREETINGS, 'hi'), 1))

    # START SERVER API
    app.run(port='5002')

    ActorSystem().tell(c, ActorExitRequest())
    ActorSystem().tell(a, ActorExitRequest())
    ActorSystem().tell(s, ActorExitRequest())