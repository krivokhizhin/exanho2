from datetime import datetime, timezone

from ...ds.reference import nsiOkpd2
from ...model.nsi import NsiOkpd2

def parse(session, root_obj:nsiOkpd2, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOkpd2Data.code
        parent_code = item.nsiOkpd2Data.parentCode
        exist_okpd2 = session.query(NsiOkpd2).filter(NsiOkpd2.parent_code == parent_code, NsiOkpd2.code == code).one_or_none()
        
        if exist_okpd2 is None:

            new_okpd2 = NsiOkpd2(
                guid = item.nsiOkpd2Data.guid,
                change_dt = item.nsiOkpd2Data.changeDateTime,
                business_status = item.nsiOkpd2Data.businessStatus,
                code = code,
                name = item.nsiOkpd2Data.name,
                parent_code = parent_code
            )

            session.add(new_okpd2)
            continue

        exist_chage_dt = exist_okpd2.change_dt if exist_okpd2.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkpd2Data.changeDateTime if item.nsiOkpd2Data.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okpd2.guid = item.nsiOkpd2Data.guid
            exist_okpd2.change_dt = item.nsiOkpd2Data.changeDateTime
            exist_okpd2.business_status = item.nsiOkpd2Data.businessStatus
            exist_okpd2.name = item.nsiOkpd2Data.name