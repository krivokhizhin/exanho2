from . import ActorConfig, ListConfigBaseDerived, SleepWorker

class SleepWorkerActorConfig(ActorConfig):
    workers = ListConfigBaseDerived(SleepWorker)