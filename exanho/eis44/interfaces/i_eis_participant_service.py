from abc import ABC, abstractmethod

from . import ParticipantInfo

class IEisParticipantService(ABC):
    
    @abstractmethod
    def get_participant(self, id:int) -> ParticipantInfo:
        pass
    
    @abstractmethod
    def get_participant_list(self, inn:str, kpp:str, page:int, size:int):
        pass
    
    @abstractmethod
    def get_current_activity(self, id:int) -> list:
        pass
    
    @abstractmethod
    def get_experience(self, id:int) -> list:
        pass