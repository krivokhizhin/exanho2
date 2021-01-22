import datetime
import decimal
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.eis44.model import ZfcsContractProcedureCancel2015

from ..model.aggregate import EisTableName, EisContractLog

log = logging.getLogger(__name__)

ContractRecord = namedtuple('ContractRecord', 'id reg_num cancel_dt')

def get_current_dto(session:OrmSession, doc_id:int):
        
    cntr_tuple = session.query(ZfcsContractProcedureCancel2015.id, ZfcsContractProcedureCancel2015.reg_num, ZfcsContractProcedureCancel2015.cancel_dt).\
        filter(ZfcsContractProcedureCancel2015.id > doc_id).filter(ZfcsContractProcedureCancel2015.cancel_dt != None).\
            order_by(ZfcsContractProcedureCancel2015.id).first()

    if cntr_tuple is None:
        return None

    return ContractRecord._make(cntr_tuple)

def add_to_log(session:OrmSession, dto:ContractRecord) -> int:
    session.add(
        EisContractLog(
            reg_num = dto.reg_num,
            publish_dt = dto.cancel_dt,

            source = get_work_table_name(),
            doc_id = dto.id
        )
    )    

    return dto.id

def get_work_table_name():
    return EisTableName.zfcs_contract_procedure_cancel2015
        
def finalize():
    pass