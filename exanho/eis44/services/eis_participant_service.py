import logging
import time

from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy import func

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.orm.domain import Sessional

from ..interfaces import IEisParticipantService, SummaryContracts, ContractShortInfo, serialize
from ..model import AggContractState, AggParticipant, AggContract, AggContractParticipant

class EisParticipantService(IEisParticipantService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @serialize
    @try_logged
    @Sessional
    def get_summary_contracts(self, inn:str, kpp:str=None) -> list:
        assert isinstance(inn, str)
        if kpp:
            assert isinstance(kpp, str)

        summary_contracts = list()

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)
          
        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            join(AggParticipant).\
                filter(AggParticipant.inn == inn, AggParticipant.kpp == kpp).\
                    subquery()

        for contract in session.query(AggContract.state.name, func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
            filter(AggContract.id.in_(contract_ids_stmt)).\
                group_by(AggContract.state, AggContract.currency_code):
            summary_contracts.append(SummaryContracts._make(contract))

        return summary_contracts
    
    @serialize
    @try_logged
    @Sessional
    def get_contracts(self, inn:str, kpp:str=None, state:str=None) -> list:
        assert isinstance(inn, str)
        if kpp:
            assert isinstance(kpp, str)

        if state:
            assert isinstance(state, str)
            if not str(state).startswith('_') and not str(state).endswith('_') and state in dir(AggContractState):
                state = AggContractState[state]

        contracts = list()

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)

        contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
            join(AggParticipant).filter(AggParticipant.inn == inn)

        if kpp:
            contract_ids_stmt = contract_ids_stmt.filter(AggParticipant.kpp == kpp)

        contracts_stmt = session.query(AggContract.reg_num, AggContract.state.name, AggContract.price, AggContract.currency_code, AggContract.start_date, AggContract.href).\
            filter(AggContract.id.in_(contract_ids_stmt))

        if state:
            contracts_stmt = contracts_stmt.filter(AggContract.state == state)

        for contract in contracts_stmt:
            contracts.append(ContractShortInfo._make(contract))

        return contracts