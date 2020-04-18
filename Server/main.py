from coordinator import CoordinatorActor

from thespian.actors import *
from common import *

import logging
extra = {'actor_name':'MAIN'}

if __name__ == "__main__":
    
    logging.basicConfig(format='%(asctime)s [%(actor_name)s] [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)

    # INIT SERVER ACTORS
    # ACTORS

    logging.info("starting", extra=extra)

    coordinator_instance = ActorSystem().createActor(CoordinatorActor)

    #ActorSystem().ask(coordinator_instance, Message(MsgType.GREETINGS, ''), 1)
    
    # TERMINATE ACTORS
    # ActorSystem().tell(coordinator_instance, ActorExitRequest())
    # ActorSystem().tell(selector_instance, ActorExitRequest())