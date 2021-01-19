import logging

from exanho.core.common import Singleton
from exanho.orm.domain import Domain, Sessional

from ..model.parsing import EisTableName, ParseWorkerState

log = logging.getLogger(__name__)

class ContractPlaceholder(metaclass=Singleton):

    def __init__(self, source_domain:Domain) -> None:
        self._source_domain = source_domain

    @property
    def source_domain(self) -> Domain:
        return self._source_domain

def get_worker_state(session, table_name:EisTableName) -> ParseWorkerState:
    worker_state = session.query(ParseWorkerState).filter(ParseWorkerState.table == table_name).one_or_none()
    if worker_state is None:
        worker_state = ParseWorkerState(table = table_name)
        session.add(worker_state)
    return worker_state


def initialize(source_domain):
    placeholder = ContractPlaceholder(source_domain)

def perform():
    placeholder = ContractPlaceholder()
    with placeholder.source_domain.session_scope() as session:
        cntr_state = get_worker_state(session, EisTableName.zfcs_contract2015)
        cntr_pr_state = get_worker_state(session, EisTableName.zfcs_contract_procedure2015)
        cntr_pr_cnl_state = get_worker_state(session, EisTableName.zfcs_contract_procedure_cancel2015)
        log.debug(f'{EisTableName.zfcs_contract2015.name}: ({cntr_state.last_dt},{cntr_state.last_id}) | {EisTableName.zfcs_contract_procedure2015.name}: ({cntr_pr_state.last_dt},{cntr_pr_state.last_id}) | {EisTableName.zfcs_contract_procedure_cancel2015.name}: ({cntr_pr_cnl_state.last_dt},{cntr_pr_cnl_state.last_id})')

def finalize():
    pass