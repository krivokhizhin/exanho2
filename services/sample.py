import time

from exanho.common import Timer
from exanho.units import RPCHandler

class SampleService(RPCHandler):

    def echo(self, *args, **kwargs):
        return 'echo', args, kwargs

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