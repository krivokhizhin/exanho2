from xmlrpc.client import ServerProxy

from exanho.eis44.interfaces import ParticipantInfo, ParticipantCurrentActivityInfo, ParticipantExperienceInfo, deserialize  

@deserialize
def get_participant(eis_service:ServerProxy, participant_id:int) -> ParticipantInfo:
    assert isinstance(participant_id, int)
    return eis_service.get_participant(participant_id)

@deserialize
def get_participant_list(eis_service:ServerProxy, inn:str, kpp:str, page:int, size:int):
    assert isinstance(inn, str)
    if kpp:
        assert isinstance(kpp, str)
    if page is None:
        page = 1
    assert isinstance(page, int)
    if size is None:
        size = 10
    assert isinstance(size, int)
    return eis_service.get_participant_list(inn, kpp, page, size)    

@deserialize
def get_current_participant_activity(eis_service:ServerProxy, participant_id:int) -> ParticipantCurrentActivityInfo:
    assert isinstance(participant_id, int)
    return eis_service.get_current_activity(participant_id)   

@deserialize
def get_current_participant_activity_report(eis_service:ServerProxy, participant_id:int) -> list:
    assert isinstance(participant_id, int)
    return eis_service.get_current_activity_report(participant_id)  

@deserialize
def get_participant_experience(eis_service:ServerProxy, participant_id:int) -> ParticipantExperienceInfo:
    assert isinstance(participant_id, int)
    return eis_service.get_experience(participant_id)   

@deserialize
def get_participant_experience_report(eis_service:ServerProxy, participant_id:int) -> list:
    assert isinstance(participant_id, int)
    return eis_service.get_experience_report(participant_id)