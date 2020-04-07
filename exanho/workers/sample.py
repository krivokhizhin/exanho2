import logging

log = logging.getLogger(__name__)

def initialize(*args, **kwargs):
    log.info(f'initialize')

def work():
    log.info(f'work')

def finalize():
    log.info(f'finalize')