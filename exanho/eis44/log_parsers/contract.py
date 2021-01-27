import datetime
import decimal
import logging

from sqlalchemy import func
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from ..model.aggregate import EisTableName, EisContractLog, EisParticipantLog, AggContractState, AggContract
from ..model.contract import ZfcsContract2015, ZfcsContractCancel2015, ZfcsContractProcedure2015, ZfcsContractProcedureCancel2015

log = logging.getLogger(__name__)

def get_contract_state(current_stage:str) -> AggContractState:
    if current_stage.upper() == 'E':
        return AggContractState.EXECUTION
    if current_stage.upper() == 'EC':
        return AggContractState.COMPLETED
    if current_stage.upper() == 'ET':
        return AggContractState.DISCONTINUED
    if current_stage.upper() == 'IN':
        return AggContractState.CANCELED

    return AggContractState.UNKNOWN

def fill_contract_by_zfcs_contract2015(session:OrmSession, cntr:AggContract, obj:ZfcsContract2015, addition_only:bool):

    if cntr is None:
        cntr = AggContract(
            publish_dt = obj.publish_dt,
            reg_num = obj.reg_num,
            subject = obj.subject,
            price = decimal.Decimal(obj.price) if obj.price else None,
            currency_code = obj.currency_code,
            right_to_conclude = obj.right_to_conclude,
            supplier_number = len(obj.suppliers),
            href = obj.href,
            state = get_contract_state(obj.current_stage),
            start_date = obj.execution_start_date,
            end_date = obj.execution_end_date
        )
        session.add(cntr)
    elif addition_only:
        if cntr.publish_dt is None: cntr.publish_dt = obj.publish_dt
        if cntr.subject is None: cntr.subject = obj.subject
        if cntr.price is None: cntr.price = decimal.Decimal(obj.price) if obj.price else None
        if cntr.currency_code is None: cntr.currency_code = obj.currency_code
        if cntr.right_to_conclude is None: cntr.right_to_conclude = obj.right_to_conclude
        if cntr.supplier_number is None: cntr.supplier_number = len(obj.suppliers)
        if cntr.href is None: cntr.href = obj.href
        if cntr.state is None: cntr.state = get_contract_state(obj.current_stage)
        if cntr.start_date is None: cntr.start_date = obj.execution_start_date
        if cntr.end_date is None: cntr.end_date = obj.execution_end_date
    else:
        cntr.publish_dt = obj.publish_dt
        cntr.subject = obj.subject
        cntr.price = decimal.Decimal(obj.price) if obj.price else None
        cntr.currency_code = obj.currency_code
        cntr.right_to_conclude = obj.right_to_conclude
        cntr.supplier_number = len(obj.suppliers)
        cntr.href = obj.href
        cntr.state = get_contract_state(obj.current_stage)
        cntr.start_date = obj.execution_start_date
        cntr.end_date = obj.execution_end_date
        cntr.updated_by = obj.id

def fill_contract_by_zfcs_contract_cancel2015(session:OrmSession, cntr:AggContract, obj:ZfcsContractCancel2015, addition_only:bool):

    if cntr is None:
        cntr = AggContract(
            reg_num = obj.reg_num,
            publish_dt = obj.publish_dt,
            state = get_contract_state(obj.current_stage)
        )
        session.add(cntr)
    elif addition_only:
        if cntr.state is None: cntr.state = get_contract_state(obj.current_stage)
    else:
        if cntr.publish_dt is None: cntr.publish_dt = obj.publish_dt
        cntr.state = get_contract_state(obj.current_stage)
        cntr.updated_by = obj.id

def fill_contract_by_zfcs_contract_procedure2015(session:OrmSession, cntr:AggContract, obj:ZfcsContractProcedure2015, addition_only:bool):

    if cntr is None:
        cntr = AggContract(
            reg_num = obj.reg_num,
            state = get_contract_state(obj.current_stage)
        )
        session.add(cntr)
    elif addition_only:
        if cntr.state is None: cntr.state = get_contract_state(obj.current_stage)
    else:
        cntr.state = get_contract_state(obj.current_stage)
        cntr.updated_by = obj.id

def fill_contract_by_zfcs_contract_procedure_cancel2015(session:OrmSession, cntr:AggContract, obj:ZfcsContractProcedureCancel2015, addition_only:bool):

    if cntr is None:
        cntr = AggContract(
            reg_num = obj.reg_num,
            state = get_contract_state(obj.current_stage)
        )
        session.add(cntr)
    elif addition_only:
        if cntr.state is None: cntr.state = get_contract_state(obj.current_stage)
    else:
        cntr.state = get_contract_state(obj.current_stage)
        cntr.updated_by = obj.id

def extract_unit(session:OrmSession):
    return session.query(EisContractLog.reg_num).\
        filter(EisContractLog.handled == False).\
            first()

def get_last_handled_publish_dt(session:OrmSession, reg_num:str) -> datetime.datetime:
    return session.query(func.max(EisContractLog.publish_dt)).\
        filter(EisContractLog.reg_num == reg_num).filter(EisContractLog.handled == True)\
            .scalar()

def unhandled_docs(session:OrmSession, reg_num:str):
    return session.query(EisContractLog.source, EisContractLog.doc_id, EisContractLog.publish_dt).\
        filter(EisContractLog.reg_num == reg_num).filter(EisContractLog.handled == False).\
            order_by(EisContractLog.publish_dt)

def handle(session:OrmSession, source:EisTableName, doc_id:int, addition_only:bool, reg_num:str):
    cntr = session.query(AggContract).filter(AggContract.reg_num == reg_num).one_or_none()
    if source == EisTableName.zfcs_contract2015:
        obj = session.query(ZfcsContract2015).get(doc_id)
        if obj is None:
            log.error(f'There is not document id={doc_id} in zfcs_contract2015. The log is marked as handled')
            return

        fill_contract_by_zfcs_contract2015(session, cntr, obj, addition_only)

        for supp_obj in obj.suppliers:
            inn = supp_obj.participant.inn
            kpp = supp_obj.participant.kpp
            participant_log = session.query(EisParticipantLog).\
                filter(EisParticipantLog.source == EisTableName.zfcs_contract2015).filter(EisParticipantLog.doc_id == doc_id).\
                    filter(EisParticipantLog.inn == inn).filter(EisParticipantLog.kpp == kpp).\
                        one_or_none()
            if participant_log is None:
                participant_log = EisParticipantLog(
                    inn = inn,
                    kpp = kpp,
                    publish_dt = obj.publish_dt,
                    source = EisTableName.zfcs_contract2015,
                    doc_id = doc_id,
                    handled = False
                )
                session.add(participant_log)
            else:
                participant_log.handled = False

            # part_dto = EisParticipant(
            #     name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name,
            #     inn = supp_obj.participant.inn,
            #     kpp = supp_obj.participant.kpp,
            # )

            # if supp_obj.participant.kind == CntrParticipantKind.FS:
            #     part_fs_obj = session.query(CntrParticipantForeign).filter(CntrParticipantForeign.id == supp_obj.participant.id).one()
            #     part_dto.name_lat = part_fs_obj.full_name_lat
            #     part_dto.tax_payer_code = part_fs_obj.tax_payer_code
            #     part_dto.country_full_name = part_fs_obj.country_full_name

    elif source == EisTableName.zfcs_contract_cancel2015:
        obj = session.query(ZfcsContractCancel2015).get(doc_id)
        if obj is None:
            log.error(f'There is not document id={doc_id} in zfcs_contract_cancel2015. The log is marked as handled')
            return

        fill_contract_by_zfcs_contract_cancel2015(session, cntr, obj, addition_only)
        
    elif source == EisTableName.zfcs_contract_procedure2015:
        obj = session.query(ZfcsContractProcedure2015).get(doc_id)
        if obj is None:
            log.error(f'There is not document id={doc_id} in zfcs_contract_procedure2015. The log is marked as handled')
            return

        fill_contract_by_zfcs_contract_procedure2015(session, cntr, obj, addition_only)

    elif source == EisTableName.zfcs_contract_procedure_cancel2015:
        obj = session.query(ZfcsContractProcedureCancel2015).get(doc_id)
        if obj is None:
            log.error(f'There is not document id={doc_id} in zfcs_contract_procedure_cancel2015. The log is marked as handled')
            return

        fill_contract_by_zfcs_contract_procedure_cancel2015(session, cntr, obj, addition_only)
        
    else:
        raise Error(f'not tested case ({source})')

def mark_as_handled(session:OrmSession, source:EisTableName, doc_id:int, reg_num:str):
    cntr_log = session.query(EisContractLog).\
        filter(EisContractLog.source == source).filter(EisContractLog.doc_id == doc_id).\
            one()

    cntr_log.handled = True
        
def finalize():
    pass