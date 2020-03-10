import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None
    
    def reset(self):
        self.elapsed = 0.0

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def __str__(self):
        if self.elapsed > 1:
            return f'{self.elapsed:0.2f} s.'
        if self.elapsed * 1000 > 1:
            return f'{self.elapsed*1000:0.2f} ms.'
        
        return f'{self.elapsed*1000000:0.2f} mcs.'
