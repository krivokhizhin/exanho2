from . import UnitCreatorBase
from ..unit_tcpserver import TCPServerUnit

class TCPServerUnitCreator(UnitCreatorBase):

    def get_unit_class(self):
        return TCPServerUnit