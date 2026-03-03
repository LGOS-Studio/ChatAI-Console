# utils/logger.py
import logging
import config
import os

def setup_logger(name="LGOS_AI"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(getattr(logging, config.LOG_LEVEL))
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger