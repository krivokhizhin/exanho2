import datetime
import decimal
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Singleton, Error
from exanho.orm.domain import Domain, Sessional

from exanho.eis44.model import CntrParticipantKind, CntrParticipantForeign, ZfcsContract2015, ZfcsContractProcedure2015, ZfcsContractProcedureCancel2015

from ..model.parsing import EisTableName, ParseWorkerState
from ..model.eis import EisContractState, EisContractKind, EisContract, EisParticipant, EisContractParticipant

log = logging.getLogger(__name__)

EisRecord = namedtuple('EisRecord', 'doc_type doc_id actual_dt')

class ContractPlaceholder(metaclass=Singleton):

    def __init__(self, source_domain:Domain, cntr_id:int, cntr_pr_id:int, cntr_pr_cnl_id:int) -> None:
        self._source_domain = source_domain
        self._cntr_id = cntr_id
        self._cntr_pr_id = cntr_pr_id
        self._cntr_pr_cnl_id = cntr_pr_cnl_id

    @property
    def source_domain(self) -> Domain:
        return self._source_domain

    @property
    def cntr_id(self) -> int:
        return self._cntr_id

    @property
    def cntr_pr_id(self) -> int:
        return self._cntr_pr_id

    @property
    def cntr_pr_cnl_id(self) -> int:
        return self._cntr_pr_cnl_id

def get_worker_state_by_table_name(session:OrmSession, table_name:EisTableName) -> ParseWorkerState:
    worker_state = session.query(ParseWorkerState).filter(ParseWorkerState.table == table_name).one_or_none()
    if worker_state is None:
        worker_state = ParseWorkerState(table = table_name)
        session.add(worker_state)
        session.flush()
    return worker_state

def get_table_last_id(state_id:int) -> int:
    with Sessional.domain.session_scope() as session:
        return session.query(ParseWorkerState.last_id).filter(ParseWorkerState.id == state_id).scalar()

def set_table_last_id(session:OrmSession, state_id:int, last_id:int):
    state = session.query(ParseWorkerState).get(state_id)
    state.last_id = last_id
    # session.execute(\
    #     ParseWorkerState.__table__.update().\
    #         where(ParseWorkerState.__table__.c.id == state_id).\
    #             values(last_id = last_id)\
    #                 )

def get_contract_state(current_stage:str) -> EisContractState:
    if current_stage.upper() == 'E':
        return EisContractState.EXECUTION
    if current_stage.upper() == 'EC':
        return EisContractState.COMPLETED
    if current_stage.upper() == 'ET':
        return EisContractState.DISCONTINUED
    if current_stage.upper() == 'IN':
        return EisContractState.CANCELED

    return EisContractState.UNKNOWN

def get_dto(session:OrmSession, type_dto:EisTableName, id:int) -> EisContract:
    if type_dto == EisTableName.zfcs_contract2015:
        obj = session.query(ZfcsContract2015).get(id)
        dto = EisContract(
            kind = EisContractKind.FZ44,
            publish_dt = obj.publish_dt,
            reg_num = obj.reg_num,
            subject = obj.subject,
            price = decimal.Decimal(obj.price),
            currency_code = obj.currency_code,
            right_to_conclude = obj.right_to_conclude,
            supplier_number = 0,
            href = obj.href,
            state = get_contract_state(obj.current_stage),
            start_date = obj.execution_start_date,
            end_date = obj.execution_end_date
        )

        dto.unstable_suppliers = list()

        for supp_obj in obj.suppliers:
            dto.supplier_number += 1

            part_dto = EisParticipant(
                name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name,
                inn = supp_obj.participant.inn,
                kpp = supp_obj.participant.kpp,
            )

            if supp_obj.participant.kind == CntrParticipantKind.FS:
                part_fs_obj = session.query(CntrParticipantForeign).filter(CntrParticipantForeign.id == supp_obj.participant.id).one()
                part_dto.name_lat = part_fs_obj.full_name_lat
                part_dto.tax_payer_code = part_fs_obj.tax_payer_code
                part_dto.country_full_name = part_fs_obj.country_full_name

            dto.unstable_suppliers.append(part_dto)

        return dto

    if type_dto == EisTableName.zfcs_contract_procedure2015:
        obj = session.query(ZfcsContractProcedure2015).get(id)
        dto = EisContract(
            kind = EisContractKind.FZ44,
            reg_num = obj.reg_num,
            state = get_contract_state(obj.current_stage)
        )

        return dto

    if type_dto == EisTableName.zfcs_contract_procedure_cancel2015:
        obj = session.query(ZfcsContractProcedureCancel2015).get(id)
        dto = EisContract(
            kind = EisContractKind.FZ44,
            reg_num = obj.reg_num,
            state = get_contract_state(obj.current_stage)
        )

        return dto

    raise Error('not tested case')

def get_current_dto(placeholder:ContractPlaceholder):
    with placeholder.source_domain.session_scope() as session:
        
        cntr_last_id = get_table_last_id(placeholder.cntr_id)
        cntr_tuple = session.query(ZfcsContract2015.id, ZfcsContract2015.publish_dt).\
            filter(ZfcsContract2015.id > cntr_last_id).filter(ZfcsContract2015.publish_dt != None).\
                order_by(ZfcsContract2015.id).first()
        
        cntr_pr_last_id = get_table_last_id(placeholder.cntr_pr_id)
        cntr_pr_tuple = session.query(ZfcsContractProcedure2015.id, ZfcsContractProcedure2015.publish_dt).\
            filter(ZfcsContractProcedure2015.id > cntr_pr_last_id).filter(ZfcsContractProcedure2015.publish_dt != None).\
                order_by(ZfcsContractProcedure2015.id).first()
        
        cntr_pr_cnl_last_id = get_table_last_id(placeholder.cntr_pr_cnl_id)
        cntr_pr_cnl_tuple = session.query(ZfcsContractProcedureCancel2015.id, ZfcsContractProcedureCancel2015.cancel_dt).\
            filter(ZfcsContractProcedureCancel2015.id > cntr_pr_cnl_last_id).\
                order_by(ZfcsContractProcedureCancel2015.id).first()

        if not any((cntr_tuple, cntr_pr_tuple, cntr_pr_cnl_tuple)):
            return None, None, None

        if cntr_tuple is None:
            cntr_tuple = (None, None, datetime.datetime(datetime.MAXYEAR, 12, 31, tzinfo=datetime.timezone.utc))
        else:
            cntr_tuple = EisRecord(doc_type=EisTableName.zfcs_contract2015, doc_id=cntr_tuple[0], actual_dt=cntr_tuple[1])

        if cntr_pr_tuple is None:
            cntr_pr_tuple = (None, None, datetime.datetime(datetime.MAXYEAR, 12, 31, tzinfo=datetime.timezone.utc))
        else:
            cntr_pr_tuple = EisRecord(doc_type=EisTableName.zfcs_contract_procedure2015, doc_id=cntr_pr_tuple[0], actual_dt=cntr_pr_tuple[1])

        if cntr_pr_cnl_tuple is None:
            cntr_pr_cnl_tuple = (None, None, datetime.datetime(datetime.MAXYEAR, 12, 31, tzinfo=datetime.timezone.utc))
        else:
            cntr_pr_cnl_tuple = EisRecord(doc_type=EisTableName.zfcs_contract_procedure_cancel2015, doc_id=cntr_pr_cnl_tuple[0], actual_dt=cntr_pr_cnl_tuple[1])

        for type_dto, doc_id, _ in sorted((cntr_tuple, cntr_pr_tuple, cntr_pr_cnl_tuple), key=lambda tp: tp.actual_dt):
            dto = get_dto(session, type_dto, doc_id)
            return type_dto, doc_id, dto

        raise Error('not tested case')

def create_or_update_participant(session:OrmSession, unstable_supplier:EisParticipant):
    participant = session.query(EisParticipant).filter(EisParticipant.inn == unstable_supplier.inn, EisParticipant.kpp == unstable_supplier.kpp).one_or_none()
    
    if participant is None:
        participant = unstable_supplier
    else:
        if unstable_supplier.name: participant.name = unstable_supplier.name
        if unstable_supplier.name_lat: participant.name_lat = unstable_supplier.name_lat
        if unstable_supplier.tax_payer_code: participant.tax_payer_code = unstable_supplier.tax_payer_code
        if unstable_supplier.country_full_name: participant.country_full_name = unstable_supplier.country_full_name

    return participant

def create_or_update_contract(session:OrmSession, dto:EisContract, dto_type:EisTableName) -> EisContract:
    contract = session.query(EisContract).filter(EisContract.reg_num == dto.reg_num).one_or_none()

    if contract is None:
        contract = dto
        session.add(contract)
    elif dto_type == EisTableName.zfcs_contract2015:
        contract.kind = dto.kind
        contract.publish_dt = dto.publish_dt
        contract.subject = dto.subject
        contract.price = dto.price
        contract.currency_code = dto.currency_code
        contract.right_to_conclude = dto.right_to_conclude
        contract.supplier_number = dto.supplier_number
        contract.href = dto.href
        contract.state = dto.state
        contract.start_date = dto.start_date
        contract.end_date = dto.end_date
    else:
        contract.kind = dto.kind
        contract.state = dto.state

    if hasattr(dto, 'unstable_suppliers'):
        contract.suppliers = list()
        for unstable_supplier in dto.unstable_suppliers:
            supplier = EisContractParticipant()
            supplier.participant = create_or_update_participant(session, unstable_supplier)
            contract.suppliers.append(supplier)

        if hasattr(contract, 'unstable_suppliers'):
            delattr(contract, 'unstable_suppliers')

    return contract


def initialize(source_domain:Domain):

    with Sessional.domain.session_scope() as session:
        cntr_state = get_worker_state_by_table_name(session, EisTableName.zfcs_contract2015)
        cntr_pr_state = get_worker_state_by_table_name(session, EisTableName.zfcs_contract_procedure2015)
        cntr_pr_cnl_state = get_worker_state_by_table_name(session, EisTableName.zfcs_contract_procedure_cancel2015)

        ContractPlaceholder(source_domain, cntr_state.id, cntr_pr_state.id, cntr_pr_cnl_state.id)

def perform():
    placeholder = ContractPlaceholder()

    dto_type, doc_id, dto = get_current_dto(placeholder)
    while isinstance(dto_type, EisTableName):
        with Sessional.domain.session_scope() as session:
            create_or_update_contract(session, dto, dto_type)
            if dto_type == EisTableName.zfcs_contract2015:
                set_table_last_id(session, placeholder.cntr_id, doc_id)
            elif dto_type == EisTableName.zfcs_contract_procedure2015:
                set_table_last_id(session, placeholder.cntr_pr_id, doc_id)
            else: # EisTableName.zfcs_contract_procedure_cancel2015
                set_table_last_id(session, placeholder.cntr_pr_cnl_id, doc_id)

        log.debug(f'{dto_type}: {doc_id} perform')
        dto_type, doc_id, dto = get_current_dto(placeholder)
        
def finalize():
    pass