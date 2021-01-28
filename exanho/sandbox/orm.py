from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy import func

from collections import namedtuple

from exanho.eis44.model import AggParticipant, AggContract, AggContractParticipant, AggContractState
from exanho.eis44.interfaces import SummaryContracts, ContractShortInfo, ContractInfo

def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis44_test')

    inn = '0105069779'
    kpp = '010501001'
    result = list()
    state = '__doc__'

    reg_num = '1010506668015000035'

    with d.session_scope() as session:
        assert isinstance(session, OrmSession)

        # contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
        #     join(AggParticipant).\
        #         filter(AggParticipant.inn == inn, AggParticipant.kpp == kpp).\
        #             subquery()

        # for tuple in session.query(AggContract.state.name, func.count(AggContract.id), func.sum(AggContract.price), AggContract.currency_code, func.min(AggContract.start_date), func.max(AggContract.end_date)).\
        #     filter(AggContract.id.in_(contract_ids_stmt)).\
        #         group_by(AggContract.state, AggContract.currency_code):
        #     print(*tuple)
        #     result.append(SummaryContracts._make(tuple))

        # contract_ids_stmt = session.query(AggContractParticipant.contract_id).\
        #     join(AggParticipant).\
        #         filter(AggParticipant.inn == inn, AggParticipant.kpp == kpp).\
        #             subquery()

        # result_stmt = session.query(AggContract.reg_num, AggContract.state.name, AggContract.price, AggContract.currency_code, AggContract.start_date, AggContract.href).\
        #     filter(AggContract.id.in_(contract_ids_stmt))

        # if state and isinstance(state, str) and not str(state).startswith('_') and not str(state).endswith('_') and state in dir(AggContractState):
        #     result_stmt = result_stmt.filter(AggContract.state == AggContractState[state])

        # for tuple in result_stmt:
        #     print(*tuple)
        #     result.append(ContractShortInfo._make(tuple))

        contract = session.query(AggContract).filter(AggContract.reg_num == reg_num).one_or_none()
        if contract:
            print(ContractInfo(
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
            ))

    print(result)