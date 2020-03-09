from . import *

def get_creator(unit_kind:str) -> UnitCreatorBase:
    if unit_kind == 'TCPServerUnit':
        return TCPServerUnitCreator()

    raise Exception('No unit found for the specified type ({}).'.format(unit_kind)) 