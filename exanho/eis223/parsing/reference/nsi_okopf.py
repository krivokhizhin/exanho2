from datetime import datetime, timezone

from ...ds.reference import nsiOkopf
from ...model.nsi import NsiOkopf

def parse(session, root_obj:nsiOkopf, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOkopfData.code
        parent_code = item.nsiOkopfData.parentCode
        exist_okopf = session.query(NsiOkopf).filter(NsiOkopf.parent_code == parent_code, NsiOkopf.code == code).one_or_none()
        
        if exist_okopf is None:

            new_okopf = NsiOkopf(
                guid = item.nsiOkopfData.guid,
                change_dt = item.nsiOkopfData.changeDateTime,
                start_date_active = item.nsiOkopfData.startDateActive,
                end_date_active = item.nsiOkopfData.endDateActive,
                business_status = item.nsiOkopfData.businessStatus,
                code = code,
                name = item.nsiOkopfData.name,
                parent_code = parent_code
            )

            session.add(new_okopf)
            continue

        exist_chage_dt = exist_okopf.change_dt if exist_okopf.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkopfData.changeDateTime if item.nsiOkopfData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okopf.guid = item.nsiOkopfData.guid
            exist_okopf.change_dt = item.nsiOkopfData.changeDateTime
            exist_okopf.start_date_active = item.nsiOkopfData.startDateActive
            exist_okopf.end_date_active = item.nsiOkopfData.endDateActive
            exist_okopf.business_status = item.nsiOkopfData.businessStatus
            exist_okopf.name = item.nsiOkopfData.name