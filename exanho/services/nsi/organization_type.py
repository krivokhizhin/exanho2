import logging

import exanho.orm.sqlalchemy as domain

from exanho.core.common import try_logged
from exanho.core.actors import ServiceBase
from exanho.interfaces import INsiOrgTypeService
from exanho.model.nsi import NsiOrganizationType

class NsiOrgTypeService(INsiOrgTypeService, ServiceBase):

    logger = logging.getLogger(__name__)

    @try_logged
    @domain.sessional
    def put(self, code, name, desc=None):
        org_type = NsiOrganizationType(code, name, desc)
        self.session.add(org_type)

    @try_logged
    @domain.sessional
    def get(self, id):
        org_type = self.session.query(NsiOrganizationType).filter_by(id=id).one_or_none()
        if org_type:
            return org_type.serialize()
        return None

    @try_logged
    @domain.sessional
    def get_by_code(self, code):
        org_type = self.session.query(NsiOrganizationType).filter_by(code=code).one_or_none()
        if org_type:
            return org_type.serialize()
        return None