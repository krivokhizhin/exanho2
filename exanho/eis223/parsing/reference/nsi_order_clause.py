from datetime import datetime, timezone

from ...ds.reference import nsiOrderClauseType, nsiOrderClauseTypeDataType, templatesType, orderClauseTemplateType, orderClauseTemplateFieldType
from .nsi_template import get_template, fill_template, fill_field_template
from ...model.nsi_order_clause import *

NOT_VALIDATE_VALUE = '???'

def parse(session, root_obj:nsiOrderClauseType, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_order_clause(session, item.nsiOrderClauseTypeData, update)
        except:
            raise

def parse_order_clause(session, order_clause_obj:nsiOrderClauseTypeDataType, update=True):
    
    ogrn = order_clause_obj.creator.ogrn
    inn = order_clause_obj.creator.inn
    kpp = order_clause_obj.creator.kpp
    order_number = order_clause_obj.orderNumber

    exist_order_clause = session.query(NsiOrderClause).\
        filter(NsiOrderClause.creator_inn == inn, NsiOrderClause.creator_kpp == kpp, NsiOrderClause.order_number == order_number).\
            one_or_none()

    if exist_order_clause is None:
        exist_order_clause = session.query(NsiOrderClause).\
            filter(NsiOrderClause.creator_ogrn == ogrn, NsiOrderClause.creator_inn == inn, NsiOrderClause.creator_kpp == kpp, NsiOrderClause.order_number == order_number).\
                one_or_none()

    if exist_order_clause is None:
        new_order_clause = NsiOrderClause(
            guid = order_clause_obj.guid,
            change_dt = order_clause_obj.changeDateTime,
            business_status = order_clause_obj.businessStatus,
            name = order_clause_obj.name,
            order_number = order_number,

            creator_inn = inn,
            creator_kpp = kpp,
            creator_ogrn = ogrn
        )

        session.add(new_order_clause)
        fill_templates(session, new_order_clause, order_clause_obj.templates)
    else:
        exist_change_dt = exist_order_clause.change_dt if exist_order_clause.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_change_dt = order_clause_obj.changeDateTime if order_clause_obj.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_change_dt > exist_change_dt):
            exist_order_clause.guid = order_clause_obj.guid
            exist_order_clause.change_dt = order_clause_obj.changeDateTime
            exist_order_clause.business_status = order_clause_obj.businessStatus
            exist_order_clause.name = order_clause_obj.name
            exist_order_clause.order_number = order_number
            
            exist_order_clause.creator_inn = inn
            exist_order_clause.creator_kpp = kpp
            exist_order_clause.creator_ogrn = ogrn

            fill_templates(session, exist_order_clause, order_clause_obj.templates)

def fill_templates(session, owner:NsiOrderClause, templates_obj:templatesType):
    owner.templates = []
    if templates_obj is None:
        return

    for template_obj in templates_obj.template:
        template_as = get_template_association(session, template_obj)
        if template_as:
            owner.templates.append(template_as)

def get_template_association(session, template_obj:orderClauseTemplateType):
    if template_obj is None:
        return None

    template = get_template(session, NsiOrderClauseTemplate, 'order_clause', template_obj.id)

    if template is None:
        template = NsiOrderClauseTemplate()
        
    fill_template(session, template, template_obj)

    if template_obj.fields:
        for field_template_obj in template_obj.fields.field:
            field_template = get_order_clause_field(session, field_template_obj)
            if field_template:
                template.fields.append(field_template)

    template_as = NsiOrderClauseTemplateAs()
    template_as.template = template

    return template_as

def get_order_clause_field(session, field_template_obj:orderClauseTemplateFieldType):
    if field_template_obj is None:
        return None

    field_template = NsiOrderClauseFieldTemplate()
    fill_field_template(session, field_template, field_template_obj)

    return field_template