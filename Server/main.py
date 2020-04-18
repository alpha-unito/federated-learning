import logging
extra = {'actor_name':'MAIN'}

# create logger
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s [%(actor_name)s] [%(levelname)s] %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


from thespian.actors import *
from common import *

from coordinator import CoordinatorActor


if __name__ == "__main__":
    # INIT SERVER ACTORS
    logger.info("starting", extra=extra)

    coordinator_instance = ActorSystem().createActor(CoordinatorActor)

    ActorSystem().ask(coordinator_instance, Message(MsgType.GREETINGS, ''), 1)

    # TERMINATE ACTORS
    # ActorSystem().tell(coordinator_instance, ActorExitRequest())
    # ActorSystem().tell(selector_instance, ActorExitRequest())