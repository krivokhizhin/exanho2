from datetime import datetime, timezone

from ...ds.reference import nsiOkei
from ...model.nsi import NsiOkeiSection, NsiOkeiGroup, NsiOkei

def parse(session, root_obj:nsiOkei, update=True, **kwargs):
    for item in root_obj.body.item:

        code = item.nsiOkeiData.code
        exist_okei = session.query(NsiOkei).filter(NsiOkei.code == code).one_or_none()

        section = get_section(session, item.nsiOkeiData.section)
        group = get_group(session, item.nsiOkeiData.group)
        
        if exist_okei is None:

            new_okei = NsiOkei(
                guid = item.nsiOkeiData.guid,
                change_dt = item.nsiOkeiData.changeDateTime,
                start_date_active = item.nsiOkeiData.startDateActive,
                end_date_active = item.nsiOkeiData.endDateActive,
                business_status = item.nsiOkeiData.businessStatus,
                code = code,
                name = item.nsiOkeiData.name
            )

            new_okei.section = section
            new_okei.group = group

            session.add(new_okei)
            continue

        exist_chage_dt = exist_okei.change_dt if exist_okei.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_chage_dt = item.nsiOkeiData.changeDateTime if item.nsiOkeiData.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_chage_dt > exist_chage_dt):
            exist_okei.guid = item.nsiOkeiData.guid
            exist_okei.change_dt = item.nsiOkeiData.changeDateTime
            exist_okei.start_date_active = item.nsiOkeiData.startDateActive
            exist_okei.end_date_active = item.nsiOkeiData.endDateActive
            exist_okei.business_status = item.nsiOkeiData.businessStatus
            exist_okei.name = item.nsiOkeiData.name
            exist_okei.section = section
            exist_okei.group = group

def get_section(session, section_obj):
    section = session.query(NsiOkeiSection).filter(NsiOkeiSection.code == section_obj.code).one_or_none()

    if section is None:
        section = NsiOkeiSection(
            code = section_obj.code,
            name = section_obj.name
        )

    return section

def get_group(session, group_obj):
    group = session.query(NsiOkeiGroup).filter(NsiOkeiGroup.code == group_obj.code).one_or_none()

    if group is None:
        group = NsiOkeiGroup(
            code = group_obj.code,
            name = group_obj.name
        )

    return group