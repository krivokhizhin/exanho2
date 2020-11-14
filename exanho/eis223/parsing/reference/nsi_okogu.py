from datetime import datetime, timezone

from ...ds.reference import nsiOkogu
from ...model.nsi import NsiOkogu

def parse(session, root_obj:nsiOkogu, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOkoguData.code
        parent_code = item.nsiOkoguData.parentCode
        exist_okogu = session.query(NsiOkogu).filter(NsiOkogu.parent_code == parent_code, NsiOkogu.code == code).one_or_none()
        
        if exist_okogu is None:

            new_okogu = NsiOkogu(
                guid = item.nsiOkoguData.guid,
                change_dt = item.nsiOkoguData.changeDateTime,
                start_date_active = item.nsiOkoguData.startDateActive,
                end_date_active = item.nsiOkoguData.endDateActive,
                business_status = item.nsiOkoguData.businessStatus,
                code = code,
                name = item.nsiOkoguData.name,
                parent_code = parent_code
            )

            session.add(new_okogu)
            continue

        exist_chage_dt = exist_okogu.change_dt if exist_okogu.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkoguData.changeDateTime if item.nsiOkoguData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okogu.guid = item.nsiOkoguData.guid
            exist_okogu.change_dt = item.nsiOkoguData.changeDateTime
            exist_okogu.start_date_active = item.nsiOkoguData.startDateActive
            exist_okogu.end_date_active = item.nsiOkoguData.endDateActive
            exist_okogu.business_status = item.nsiOkoguData.businessStatus
            exist_okogu.name = item.nsiOkoguData.name