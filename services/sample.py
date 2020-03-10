import logging
import time

from exanho.common import try_logged, Timer
from exanho.units import RPCHandler

class SampleService(RPCHandler):

    logger = logging.getLogger(__name__)

    @try_logged
    def echo(self, *args, **kwargs):
        return 'echo', args, kwargs

    @try_logged
    def load(self, load = 10000000):
        timer = Timer()
        with timer:
            n = int(load)
            i = j = k = 0
            while i < n:
                while j < n:
                    while k < n:
                        k += 1
                    j += 1
                i += 1
        return 'load', timer.elapsed

    @try_logged
    def raise_ex(self, message = 'raise Exception'):
        raise Exception(message)