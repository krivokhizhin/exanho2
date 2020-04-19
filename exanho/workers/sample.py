import logging

log = logging.getLogger(__name__)

def initialize(appsettings=None):
    log.info(f'initialize')
    return appsettings if appsettings else object()

def work(context):
    log.info(f'work')
    return context

def finalize(context):
    log.info(f'finalize')