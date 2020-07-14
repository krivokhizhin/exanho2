import logging

from multiprocessing import Process, Queue, Event

from exanho.core.common.log_utilities import configurer_logging

# The guard used to turn off
class ActorExit(Exception):
    pass

class Actor:
    def __init__(self, config, context):
        self._config = config
        self._context = context
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
        t = Process(target=self._bootstrap, name=self._config.name, args=(self._config, self._context, ))
        t.daemon = self._config.daemon
        t.start()

    def _bootstrap(self, config, context):
        try:
            configurer_logging(context.log_queue)
            self.run(config, context)
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

    def handle(self, msg):
        pass