from datetime import datetime, timezone

from ...ds.reference import nsiOkved
from ...model.nsi import NsiOkved

def parse(session, root_obj:nsiOkved, update=True, **kwargs):
    for item in root_obj.body.item:
        section = item.nsiOkvedData.section
        subsection = item.nsiOkvedData.subsection
        parent_code = item.nsiOkvedData.parentCode
        code = item.nsiOkvedData.code
        
        exist_okved = session.query(NsiOkved).filter(NsiOkved.subsection == subsection, NsiOkved.section == section, NsiOkved.parent_code == parent_code, NsiOkved.code == code).one_or_none()

        if exist_okved is None:
            new_okved = NsiOkved(
                guid = item.nsiOkvedData.guid,
                change_dt = item.nsiOkvedData.changeDateTime,
                start_date_active = item.nsiOkvedData.startDateActive,
                end_date_active = item.nsiOkvedData.endDateActive,
                business_status = item.nsiOkvedData.businessStatus,
                code = code,
                name = item.nsiOkvedData.name,
                parent_code = parent_code,
                section = section,
                subsection = subsection
            )
            session.add(new_okved)
            continue

        exist_chage_dt = exist_okved.change_dt if exist_okved.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkvedData.changeDateTime if item.nsiOkvedData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okved.guid = item.nsiOkvedData.guid
            exist_okved.change_dt = item.nsiOkvedData.changeDateTime
            exist_okved.start_date_active = item.nsiOkvedData.startDateActive
            exist_okved.end_date_active = item.nsiOkvedData.endDateActive
            exist_okved.business_status = item.nsiOkvedData.businessStatus
            exist_okved.name = item.nsiOkvedData.name

        