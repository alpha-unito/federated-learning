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



if __name__ == "__main__":
    # INIT SERVER ACTORS
    logger.info("1", extra=extra)

    from thespian.actors import *
    logger.info("2", extra=extra)

    from common import *
    logger.info("3", extra=extra)

    import time
    logger.info("4", extra=extra)

    from aggregator import AggregatorActor
    logger.info("5", extra=extra)

    from selector import SelectorActor
    logger.info("6", extra=extra)

    from coordinator import CoordinatorActor
    logger.info("7", extra=extra)
