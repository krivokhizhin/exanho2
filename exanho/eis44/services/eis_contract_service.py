import logging
import time

from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.orm.domain import Sessional

from ..interfaces import IEisContractService, ContractInfo
from ..model import AggContract

class EisContractService(IEisContractService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @try_logged
    @Sessional
    def get_contract(self, reg_num:str) -> ContractInfo:
        assert isinstance(reg_num, str)

        session = Sessional.domain.Session
        assert isinstance(session, OrmSession)

        contract = session.query(AggContract).filter(AggContract.reg_num == reg_num).one_or_none()
        if contract:
            return ContractInfo(
                reg_num = contract.reg_num,
                state = contract.state.name,
                publish_dt = contract.publish_dt,
                subject = contract.subject,
                price = contract.price,
                currency_code = contract.currency_code,
                right_to_conclude = contract.right_to_conclude,
                supplier_number = contract.supplier_number,
                href = contract.href,
                start_date = contract.start_date,
                end_date = contract.end_date
            )

        return None