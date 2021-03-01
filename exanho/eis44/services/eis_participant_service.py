from exanho.eis44.model.aggregate import participant
import logging
import time

from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy import func

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.orm.domain import Sessional

from ..interfaces import IEisParticipantService, ParticipantInfo, ParticipantCurrentActivityInfo, ContractInfo, ParticipantExperienceInfo, serialize
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
    def get_current_activity(self, id: int) -> ParticipantCurrentActivityInfo:
        assert isinstance(id, int)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        cntr_count = 0
        cntr_rur_sum = 0
        cntr_currencies = list()
        cntr_cur_count = list()
        cntr_cur_sum = list()
        cntr_first_start_date = None
        cntr_last_end_date = None

        for exec_contr in session.query(func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state == AggContractState.EXECUTION).\
                group_by(AggContract.currency_code):
            
            cntr_count_by_currency, cntr_sum, cntr_currency, cntr_first, cntr_last = exec_contr
            if cntr_currency == 'RUB':
                cntr_count += cntr_count_by_currency
                cntr_rur_sum += cntr_sum
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)
            elif cntr_currency is None or cntr_currency == '':
                cntr_count += cntr_count_by_currency
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)
            else:
                cntr_count += cntr_count_by_currency
                cntr_currencies.append(cntr_currency)
                cntr_cur_count.append(cntr_count)
                cntr_cur_sum.append(cntr_sum)
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)

        cntr_right_to_conclude_count = session.query(func.count(AggContract.id)).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state == AggContractState.EXECUTION).\
                filter(AggContract.right_to_conclude == True).scalar()
        
        exec_activities = ParticipantCurrentActivityInfo(
            participant_id=id,
            cntr_count=cntr_count,
            cntr_rur_sum=cntr_rur_sum,
            cntr_currencies=cntr_currencies,
            cntr_cur_count=cntr_cur_count,
            cntr_cur_sum=cntr_cur_sum,
            cntr_right_to_conclude_count=cntr_right_to_conclude_count,
            cntr_first_start_date=cntr_first_start_date,
            cntr_last_end_date=cntr_last_end_date
        )

        return exec_activities

    @serialize
    @try_logged
    @Sessional
    def get_current_activity_report(self, id: int) -> list:
        assert isinstance(id, int)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        result = list()

        for exec_contr in session.query(AggContract).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state == AggContractState.EXECUTION).\
                order_by(AggContract.publish_dt):
            
            result.append(
                ContractInfo(
                    reg_num=exec_contr.reg_num,
                    state=AggContractState.EXECUTION.name,
                    publish_dt=exec_contr.publish_dt,
                    subject=exec_contr.subject,
                    price=exec_contr.price,
                    currency_code=exec_contr.currency_code,
                    right_to_conclude=exec_contr.right_to_conclude,
                    start_date=exec_contr.start_date,
                    end_date=exec_contr.end_date,
                    supplier_number=exec_contr.supplier_number,
                    href=exec_contr.href
                )
            )

        return result

    @serialize
    @try_logged
    @Sessional
    def get_experience(self, id: int) -> ParticipantExperienceInfo:
        assert isinstance(id, int)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)

        cntr_ec_count = 0
        cntr_ec_rur_sum = 0
        cntr_ec_cur_count = 0
        cntr_et_count = 0
        cntr_et_rur_sum = 0
        cntr_et_cur_count = 0
        cntr_in_count = 0
        cntr_in_rur_sum = 0
        cntr_in_cur_count = 0
        cntr_first_start_date = None
        cntr_last_end_date = None
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        for done_contr in session.query(AggContract.state, func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state != AggContractState.EXECUTION).\
                group_by(AggContract.state, AggContract.currency_code):

            cntr_state, cntr_count, cntr_sum, cntr_currency, cntr_first, cntr_last = done_contr
            if cntr_state == AggContractState.COMPLETED:
                cntr_ec_count += cntr_count
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)
                if cntr_currency == 'RUB':
                    cntr_ec_rur_sum += cntr_sum
                else:
                    cntr_ec_cur_count += cntr_count
            elif cntr_state == AggContractState.DISCONTINUED:
                cntr_et_count += cntr_count
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)
                if cntr_currency == 'RUB':
                    cntr_et_rur_sum += cntr_sum
                else:
                    cntr_et_cur_count += cntr_count
            elif cntr_state == AggContractState.CANCELED:
                cntr_in_count += cntr_count
                cntr_first_start_date = cntr_first if cntr_first_start_date is None else min(cntr_first_start_date, cntr_first)
                cntr_last_end_date = cntr_last if cntr_last_end_date is None else max(cntr_last_end_date, cntr_last)
                if cntr_currency == 'RUB':
                    cntr_in_rur_sum += cntr_sum
                else:
                    cntr_in_cur_count += cntr_count
            else:
                pass

        experience = ParticipantExperienceInfo(
            participant_id = id,
            cntr_ec_count = cntr_ec_count,
            cntr_ec_rur_sum = cntr_ec_rur_sum,
            cntr_ec_cur_count = cntr_ec_cur_count,
            cntr_et_count = cntr_et_count,
            cntr_et_rur_sum = cntr_et_rur_sum,
            cntr_et_cur_count = cntr_et_cur_count,
            cntr_in_count = cntr_in_count,
            cntr_in_rur_sum = cntr_in_rur_sum,
            cntr_in_cur_count = cntr_in_cur_count,
            cntr_first_start_date = cntr_first_start_date,
            cntr_last_end_date = cntr_last_end_date
        )

        return experience

    @serialize
    @try_logged
    @Sessional
    def get_experience_report(self, id: int) ->list:
        assert isinstance(id, int)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            filter(AggContractParticipant.participant_id == id).\
                subquery()

        result = list()

        for exec_contr in session.query(AggContract).\
            filter(AggContract.id.in_(contract_ids_stmt)).filter(AggContract.state != AggContractState.EXECUTION).\
                order_by(AggContract.publish_dt):
            
            result.append(
                ContractInfo(
                    reg_num=exec_contr.reg_num,
                    state=exec_contr.state.name,
                    publish_dt=exec_contr.publish_dt,
                    subject=exec_contr.subject,
                    price=exec_contr.price,
                    currency_code=exec_contr.currency_code,
                    right_to_conclude=exec_contr.right_to_conclude,
                    start_date=exec_contr.start_date,
                    end_date=exec_contr.end_date,
                    supplier_number=exec_contr.supplier_number,
                    href=exec_contr.href
                )
            )

        return result