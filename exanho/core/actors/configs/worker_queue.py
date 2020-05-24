from ...common.descriptors import String
from . import WorkerConfig

class QueueWorker(WorkerConfig):
    queue_name = String()