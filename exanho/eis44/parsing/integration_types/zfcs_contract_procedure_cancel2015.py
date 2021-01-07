from ...ds.export_types import zfcs_contractProcedureCancel2015Type
from ...model.contract import *

def parse(session, cntr_proc_cancel_obj:zfcs_contractProcedureCancel2015Type, update=True, **kwargs):
    cancelled_id = cntr_proc_cancel_obj.cancelledProcedureId
    cancel_dt = cntr_proc_cancel_obj.cancelDate
    court_doc_date = None if cntr_proc_cancel_obj.contractInvalidationCancel is None else cntr_proc_cancel_obj.contractInvalidationCancel.cancelReason.docDate
    current_stage = cntr_proc_cancel_obj.currentContractStage

    if session.query(ZfcsContractProcedureCancel2015).\
        filter(ZfcsContractProcedureCancel2015.cancelled_id == cancelled_id, ZfcsContractProcedureCancel2015.current_stage == current_stage, ZfcsContractProcedureCancel2015.cancel_dt == cancel_dt, ZfcsContractProcedureCancel2015.court_doc_date == court_doc_date).\
            count() > 0:
        return

    new_cancel = ZfcsContractProcedureCancel2015(
        cancelled_id = cancelled_id,
        reg_num = cntr_proc_cancel_obj.regNum,
        cancel_dt = cancel_dt,
        reason = cntr_proc_cancel_obj.reason,
        current_stage = current_stage,
        scheme_version = cntr_proc_cancel_obj.schemeVersion
    )
    session.add(new_cancel)

    if cntr_proc_cancel_obj.contractInvalidationCancel:
        new_cancel.court_name = cntr_proc_cancel_obj.contractInvalidationCancel.cancelReason.courtName
        new_cancel.court_doc_name = cntr_proc_cancel_obj.contractInvalidationCancel.cancelReason.docName
        new_cancel.court_doc_date = court_doc_date
        new_cancel.court_doc_number = cntr_proc_cancel_obj.contractInvalidationCancel.cancelReason.docNumber