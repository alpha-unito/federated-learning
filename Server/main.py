import logging
logging.basicConfig(level=logging.DEBUG)

extra = {'actor_name':'MAIN'}

class actorLogFilter(logging.Filter):
    def filter(self, logrecord):
        return 'actorAddress' in logrecord.__dict__
class notActorLogFilter(logging.Filter):
    def filter(self, logrecord):
        return 'actorAddress' not in logrecord.__dict__

logcfg = { 'version': 1,
           'formatters': {
               'normal': {'format': '%(asctime)s [%(levelname)s][%(actor_name)s] %(message)s'},
               'actor': {'format': '%(asctime)s [%(levelname)s] %(actorAddress)s => %(message)s'}},
           'filters': { 'isActorLog': { '()': actorLogFilter},
                        'notActorLog': { '()': notActorLogFilter}},
           'handlers': { 'h1': {'class': 'logging.StreamHandler',
                                'formatter': 'normal',
                                'filters': ['notActorLog'],
                                'level': logging.INFO},
                         'h2': {'class': 'logging.StreamHandler',
                                'formatter': 'actor',
                                'filters': ['isActorLog'],
                                'level': logging.INFO},},
           'loggers' : { '': {'handlers': ['h1', 'h2'], 'level': logging.DEBUG}}
         }


from thespian.actors import *
from common import *

from coordinator import CoordinatorActor


if __name__ == "__main__":
    # INIT SERVER ACTORS
    actor_system = ActorSystem(logDefs=logcfg)
    logging.info("starting", extra=extra)
    coordinator_instance = actor_system.createActor(CoordinatorActor)

    logging.info("starting 2", extra=extra)

    actor_system.ask(coordinator_instance, Message(MsgType.GREETINGS, ''), 1)
    logging.info("starting 3", extra=extra)

    # TERMINATE ACTORS
    # ActorSystem(logDefs={}).tell(coordinator_instance, ActorExitRequest())
    # ActorSystem(logDefs={}).tell(selector_instance, ActorExitRequest())