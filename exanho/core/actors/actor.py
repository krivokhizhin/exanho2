import logging

from threading import Thread, Event
from queue import Queue

# The guard used to turn off
class ActorExit(Exception):
    pass

class Actor:
    def __init__(self, config, log_queue):
        self._config = config
        self._log_queue = log_queue
        self._mailbox = Queue()

    @property
    def config(self):
        return self._config

    def send(self, msg):
        '''
        Sends a message to the actor
        '''
        self._mailbox.put(msg)

    def recv(self):
        '''
        Gets an incoming message
        '''
        msg = self._mailbox.get()

        if msg is ActorExit:
            raise ActorExit()
        
        return msg

    def close(self):
        '''
        Closes the actor and disables it
        '''
        self.send(ActorExit)

    def start(self):
        '''
        Starts competitive execution
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap, name=self._config.name)
        t.daemon = self._config.daemon
        t.start()

    def _bootstrap(self):
        try:
            self.run()
            self.pool()
        except ActorExit:
            self.finalize()
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def pool(self):
        '''
        Runs a method that the user implements
        '''
        while True:
            msg = self.recv()
            self.handle(msg)

    def run(self, config):
        pass

    def finalize(self):
        pass

    def handle(msg):
        pass