from datetime import datetime, timezone

from ...ds.reference import nsiOkfs
from ...model.nsi import NsiOkfs

def parse(session, root_obj:nsiOkfs, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOkfsData.code
        parent_code = item.nsiOkfsData.parentCode
        exist_okfs = session.query(NsiOkfs).filter(NsiOkfs.parent_code == parent_code, NsiOkfs.code == code).one_or_none()
        
        if exist_okfs is None:

            new_okfs = NsiOkfs(
                guid = item.nsiOkfsData.guid,
                change_dt = item.nsiOkfsData.changeDateTime,
                start_date_active = item.nsiOkfsData.startDateActive,
                end_date_active = item.nsiOkfsData.endDateActive,
                business_status = item.nsiOkfsData.businessStatus,
                code = code,
                name = item.nsiOkfsData.name,
                parent_code = parent_code
            )

            session.add(new_okfs)
            continue

        exist_chage_dt = exist_okfs.change_dt if exist_okfs.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkfsData.changeDateTime if item.nsiOkfsData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okfs.guid = item.nsiOkfsData.guid
            exist_okfs.change_dt = item.nsiOkfsData.changeDateTime
            exist_okfs.start_date_active = item.nsiOkfsData.startDateActive
            exist_okfs.end_date_active = item.nsiOkfsData.endDateActive
            exist_okfs.business_status = item.nsiOkfsData.businessStatus
            exist_okfs.name = item.nsiOkfsData.name