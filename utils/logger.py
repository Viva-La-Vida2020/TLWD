import logging
import pdb
# Ignore warnings
import warnings

warnings.filterwarnings("ignore")
import json

'''Logging Modules'''


def get_logger(name, log_file_path='./logs/temp.log', logging_level=logging.INFO,
               log_format='%(asctime)s | %(levelname)s | %(filename)s: %(lineno)s : %(funcName)s() ::\t %(message)s'):
    logger = logging.getLogger(name)
    logger.setLevel(logging_level)
    formatter = logging.Formatter(log_format)

    file_handler = logging.FileHandler(log_file_path, mode='w')
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging_level)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def print_log(logger, dict):
    string = ''
    for key, value in dict.items():
        string += '\n {}: {}\t'.format(key.replace('_', ' '), value)
    logger.info(string)
