from datetime import datetime, timezone

from ...ds.reference import nsiOkato
from ...model.nsi import NsiOkato

def parse(session, root_obj:nsiOkato, update=True, **kwargs):
    for item in root_obj.body.item:
        parent_code = item.nsiOkatoData.parentCode
        code = item.nsiOkatoData.code
        
        exist_okato = session.query(NsiOkato).filter(NsiOkato.parent_code == parent_code, NsiOkato.code == code).one_or_none()

        if exist_okato is None:
            new_okato = NsiOkato(
                guid = item.nsiOkatoData.guid,
                change_dt = item.nsiOkatoData.changeDateTime,
                start_date_active = item.nsiOkatoData.startDateActive,
                end_date_active = item.nsiOkatoData.endDateActive,
                business_status = item.nsiOkatoData.businessStatus,
                code = code,
                name = item.nsiOkatoData.name,
                parent_code = parent_code
            )
            session.add(new_okato)
            continue

        exist_chage_dt = exist_okato.change_dt if exist_okato.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkatoData.changeDateTime if item.nsiOkatoData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okato.guid = item.nsiOkatoData.guid
            exist_okato.change_dt = item.nsiOkatoData.changeDateTime
            exist_okato.start_date_active = item.nsiOkatoData.startDateActive
            exist_okato.end_date_active = item.nsiOkatoData.endDateActive
            exist_okato.business_status = item.nsiOkatoData.businessStatus
            exist_okato.name = item.nsiOkatoData.name

        