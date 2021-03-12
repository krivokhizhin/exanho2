import datetime
import logging

from collections import namedtuple
from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy import func

from exanho.core.manager_context import Context as ExanhoContext
from exanho.orm.domain import Sessional

from ..model.contract import ZfcsContract2015
from ..model.aggregate import EisTableName, EisContractLog, AggContract

from ..log_parsers import contract_ensuring

log = logging.getLogger(__name__)

Context = namedtuple('Context', ['min_doc_id', 'max_doc_id', 'docs'], defaults =[list()])

def initialize(appsettings, exanho_context:ExanhoContext):
    context = Context(**appsettings)
    
    log.info(f'Initialized')
    return context

def work(context:Context):
    min_doc_id: int = context.min_doc_id
    max_doc_id: int = context.max_doc_id
    docs:list = context.docs
    min_dt = datetime.datetime(2019, 11, 1)

    with Sessional.domain.session_scope() as session:
        assert isinstance(session, OrmSession)

        upd_cnt = None
        if docs:
            upd_cnt = len(docs)
        else:
            upd_cnt =  session.query(func.count(EisContractLog.id)).filter(EisContractLog.source == EisTableName.zfcs_contract2015).\
                filter(EisContractLog.doc_id >= min_doc_id, EisContractLog.doc_id <= max_doc_id).\
                    filter(EisContractLog.publish_dt > min_dt, EisContractLog.handled == True).scalar()

        print(f'All: {upd_cnt}')
        cur_upd_cnt = 0
        progress = 1

        stmt = session.query(EisContractLog).filter(EisContractLog.source == EisTableName.zfcs_contract2015)
        if docs:
            stmt = stmt.filter(EisContractLog.doc_id.in_(docs))
        else:
            stmt = stmt.filter(EisContractLog.doc_id >= min_doc_id, EisContractLog.doc_id <= max_doc_id)

        for eis_contract_log in stmt.\
            filter(EisContractLog.publish_dt > min_dt, EisContractLog.handled == True).\
                order_by(EisContractLog.publish_dt):

            cur_upd_cnt += 1
            if progress <= (cur_upd_cnt*100/upd_cnt):
                print(f'Done: {progress}%')
                progress += 1

            obj = session.query(ZfcsContract2015).get(eis_contract_log.doc_id)
            if obj is None:
                raise RuntimeError(f'No ZfcsContract2015 document id={eis_contract_log.doc_id} found')

            if obj.enforcements or obj.quality_guarantee or obj.guarantee_returns:

                cntr = session.query(AggContract).filter(AggContract.reg_num == eis_contract_log.reg_num).one()

                if obj.enforcements:
                    for enforcement in obj.enforcements:
                        contract_ensuring.handle_enforcement(session, cntr, enforcement, False)

                if obj.quality_guarantee:
                    contract_ensuring.handle_quality_guarantee(session, cntr, obj.quality_guarantee, False)

                if obj.guarantee_returns:
                    for guarantee_return in obj.guarantee_returns:
                        contract_ensuring.handle_guarantee_return(session, cntr, guarantee_return, False)

                session.commit()
       

    return context 

def finalize(context:Context):
    log.info(f'Finalized')