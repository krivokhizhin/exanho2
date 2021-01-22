import datetime
import decimal
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from exanho.eis44.model import CntrParticipantKind, CntrParticipantForeign, ZfcsContract2015, ZfcsContractProcedure2015, ZfcsContractProcedureCancel2015

from ..model.aggregate import EisTableName, EisContractLog
# from ..model.eis import EisContractState, EisContractKind, EisContract, EisParticipant, EisContractParticipant

log = logging.getLogger(__name__)

ContractRecord = namedtuple('ContractRecord', 'id reg_num publish_dt')

# def get_contract_state(current_stage:str) -> EisContractState:
#     if current_stage.upper() == 'E':
#         return EisContractState.EXECUTION
#     if current_stage.upper() == 'EC':
#         return EisContractState.COMPLETED
#     if current_stage.upper() == 'ET':
#         return EisContractState.DISCONTINUED
#     if current_stage.upper() == 'IN':
#         return EisContractState.CANCELED

#     return EisContractState.UNKNOWN

# def get_dto(session:OrmSession, type_dto:EisTableName, id:int) -> EisContract:
#     if type_dto == EisTableName.zfcs_contract2015:
#         obj = session.query(ZfcsContract2015).get(id)
#         dto = EisContract(
#             kind = EisContractKind.FZ44,
#             publish_dt = obj.publish_dt,
#             reg_num = obj.reg_num,
#             subject = obj.subject,
#             price = decimal.Decimal(obj.price),
#             currency_code = obj.currency_code,
#             right_to_conclude = obj.right_to_conclude,
#             supplier_number = 0,
#             href = obj.href,
#             state = get_contract_state(obj.current_stage),
#             start_date = obj.execution_start_date,
#             end_date = obj.execution_end_date
#         )

#         dto.unstable_suppliers = list()

#         for supp_obj in obj.suppliers:
#             dto.supplier_number += 1

#             part_dto = EisParticipant(
#                 name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name,
#                 inn = supp_obj.participant.inn,
#                 kpp = supp_obj.participant.kpp,
#             )

#             if supp_obj.participant.kind == CntrParticipantKind.FS:
#                 part_fs_obj = session.query(CntrParticipantForeign).filter(CntrParticipantForeign.id == supp_obj.participant.id).one()
#                 part_dto.name_lat = part_fs_obj.full_name_lat
#                 part_dto.tax_payer_code = part_fs_obj.tax_payer_code
#                 part_dto.country_full_name = part_fs_obj.country_full_name

#             dto.unstable_suppliers.append(part_dto)

#         return dto

#     if type_dto == EisTableName.zfcs_contract_procedure2015:
#         obj = session.query(ZfcsContractProcedure2015).get(id)
#         dto = EisContract(
#             kind = EisContractKind.FZ44,
#             reg_num = obj.reg_num,
#             state = get_contract_state(obj.current_stage)
#         )

#         return dto

#     if type_dto == EisTableName.zfcs_contract_procedure_cancel2015:
#         obj = session.query(ZfcsContractProcedureCancel2015).get(id)
#         dto = EisContract(
#             kind = EisContractKind.FZ44,
#             reg_num = obj.reg_num,
#             state = get_contract_state(obj.current_stage)
#         )

#         return dto

#     raise Error('not tested case')

# def create_or_update_participant(session:OrmSession, unstable_supplier:EisParticipant):
#     participant = session.query(EisParticipant).filter(EisParticipant.inn == unstable_supplier.inn, EisParticipant.kpp == unstable_supplier.kpp).one_or_none()
    
#     if participant is None:
#         participant = unstable_supplier
#     else:
#         if unstable_supplier.name: participant.name = unstable_supplier.name
#         if unstable_supplier.name_lat: participant.name_lat = unstable_supplier.name_lat
#         if unstable_supplier.tax_payer_code: participant.tax_payer_code = unstable_supplier.tax_payer_code
#         if unstable_supplier.country_full_name: participant.country_full_name = unstable_supplier.country_full_name

#     return participant

def get_current_dto(session:OrmSession, doc_id:int):
        
    cntr_tuple = session.query(ZfcsContract2015.id, ZfcsContract2015.reg_num, ZfcsContract2015.publish_dt).\
        filter(ZfcsContract2015.id > doc_id).filter(ZfcsContract2015.publish_dt != None).\
            order_by(ZfcsContract2015.id).first()

    if cntr_tuple is None:
        return None

    return ContractRecord._make(cntr_tuple)

def add_to_log(session:OrmSession, dto:ContractRecord) -> int:
    session.add(
        EisContractLog(
            reg_num = dto.reg_num,
            publish_dt = dto.publish_dt,

            source = get_work_table_name(),
            doc_id = dto.id
        )
    )    

    return dto.id

def get_work_table_name():
    return EisTableName.zfcs_contract2015
        
def finalize():
    pass