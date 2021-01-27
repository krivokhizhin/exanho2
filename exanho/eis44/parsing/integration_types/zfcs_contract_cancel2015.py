from ...ds.contracts.fcsExport import zfcs_contractCancel2015Type
from ...model.contract import *

def parse(session, cntr_cancel_obj:zfcs_contractCancel2015Type, update=True, **kwargs):
    content_id = kwargs.get('content_id')
    reg_num = cntr_cancel_obj.regNum
    cancel_dt = cntr_cancel_obj.cancelDate
    doc_base = cntr_cancel_obj.documentBase

    cancel = session.query(ZfcsContractCancel2015).\
        filter(ZfcsContractCancel2015.reg_num == reg_num, ZfcsContractCancel2015.cancel_dt == cancel_dt, ZfcsContractCancel2015.doc_base == doc_base).\
            one_or_none()

    if cancel is None:
        cancel = ZfcsContractCancel2015(
            reg_num = reg_num,
            cancel_dt = cancel_dt,
            publish_dt = cntr_cancel_obj.publishDate,
            doc_base = doc_base,
            current_stage = cntr_cancel_obj.currentContractStage,
            scheme_version = cntr_cancel_obj.schemeVersion
        )
        session.add(cancel)

    elif not update:
        return
    else:
        cancel.publish_dt = cntr_cancel_obj.publishDate
        cancel.current_stage = cntr_cancel_obj.currentContractStage
        cancel.scheme_version = cntr_cancel_obj.schemeVersion

    cancel.content_id = content_id

    if cntr_cancel_obj.contractPrintFormInfo:
        cancel.contract_number = cntr_cancel_obj.contractPrintFormInfo.number
        cancel.sign_date = cntr_cancel_obj.contractPrintFormInfo.signDate
        # TODO: customer
        cancel.sign_name = cntr_cancel_obj.contractPrintFormInfo.signName