import logging
import time

from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy import func

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.orm.domain import Sessional

from ..interfaces import IEisParticipantService, ParticipantInfo, SummaryContractsByStateInfo, serialize
from ..model import AggContractState, AggParticipant, AggContract, AggContractParticipant

class EisParticipantService(IEisParticipantService, ServiceBase):

    logger = logging.getLogger(__name__)

    @serialize
    @try_logged
    @Sessional
    def get_participant(self, id:int):
        assert isinstance(id, int)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)

        participant = session.query(AggParticipant).get(id)
        if participant:
            return ParticipantInfo(
                id=id,
                name=participant.name,
                inn=participant.inn,
                kpp=participant.kpp
            )
        
        return None

    @serialize
    @try_logged
    @Sessional
    def get_participant_list(self, inn:str, kpp:str, page:int, size:int):
        assert isinstance(inn, str)
        if kpp:
            assert isinstance(kpp, str)
        
        if page < 1: page = 1
        if size < 1: size = 1

        participants = list()

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)

        participant_stmt = session.query(AggParticipant.id, AggParticipant.name, AggParticipant.inn, AggParticipant.kpp).filter(AggParticipant.inn == inn)
        if kpp:
            for participant in participant_stmt.filter(AggParticipant.kpp == kpp):
                participants.append(ParticipantInfo._make(participant))
            return (participants, len(participants))

        if not participants:
            for participant in participant_stmt.limit(size).offset((page-1)*size):
                participants.append(ParticipantInfo._make(participant))
            return (participants, participant_stmt.count())

        return (list(), 0)

    @serialize
    @try_logged
    @Sessional
    def get_current_activity(self, id: int) -> list:
        assert isinstance(id, int)

        exec_contracts = list()

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        for exec_contr in session.query(AggContract.state, func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state == AggContractState.EXECUTION).\
                group_by(AggContract.state, AggContract.currency_code).\
                    order_by(AggContract.state, AggContract.currency_code):
            exec_contracts.append(SummaryContractsByStateInfo._make((id, *exec_contr)))

        return exec_contracts

    @serialize
    @try_logged
    @Sessional
    def get_experience(self, id: int) ->list:
        assert isinstance(id, int)

        done_contracts = list()

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        for done_contr in session.query(AggContract.state, func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state != AggContractState.EXECUTION).\
                group_by(AggContract.state, AggContract.currency_code):
            done_contracts.append(SummaryContractsByStateInfo._make((id, *done_contr)))

        return done_contracts