from ...ds.reference import nsiOkdp
from ...model.nsi import NsiOkdp

def parse(session, root_obj:nsiOkdp, update=True, **kwargs):
    for item in root_obj.body.item:
        section = item.nsiOkdpData.section
        parent_code = item.nsiOkdpData.parentCode
        code = item.nsiOkdpData.code
        name = item.nsiOkdpData.name if item.nsiOkdpData.name else ''
        
        exist_okpd = session.query(NsiOkdp).filter(NsiOkdp.section == section, NsiOkdp.parent_code == parent_code, NsiOkdp.code == code).one_or_none()

        if exist_okpd is None:
            new_okpd = NsiOkdp(
                guid = item.nsiOkdpData.guid,
                change_dt = item.nsiOkdpData.changeDateTime,
                start_date_active = item.nsiOkdpData.startDateActive,
                end_date_active = item.nsiOkdpData.endDateActive,
                business_status = item.nsiOkdpData.businessStatus,
                code = code,
                name = name,
                parent_code = parent_code,
                section = section
            )
            session.add(new_okpd)

        if update or (exist_okpd and item.nsiOkdpData.changeDateTime > exist_okpd.change_dt):
            exist_okpd.guid = item.nsiOkdpData.guid
            exist_okpd.change_dt = item.nsiOkdpData.changeDateTime
            exist_okpd.start_date_active = item.nsiOkdpData.startDateActive
            exist_okpd.end_date_active = item.nsiOkdpData.endDateActive
            exist_okpd.business_status = item.nsiOkdpData.businessStatus
            exist_okpd.name = name

        