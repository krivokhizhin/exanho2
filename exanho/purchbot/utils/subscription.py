import datetime
from sqlalchemy.orm.session import Session as OrmSession
from sqlalchemy.sql.schema import Table

from exanho.core.common import Error

from ..model import EventSubscription

def find_and_deactivate(session:OrmSession, current_dt: datetime.date = datetime.date.today()):
    assert isinstance(current_dt, datetime.date)

    tbl:Table = EventSubscription.__table__
    session.execute(
        tbl.update().where(tbl.c.active == True).where(tbl.c.last_date < current_dt).values(active = False)
    )