import logging
import time
from threading import Thread
from multiprocessing import Queue
import logging.config
import logging.handlers

def start_log_listener(logging_config, logging_maxsize):
    logging.config.fileConfig(logging_config)
    log_queue = Queue(logging_maxsize)
    log_listener = Thread(target=logger_thread, args=(log_queue, ))
    log_listener.daemon = True
    log_listener.start()

    while not log_listener.is_alive:
        time.sleep(1)

    return log_listener, log_queue

def logger_thread(queue): 
    while True:
        try:
            record = queue.get()
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)