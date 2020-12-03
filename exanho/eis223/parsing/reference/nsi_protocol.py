from datetime import datetime, timezone

from ...ds.reference import nsiProtocolType, nsiProtocolTypeDataType, templatesType27, protocolTemplateType, protocolTemplateFieldType
from .nsi_template import get_template, fill_template, fill_field_template
from ...model.nsi_protocol import *

NOT_VALIDATE_VALUE = '???'

def parse(session, root_obj:nsiProtocolType, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_protocol(session, item.nsiProtocolTypeData, update)
        except:
            raise

def parse_protocol(session, protocol_obj:nsiProtocolTypeDataType, update=True):
    
    code = protocol_obj.code
    exist_protocol = session.query(NsiProtocol).filter(NsiProtocol.code == code).one_or_none()

    if exist_protocol is None:
        new_protocol = NsiProtocol(
            guid = protocol_obj.guid,
            create_dt = protocol_obj.createDateTime,
            change_dt = protocol_obj.changeDateTime,
            start_date_active = protocol_obj.startDateActive,
            end_date_active = protocol_obj.endDateActive,
            business_status = protocol_obj.businessStatus,
            code = code,
            name = protocol_obj.name,
            order_number = protocol_obj.orderNumber,

            extended = protocol_obj.extended,
            
            protocol_kind = protocol_obj.protocolKind,
            lot_oriented = protocol_obj.lotOriented
        )

        session.add(new_protocol)
        fill_purchase_methods(session, new_protocol, protocol_obj.purchaseMethod)
        fill_templates(session, new_protocol, protocol_obj.templates)
    else:
        exist_change_dt = exist_protocol.change_dt if exist_protocol.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_change_dt = protocol_obj.changeDateTime if protocol_obj.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_change_dt > exist_change_dt):
            exist_protocol.guid = protocol_obj.guid
            exist_protocol.create_dt = protocol_obj.createDateTime
            exist_protocol.change_dt = protocol_obj.changeDateTime
            exist_protocol.start_date_active = protocol_obj.startDateActive
            exist_protocol.end_date_active = protocol_obj.endDateActive
            exist_protocol.business_status = protocol_obj.businessStatus
            exist_protocol.name = protocol_obj.name
            exist_protocol.order_number = protocol_obj.orderNumber
            
            exist_protocol.extended = protocol_obj.extended
            
            exist_protocol.protocol_kind = protocol_obj.protocolKind
            exist_protocol.lot_oriented = protocol_obj.lotOriented

            fill_purchase_methods(session, exist_protocol, protocol_obj.purchaseMethod)
            fill_templates(session, exist_protocol, protocol_obj.templates)

def fill_purchase_methods(session, protocol:NsiProtocol, methods_obj:list):
    protocol.purchase_methods = []
    
    if methods_obj:        

        for method_code in methods_obj:
            if method_code:
                protocol.purchase_methods.append(
                    NsiProtocolPurchMethod(purch_method_code = method_code)
                )

def fill_templates(session, owner:NsiProtocol, templates_obj:templatesType27):
    owner.templates = []
    if templates_obj is None:
        return

    for template_obj in templates_obj.template:
        template_as = get_template_association(session, template_obj)
        if template_as:
            owner.templates.append(template_as)

def get_template_association(session, template_obj:protocolTemplateType):
    if template_obj is None:
        return None

    template = get_template(session, NsiProtocolTemplate, 'protocol', template_obj.id)

    if template is None:
        template = NsiProtocolTemplate()
        fill_template(session, template, template_obj)

        template.hide_comm_decision = template_obj.blocks.hideCommDecision
        template.hide_comm_decision_access = template_obj.blocks.hideCommDecisionAccess
        template.hide_comm_decision_result = template_obj.blocks.hideCommDecisionResult
        template.hide_procedure = template_obj.blocks.hideProcedure
        template.hide_cancellation = template_obj.blocks.hideCancellation

        if template_obj.fields:
            for field_template_obj in template_obj.fields.field:
                field_template = get_protocol_field(session, field_template_obj)
                if field_template:
                    template.fields.append(field_template)

    template_as = NsiProtocolTemplateAs()
    template_as.template = template

    return template_as

def get_protocol_field(session, field_template_obj:protocolTemplateFieldType):
    if field_template_obj is None:
        return None

    field_template = NsiProtocolFieldTemplate()
    fill_field_template(session, field_template, field_template_obj)

    field_template.tab_level = field_template_obj.tabLevel
    field_template.is_base_field = field_template_obj.isBaseField

    return field_template