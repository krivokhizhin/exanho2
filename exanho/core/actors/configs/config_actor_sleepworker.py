from ...common.descriptors import List
from . import ActorConfig, ListConfigBaseDerived, SleepWorker

class SleepWorkerActorConfig(ActorConfig):
    workers = ListConfigBaseDerived(SleepWorker)