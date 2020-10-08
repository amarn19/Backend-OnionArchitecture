import logging

def logger():
    # Logger configuration
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger