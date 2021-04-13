from abc import ABC, abstractmethod

from . import ParticipantInfo, ParticipantCurrentActivityInfo, ParticipantExperienceInfo

class IEisParticipantService(ABC):
    
    @abstractmethod
    def get_participant(self, id:int) -> ParticipantInfo:
        pass
    
    @abstractmethod
    def get_participant_list(self, inn:str, kpp:str, page:int, size:int):
        pass
    
    @abstractmethod
    def get_current_activity(self, id:int) -> ParticipantCurrentActivityInfo:
        pass
    
    @abstractmethod
    def get_current_activity_report(self, id:int) -> list:
        pass
    
    @abstractmethod
    def get_experience(self, id:int) -> ParticipantExperienceInfo:
        pass
    
    @abstractmethod
    def get_experience_report(self, id:int) -> list:
        pass
    
    @abstractmethod
    def get_last_participant_events(self, id:int, last_event_id:int=None) -> list:
        pass