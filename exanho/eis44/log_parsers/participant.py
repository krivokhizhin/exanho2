import datetime
import logging

from sqlalchemy import func
from sqlalchemy.orm.session import Session as OrmSession

from exanho.core.common import Error

from exanho.eis44.model import CntrParticipantKind, CntrParticipantForeign, ZfcsContract2015

from ..model.aggregate import EisTableName, EisParticipantLog, AggParticipant, AggContract, AggContractParticipant
from ..model.contract import ZfcsContract2015

log = logging.getLogger(__name__)

def fill_participant_by_zfcs_contract2015(session:OrmSession, participant:AggParticipant, obj:ZfcsContract2015, addition_only:bool, inn:str, kpp:str):
        
    contract = session.query(AggContract).filter(AggContract.reg_num == obj.reg_num).one()

    for supp_obj in obj.suppliers:
        if supp_obj.participant.inn != inn or supp_obj.participant.kpp != kpp:
            continue

        part_fs_obj = None
        if supp_obj.participant.kind == CntrParticipantKind.FS:
            part_fs_obj = session.query(CntrParticipantForeign).filter(CntrParticipantForeign.id == supp_obj.participant.id).one()

        if participant is None:

            participant = AggParticipant(
                name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name,
                inn = inn,
                kpp = kpp
            )
            session.add(participant)
            
            if part_fs_obj:
                participant.name_lat = part_fs_obj.full_name_lat
                participant.tax_payer_code = part_fs_obj.tax_payer_code
                participant.country_full_name = part_fs_obj.country_full_name

        elif addition_only:

            if participant.name is None: participant.name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name
            if part_fs_obj and participant.name_lat is None: participant.name_lat = part_fs_obj.full_name_lat
            if part_fs_obj and participant.tax_payer_code is None: participant.tax_payer_code = part_fs_obj.tax_payer_code
            if part_fs_obj and participant.country_full_name is None: participant.country_full_name = part_fs_obj.country_full_name

        else:

            participant.name = supp_obj.participant.short_name if supp_obj.participant.short_name else supp_obj.participant.full_name
            if part_fs_obj:
                participant.name_lat = part_fs_obj.full_name_lat
                participant.tax_payer_code = part_fs_obj.tax_payer_code
                participant.country_full_name = part_fs_obj.country_full_name

        cntr_prtc = session.query(AggContractParticipant).\
            filter(AggContractParticipant.contract == contract).filter(AggContractParticipant.participant == participant).\
                one_or_none()

        if cntr_prtc is None:
            cntr_prtc = AggContractParticipant()
            cntr_prtc.contract = contract
            cntr_prtc.participant = participant
            session.add(cntr_prtc)

def extract_unit(session:OrmSession):
    return session.query(EisParticipantLog.inn, EisParticipantLog.kpp).\
        filter(EisParticipantLog.handled == False).\
            first()

def get_last_handled_publish_dt(session:OrmSession, inn:str, kpp:str) -> datetime.datetime:
    return session.query(func.max(EisParticipantLog.publish_dt)).\
        filter(EisParticipantLog.inn == inn).filter(EisParticipantLog.kpp == kpp).filter(EisParticipantLog.handled == True)\
            .scalar()

def unhandled_docs(session:OrmSession, inn:str, kpp:str):
    return session.query(EisParticipantLog.source, EisParticipantLog.doc_id, EisParticipantLog.publish_dt).\
        filter(EisParticipantLog.inn == inn).filter(EisParticipantLog.kpp == kpp).filter(EisParticipantLog.handled == False).\
            order_by(EisParticipantLog.publish_dt)

def handle(session:OrmSession, source:EisTableName, doc_id:int, addition_only:bool, inn:str, kpp:str):
    prtc = session.query(AggParticipant).filter(AggParticipant.inn == inn).filter(AggParticipant.kpp == kpp).one_or_none()
    if source == EisTableName.zfcs_contract2015:
        obj = session.query(ZfcsContract2015).get(doc_id)
        if obj is None:
            log.error(f'There is not document id={doc_id} in zfcs_contract2015. The log is marked as handled')
            return

        fill_participant_by_zfcs_contract2015(session, prtc, obj, addition_only, inn, kpp)
        
    else:
        raise Error(f'not tested case ({source})')

def mark_as_handled(session:OrmSession, source:EisTableName, doc_id:int, inn:str, kpp:str):
    prtc_log = session.query(EisParticipantLog).\
        filter(EisParticipantLog.source == source).filter(EisParticipantLog.doc_id == doc_id).\
            filter(EisParticipantLog.inn == inn).filter(EisParticipantLog.kpp == kpp).\
                one()

    prtc_log.handled = True
        
def finalize():
    pass