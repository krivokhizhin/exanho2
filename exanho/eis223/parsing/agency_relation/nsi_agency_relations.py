from datetime import datetime, timezone

from exanho.core.common import Error

from ...ds.agency_relation import nsiAgencyRelations, nsiAgencyRelationsDataType, relationsType, relationType
from ..types.customer_main_info_type import get_customer_main_info
from ...model.nsi_customer import *

def parse(session, root_obj:nsiAgencyRelations, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_agency_relations(session, item.nsiAgencyRelationsData, update)
        except:
            raise

def parse_agency_relations(session, agency_relations_obj:nsiAgencyRelationsDataType, update=True):

    customer = get_customer_main_info(session, agency_relations_obj.customer, False)
    if customer is None:
        raise Error('customer is None')

    customer.relations = []
    if agency_relations_obj.relations is None:
        return

    for relation_obj in agency_relations_obj.relations.relation:
        relation = get_relation(session, relation_obj)
        if relation:
            customer.relations.append(relation)

def get_relation(session, relation_obj:relationType):
    if relation_obj is None:
        return None

    relation = NsiAgencyRelation(
        relation_type = relation_obj.relationType,
        status = relation_obj.status,
        create_dt = relation_obj.createDateTime,
        update_dt = relation_obj.updateDateTime,
        comment = relation_obj.comment
    )

    relation.agency = get_customer_main_info(session, relation_obj.agency, False)

    session.add(relation)

    return relation