import logging
import xml.etree.ElementTree as ET

from multiprocessing import shared_memory

import exanho.orm.sqlalchemy as domain

from exanho.core.common import try_logged
from exanho.core.actors import ServiceBase
from exanho.interfaces import IParse, INsiOrgTypeService
from exanho.model.nsi import NsiOrganizationType

namespaces = {
    '': 'http://zakupki.gov.ru/oos/export/1',
    'oos': 'http://zakupki.gov.ru/oos/types/1',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

class NsiOrgTypeService(IParse, INsiOrgTypeService, ServiceBase):

    logger = logging.getLogger(__name__)

    @try_logged
    @domain.sessional
    def put(self, code, name, desc=None):
        org_type = NsiOrganizationType(code, name, desc)
        self.session.add(org_type)

    @try_logged
    @domain.sessional
    def get(self, id):
        log = logging.getLogger(__name__)
        log.debug(f'get({id})')
        org_type = self.session.query(NsiOrganizationType).filter_by(id=id).one_or_none()
        log.debug(org_type)
        if org_type:
            return org_type.serialize()
        return None

    @try_logged
    @domain.sessional
    def get_by_code(self, code):
        log = logging.getLogger(__name__)
        log.debug(f'get_by_code({code})')
        org_type = self.session.query(NsiOrganizationType).filter_by(code=code).one_or_none()
        log.debug(org_type)
        if org_type:
            return org_type.serialize()
        return None

    @try_logged
    @domain.sessional
    def parse(self, filename, size, message, update=False):
        log = logging.getLogger(__name__)

        new_counter = 0
        update_counter = 0

        try:
            shm = shared_memory.SharedMemory(message)
            buffer = shm.buf[:size]

            doc = ET.fromstring(buffer.tobytes().decode(encoding="utf-8", errors="strict"))
            type_list = doc.find('nsiOrganizationTypesList', namespaces=namespaces)

            if type_list is None:
                raise RuntimeError('Element "nsiOrganizationTypesList" was not found')

            for org_type_elem in type_list:
                code = org_type_elem.find('oos:code', namespaces=namespaces).text
                name = org_type_elem.find('oos:name', namespaces=namespaces).text
                desc_elem = org_type_elem.find('oos:description', namespaces=namespaces)

                exists_org_type = self.session.query(NsiOrganizationType).filter_by(code=code).one_or_none()
                if exists_org_type and update:
                    exists_org_type.name = name
                    exists_org_type.description = desc_elem.text if desc_elem else None
                    update_counter += 1
                elif exists_org_type is None:
                    self.session.add(NsiOrganizationType(code, name, desc_elem.text if desc_elem else None))
                    new_counter += 1
        finally:
            buffer.release()
            shm.close()

        return new_counter, update_counter