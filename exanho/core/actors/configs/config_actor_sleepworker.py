from ...common.descriptors import List
from . import ActorConfig, ListConfigBaseDerived, SleepWorker

class SleepWorkerActorConfig(ActorConfig):
    joinable_queues = List()
    workers = ListConfigBaseDerived(SleepWorker)