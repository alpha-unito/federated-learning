import logging
extra = {'actor_name':'COORDINATOR'}

logging.basicConfig(format='%(asctime)s [%(actor_name)s] [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG)

logging.warning('is when this event was logged.', extra=extra)
logging.info('is when this event was logged.', extra=extra)