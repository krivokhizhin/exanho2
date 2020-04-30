import logging

def configurer_logging(queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    root = logging.getLogger('root')
    root.addHandler(h)
    root.setLevel(logging.DEBUG)