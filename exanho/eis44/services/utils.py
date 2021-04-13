
from sqlalchemy.orm.session import Session as OrmSession

from exanho.eis44.model.aggregate import EisTableName
from exanho.eis44.model.contract import ZfcsContract2015

def get_href_by_doc(session:OrmSession, table_name:EisTableName, doc_id:int) -> str :

    if table_name == EisTableName.zfcs_contract2015:
        return session.query(ZfcsContract2015.href).filter(ZfcsContract2015.id == doc_id).scalar()
    else:
        return None

def get_docstrings_by_doc(table_name:EisTableName, doc_id:int) -> str :

    if table_name == EisTableName.zfcs_contract2015:
        return ZfcsContract2015.__doc__
    else:
        return None