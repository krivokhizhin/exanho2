from abc import ABC, abstractmethod

from . import SummaryContracts

class IEisParticipantService(ABC):
    
    @abstractmethod
    def get_participants(self, inn:str, kpp:str=None) -> list:
        pass
    
    @abstractmethod
    def get_current_activity(self, id:int) -> list:
        pass
    
    @abstractmethod
    def get_experience(self, id:int) -> list:
        pass