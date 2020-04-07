import logging

def initialize():
    log = logging.getLogger(__name__)
    log.info(f'initialize')

def work():
    log = logging.getLogger(__name__)
    log.info(f'work')

def finalize():
    log = logging.getLogger(__name__)
    log.info(f'finalize')