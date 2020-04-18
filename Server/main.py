from coordinator import CoordinatorActor

from thespian.actors import *
from common import *


if __name__ == "__main__":

    # INIT SERVER ACTORS
    # ACTORS
    coordinator_instance = ActorSystem().createActor(CoordinatorActor)

    print(ActorSystem().ask(coordinator_instance, Message(MsgType.GREETINGS, ''), 1))
    
    # TERMINATE ACTORS
    # ActorSystem().tell(coordinator_instance, ActorExitRequest())
    # ActorSystem().tell(selector_instance, ActorExitRequest())