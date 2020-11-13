from datetime import datetime, timezone

from ...ds.reference import nsiOkv
from ...model.nsi import NsiOkv

def parse(session, root_obj:nsiOkv, update=True, **kwargs):
    for item in root_obj.body.item:
        code = item.nsiOkvData.code
        digit_code = item.nsiOkvData.digitalCode

        exist_okv = session.query(NsiOkv).filter(NsiOkv.code == code, NsiOkv.digital_code == digit_code).one_or_none()

        if exist_okv is None:
            new_okv = NsiOkv(
                guid = item.nsiOkvData.guid,
                change_dt = item.nsiOkvData.changeDateTime,
                start_date_active = item.nsiOkvData.startDateActive,
                end_date_active = item.nsiOkvData.endDateActive,
                business_status = item.nsiOkvData.businessStatus,
                code = code,
                digital_code = digit_code,
                name = item.nsiOkvData.name,
                short_name = item.nsiOkvData.shortName
            )
            session.add(new_okv)
            continue

        exist_chage_dt = exist_okv.change_dt if exist_okv.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkvData.changeDateTime if item.nsiOkvData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okv.guid = item.nsiOkvData.guid
            exist_okv.change_dt = item.nsiOkvData.changeDateTime
            exist_okv.start_date_active = item.nsiOkvData.startDateActive
            exist_okv.end_date_active = item.nsiOkvData.endDateActive
            exist_okv.business_status = item.nsiOkvData.businessStatus
            exist_okv.name = item.nsiOkvData.name
            exist_okv.short_name = item.nsiOkvData.shortName

        