from ...ds.reference import nsiOkved2
from ...model.nsi import NsiOkved2

def parse(session, root_obj:nsiOkved2, update=True, **kwargs):
    for item in root_obj.body.item:
        section = item.nsiOkved2Data.section
        parent_code = item.nsiOkved2Data.parentCode
        code = item.nsiOkved2Data.code
        
        exist_okved2 = session.query(NsiOkved2).filter(NsiOkved2.section == section, NsiOkved2.parent_code == parent_code, NsiOkved2.code == code).one_or_none()

        if exist_okved2 is None:
            new_okved2 = NsiOkved2(
                guid = item.nsiOkved2Data.guid,
                change_dt = item.nsiOkved2Data.changeDateTime,
                start_date_active = item.nsiOkved2Data.startDateActive,
                end_date_active = item.nsiOkved2Data.endDateActive,
                business_status = item.nsiOkved2Data.businessStatus,
                code = code,
                name = item.nsiOkved2Data.name,
                parent_code = parent_code,
                section = section
            )
            session.add(new_okved2)

        if update or (exist_okved2 and item.nsiOkved2Data.changeDateTime > exist_okved2.change_dt):
            exist_okved2.guid = item.nsiOkved2Data.guid
            exist_okved2.change_dt = item.nsiOkved2Data.changeDateTime
            exist_okved2.start_date_active = item.nsiOkved2Data.startDateActive
            exist_okved2.end_date_active = item.nsiOkved2Data.endDateActive
            exist_okved2.business_status = item.nsiOkved2Data.businessStatus
            exist_okved2.name = item.nsiOkved2Data.name

        