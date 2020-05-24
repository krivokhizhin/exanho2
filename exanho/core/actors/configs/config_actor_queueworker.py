from . import ActorConfig, ListConfigBaseDerived, QueueWorker

class QueueWorkerActorConfig(ActorConfig):
    workers = ListConfigBaseDerived(QueueWorker)