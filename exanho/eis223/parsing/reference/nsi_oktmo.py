from datetime import datetime, timezone

from ...ds.reference import nsiOktmo
from ...model.nsi import NsiOktmo

def parse(session, root_obj:nsiOktmo, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOktmoData.code
        parent_code = item.nsiOktmoData.parentCode
        exist_oktmo = session.query(NsiOktmo).filter(NsiOktmo.parent_code == parent_code, NsiOktmo.code == code).one_or_none()
        
        if exist_oktmo is None:

            new_oktmo = NsiOktmo(
                guid = item.nsiOktmoData.guid,
                change_dt = item.nsiOktmoData.changeDateTime,
                start_date_active = item.nsiOktmoData.startDateActive,
                end_date_active = item.nsiOktmoData.endDateActive,
                business_status = item.nsiOktmoData.businessStatus,
                code = code,
                name = item.nsiOktmoData.name,
                parent_code = parent_code,
                okato = item.nsiOktmoData.okato
            )

            session.add(new_oktmo)
            continue

        exist_chage_dt = exist_oktmo.change_dt if exist_oktmo.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOktmoData.changeDateTime if item.nsiOktmoData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_oktmo.guid = item.nsiOktmoData.guid
            exist_oktmo.change_dt = item.nsiOktmoData.changeDateTime
            exist_oktmo.start_date_active = item.nsiOktmoData.startDateActive
            exist_oktmo.end_date_active = item.nsiOktmoData.endDateActive
            exist_oktmo.business_status = item.nsiOktmoData.businessStatus
            exist_oktmo.name = item.nsiOktmoData.name
            exist_oktmo.okato = item.nsiOktmoData.okato