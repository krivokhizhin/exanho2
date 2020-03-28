import logging

from multiprocessing import Process, Queue, Event

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
        t = Process(target=self._bootstrap, name=self._config.name, args=(self._config, self._log_queue))
        t.daemon = True
        t.start()

    def _bootstrap(self, config, log_queue):
        try:
            self._configurer_logging(log_queue)
            self.run(config)
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

    def _configurer_logging(self, queue):
        h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
        root = logging.getLogger('root')
        root.addHandler(h)
        root.setLevel(logging.DEBUG)

    def run(self, config):
        pass

    def finalize(self):
        pass

    def handle(msg):
        pass