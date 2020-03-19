from functools import wraps
import logging

from . import Timer


def try_logged(func):
    log = logging.getLogger(func.__module__)
    timer = Timer()

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            with timer:
                result = func(*args, **kwargs)
            log.info(f'{func.__name__}(), OK: {timer}')
        except Exception as ex:
            log.exception(ex)
            result = ex.args
        finally:
            timer.reset()
        return result
    return wrapper
