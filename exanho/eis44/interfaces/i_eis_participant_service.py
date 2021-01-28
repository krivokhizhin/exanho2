from abc import ABC, abstractmethod

from . import SummaryContracts

class IEisParticipantService(ABC):
    
    @abstractmethod
    def get_summary_contracts(self, inn:str, kpp:str=None) -> list:
        pass
    
    @abstractmethod
    def get_contracts(self, inn:str, kpp:str=None, **kwargs) -> list:
        pass