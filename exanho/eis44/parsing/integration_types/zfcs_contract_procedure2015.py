from ...ds.export_types import zfcs_contractProcedure2015Type
from ...model.contract import *

def parse(session, cntr_proc_obj:zfcs_contractProcedure2015Type, update=True, **kwargs):
    doc_id = cntr_proc_obj.id
    external_id = cntr_proc_obj.externalId

    procedure = session.query(ZfcsContractProcedure2015).filter(ZfcsContractProcedure2015.doc_id == doc_id, ZfcsContractProcedure2015.external_id == external_id).one_or_none()

    if procedure is None:
        procedure = ZfcsContractProcedure2015(
            doc_id = doc_id,
            external_id = external_id,
            reg_num = cntr_proc_obj.regNum,
            defense_number = cntr_proc_obj.defenseContractNumber,
            direct_dt = cntr_proc_obj.directDate,
            publish_dt = cntr_proc_obj.publishDate,
            version_number = cntr_proc_obj.versionNumber,

            modification_reason = cntr_proc_obj.modificationReason,
            current_stage = cntr_proc_obj.currentContractStage,
            okpd2okved2 = cntr_proc_obj.okpd2okved2,
            scheme_version = cntr_proc_obj.schemeVersion
        )
        session.add(procedure)
    elif not update:
        return
    else:
        procedure.reg_num = cntr_proc_obj.regNum
        procedure.defense_number = cntr_proc_obj.defenseContractNumber
        procedure.direct_dt = cntr_proc_obj.directDate
        procedure.publish_dt = cntr_proc_obj.publishDate
        procedure.version_number = cntr_proc_obj.versionNumber

        procedure.modification_reason = cntr_proc_obj.modificationReason
        procedure.current_stage = cntr_proc_obj.currentContractStage
        procedure.okpd2okved2 = cntr_proc_obj.okpd2okved2
        procedure.scheme_version = cntr_proc_obj.schemeVersion