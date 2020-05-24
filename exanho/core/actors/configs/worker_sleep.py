from ...common.descriptors import Float
from . import WorkerConfig

class SleepWorker(WorkerConfig):
    sleep = Float()