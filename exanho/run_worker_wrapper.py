from .units.creators import UnitCreatorBase

def run_worker_wrapper(creator: UnitCreatorBase, *args, **kwargs):
    unit = creator.instance(*args, **kwargs)
    unit.initialize()
    unit.run()