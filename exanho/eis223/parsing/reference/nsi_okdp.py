from ...ds.reference import nsiOkdp
from ...model.nsi import NsiOkdp

def parse(session, root_obj:nsiOkdp, update=True, **kwargs):
    for item in root_obj.body.item:
        section = item.nsiOkdpData.section
        parent_code = item.nsiOkdpData.parentCode
        code = item.nsiOkdpData.code
        name = item.nsiOkdpData.name if item.nsiOkdpData.name else ''
        
        exist_okdp = session.query(NsiOkdp).filter(NsiOkdp.section == section, NsiOkdp.parent_code == parent_code, NsiOkdp.code == code).one_or_none()

        if exist_okdp is None:
            new_okdp = NsiOkdp(
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
            session.add(new_okdp)

        if update or (exist_okdp and item.nsiOkdpData.changeDateTime > exist_okdp.change_dt):
            exist_okdp.guid = item.nsiOkdpData.guid
            exist_okdp.change_dt = item.nsiOkdpData.changeDateTime
            exist_okdp.start_date_active = item.nsiOkdpData.startDateActive
            exist_okdp.end_date_active = item.nsiOkdpData.endDateActive
            exist_okdp.business_status = item.nsiOkdpData.businessStatus
            exist_okdp.name = name

        