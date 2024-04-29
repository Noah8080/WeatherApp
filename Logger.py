import logging

# create logger and set level to debug
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) 

# Create a file handler and set the log level to debug
file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file handler
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)


