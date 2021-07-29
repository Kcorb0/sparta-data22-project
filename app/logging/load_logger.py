import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('loading.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
