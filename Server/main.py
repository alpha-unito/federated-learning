from coordinator import coordinator_actor
from selector import selector_actor

from model_utils import init_model

from thespian.actors import *
from common import *

# ACTORS
coordinator_instance = ActorSystem().createActor(coordinator_actor)
selector_instance = ActorSystem().createActor(selector_actor)

if __name__ == "__main__":
    # INIT FEDERATED LEARNING MODEL
    init_model()

    # INIT SERVER ACTORS
    print(ActorSystem().ask(coordinator_instance, Message(MsgType.GREETINGS, selector_instance), 1))
    print(ActorSystem().ask(selector_instance, Message(MsgType.GREETINGS, 'hi'), 1))

    # TERMINATE ACTORS
    # ActorSystem().tell(coordinator_instance, ActorExitRequest())
    # ActorSystem().tell(selector_instance, ActorExitRequest())