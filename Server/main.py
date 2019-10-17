from coordinator import coordinator_actor
from aggregator import aggregator_actor
from selector import selector_actor

from thespian.actors import *

if __name__ == "__main__":
    c = ActorSystem().createActor(coordinator_actor)
    a = ActorSystem().createActor(aggregator_actor)
    s = ActorSystem().createActor(selector_actor)

    print(ActorSystem().ask(c, 'hi', 1))
    print(ActorSystem().ask(a, 'hi', 1))
    print(ActorSystem().ask(s, 'hi', 1))

    ActorSystem().tell(c, ActorExitRequest())
    ActorSystem().tell(a, ActorExitRequest())
    ActorSystem().tell(s, ActorExitRequest())