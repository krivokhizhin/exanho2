from datetime import datetime, timezone
from exanho.orm.domain import validate

from ...ds.reference import nsiPurchaseMethod, nsiPurchaseMethodDataType, protocolListType, purchasePhaseListType, templatesType29, noticeTemplateType, noticeTemplateFieldType, templateTableType, purchaseProtocol, purchasePhase, phaseTransitionsListType, phaseTransition, templateTableColumnType
from ...model.nsi_template import *
from ...model.nsi_purchase_method import *

NOT_VALIDATE_VALUE = '???'

def parse(session, root_obj:nsiPurchaseMethod, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_purchase_method(session, item.nsiPurchaseMethodData, update)
        except:
            raise

def parse_purchase_method(session, method_obj:nsiPurchaseMethodDataType, update=True):
    
    code = method_obj.code
    exist_method = session.query(NsiPurchaseMethod).filter(NsiPurchaseMethod.code == code).one_or_none()

    if exist_method is None:
        new_method = NsiPurchaseMethod(
            guid = method_obj.guid,
            create_dt = method_obj.changeDateTime,
            change_dt = method_obj.createDateTime,
            start_date_active = method_obj.startDateActive,
            end_date_active = method_obj.endDateActive,
            business_status = method_obj.businessStatus,
            code = code,
            name = method_obj.name,
            parent_code = method_obj.parentCode,
            order_number = method_obj.orderNumber,
            is_electronic = False if method_obj.isElectronic is None else method_obj.isElectronic,

            creator_inn = None if method_obj.creator is None else method_obj.creator.inn,
            creator_kpp = None if method_obj.creator is None else method_obj.creator.kpp,
            creator_ogrn = None if method_obj.creator is None else method_obj.creator.ogrn,

            extended = method_obj.extended,
            competitive = method_obj.competitive,

            protocol_controlled_order = None if method_obj.protocols is None else method_obj.protocols.controlledOrder,

            has_phases = method_obj.hasPhases,
            typal = method_obj.typal,
            typal_kind = method_obj.typalKind,
            lot_oriented = method_obj.lotOriented
        )

        session.add(new_method)
        fill_templates(session, new_method, method_obj.templates)
        fill_protocols(session, new_method, method_obj.protocols, get_protocol_association)
        fill_phases(session, new_method, method_obj.phases)
    else:
        exist_change_dt = exist_method.change_dt if exist_method.change_dt else exist_method.fromtimestamp(0, tz=timezone.utc)
        new_change_dt = method_obj.changeDateTime if method_obj.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_change_dt > exist_change_dt):
            exist_method.guid = method_obj.guid
            exist_method.create_dt = method_obj.changeDateTime
            exist_method.change_dt = method_obj.createDateTime
            exist_method.start_date_active = method_obj.startDateActive
            exist_method.end_date_active = method_obj.endDateActive
            exist_method.business_status = method_obj.businessStatus
            exist_method.name = method_obj.name
            exist_method.parent_code = method_obj.parentCode
            exist_method.order_number = method_obj.orderNumber
            exist_method.is_electronic = False if method_obj.isElectronic is None else method_obj.isElectronic

            exist_method.creator_inn = None if method_obj.creator is None else method_obj.creator.inn
            exist_method.creator_kpp = None if method_obj.creator is None else method_obj.creator.kpp
            exist_method.creator_ogrn = None if method_obj.creator is None else method_obj.creator.ogrn

            exist_method.extended = method_obj.extended
            exist_method.competitive = method_obj.competitive

            exist_method.protocol_controlled_order = None if method_obj.protocols is None else method_obj.protocols.controlledOrder

            exist_method.has_phases = method_obj.hasPhases
            exist_method.typal = method_obj.typal
            exist_method.typal_kind = method_obj.typalKind
            exist_method.lot_oriented = method_obj.lotOriented

            fill_templates(session, exist_method, method_obj.templates)
            fill_protocols(session, exist_method, method_obj.protocols, get_protocol_association)
            fill_phases(session, exist_method, method_obj.phases)

def fill_templates(session, owner:NsiPurchaseMethod, templates_obj:templatesType29):
    owner.templates = []
    if templates_obj is None:
        return

    for template_obj in templates_obj.template:
        template_as = get_template_association(session, template_obj)
        if template_as:
            owner.templates.append(template_as)

def get_template_association(session, template_obj:noticeTemplateType):
    if template_obj is None:
        return None

    long_id = template_obj.id
    parent_id = template_obj.parent
    template = session.query(NsiTemplateBase).filter(NsiTemplateBase.parent_long_id == parent_id, NsiTemplateBase.long_id == long_id).one_or_none()

    if template is None:
        template = NsiNoticeTemplate(
            long_id = long_id,
            parent_long_id = parent_id,
            status = template_obj.status,
            version = template_obj.version,

            copy_of_type = template_obj.copyOfType if template_obj.copyOfType and template_obj.validate_templateExtendPurchaseTypes(template_obj.copyOfType) else NOT_VALIDATE_VALUE,
            hidden_fields = template_obj.hiddenFields if template_obj.hiddenFields and template_obj.validate_hiddenFieldsType(template_obj.hiddenFields) else NOT_VALIDATE_VALUE
        )

        if template_obj.fields:
            for field_obj in template_obj.fields.field:
                field = get_notice_field(session, field_obj)
                if field:
                    template.fields.append(field)

    template_as = NsiPurchMethodTemplateAs()
    template_as.template = template

    return template_as

def get_notice_field(session, fields_obj:noticeTemplateFieldType):
    if fields_obj is None:
        return None

    field = NsiNoticeFieldTemplate(
        long_id = fields_obj.id,
        name = fields_obj.name,
        extend_type = fields_obj.type_,
        length = fields_obj.length,
        mandatory = fields_obj.mandatory,

        tab_ordinal = fields_obj.position.tabOrdinal,
        tab_name = fields_obj.position.tabName,
        section_ordinal = fields_obj.position.sectionOrdinal,
        section_name = fields_obj.position.sectionName,

        info = fields_obj.typeInfo,
        integr_code = fields_obj.integrCode,
        index_number = fields_obj.indexNumber,
        code = fields_obj.code,

        tab_level = fields_obj.tabLevel,
        is_base_field = fields_obj.isBaseField
    )

    field.table_type = get_table_type(session, fields_obj.tableType)

    return field

def get_table_type(session, template_table_obj:templateTableType):
    if template_table_obj is None:
        return None

    long_id = template_table_obj.id
    table = session.query(NsiTableTemplate).filter(NsiTableTemplate.long_id == long_id).one_or_none()

    if table is None:
        table = NsiTableTemplate(
            long_id = long_id,
            name = template_table_obj.name
        )

        if template_table_obj.fixedColumnsData:
            for fixed_column_data_obj in template_table_obj.fixedColumnsData.colValue:
                fixed_column_data = get_table_fixed_column_data(session, fixed_column_data_obj)
                if fixed_column_data:
                    table.fixed_columns_data.append(fixed_column_data)

        if template_table_obj.columns:
            for column_obj in template_table_obj.columns.column:
                column = get_table_column(session, column_obj)
                if column:
                    table.columns.append(column)

    return table

def get_table_fixed_column_data(session, fixed_column_data_obj:str):
    if fixed_column_data_obj is None:
        return None
        
    fixed_column_data = NsiTableTemplateFixedColumnData(
        value = fixed_column_data_obj
    )

    return fixed_column_data

def get_table_column(session, column_obj:templateTableColumnType):
    if column_obj is None:
        return None

    column = NsiTableColumnTemplate(
        index = column_obj.colIndex,
        name = column_obj.colName,
        extend_type = column_obj.colType,
        length = column_obj.colLength,
        mandatory = column_obj.colMandatory,
        integr_code = column_obj.integrCode,
        info = column_obj.typeInfo
    )

    return column

def fill_protocols(session, owner, protocols_obj:protocolListType, get_association:callable):
    owner.protocols = []
    if protocols_obj is None:
        return

    for protocol_obj in protocols_obj.protocol:
        protocol_as = get_association(session, owner, protocol_obj)
        if protocol_as:
            owner.protocols.append(protocol_as)

def get_protocol_association(session, owner:NsiPurchaseMethod, protocol_obj:purchaseProtocol):
    if protocol_obj is None:
        return None

    code = protocol_obj.code

    protocol = [p_as.protocol for p_as in owner.protocols if p_as.protocol.code == code]
    if protocol:
        protocol = protocol[0]
    else:
        protocol = session.query(NsiPurchaseProtocol).filter(NsiPurchaseProtocol.code == code).one_or_none()

    if protocol is None:
        protocol = NsiPurchaseProtocol(
            code = code,
            name = protocol_obj.name
        )

    protocol_as = NsiPurchMethodProtocolAs()
    protocol_as.protocol = protocol

    return protocol_as

def fill_phases(session, owner:NsiPurchaseMethod, phases_obj:purchasePhaseListType):
    owner.phases = []
    if phases_obj is None:
        return

    for phase_obj in phases_obj.phase:
        phase_as = get_phase_association(session, owner, phase_obj)
        if phase_as:
            owner.phases.append(phase_as)

def get_phase_association(session, owner:NsiPurchaseMethod, phase_obj:purchasePhase):
    if phase_obj is None:
        return None

    code = phase_obj.code

    phase = [p_as.phase for p_as in owner.phases if p_as.phase.code == code]
    if phase:
        phase = phase[0]
    else:
        phase = session.query(NsiPurchasePhase).filter(NsiPurchasePhase.code == code).one_or_none()

    if phase is None:
        phase = NsiPurchasePhase(
            order_number = phase_obj.orderNumber,
            code = code,
            name = phase_obj.name,
            edit_enabled = phase_obj.editEnabled,
            protocol_controlled_order = None if phase_obj.protocols is None else phase_obj.protocols.controlledOrder
        )

        fill_protocols(session, phase, phase_obj.protocols, get_phase_protocol_association)
        fill_phase_transitions(session, phase, phase_obj.phaseTransitions)

    phase_as = NsiPurchMethodPhaseAs()
    phase_as.phase = phase

    return phase_as

def get_phase_protocol_association(session, owner:NsiPurchasePhase, protocol_obj:purchaseProtocol):
    if protocol_obj is None:
        return None

    code = protocol_obj.code

    protocol = [p_as.protocol for p_as in owner.protocols if p_as.protocol.code == code]
    if protocol:
        protocol = protocol[0]
    else:
        protocol = session.query(NsiPurchaseProtocol).filter(NsiPurchaseProtocol.code == code).one_or_none()

    if protocol is None:
        protocol = NsiPurchaseProtocol(
            code = code,
            name = protocol_obj.name
        )

    protocol_as = NsiPurchPhaseProtocolAs()
    protocol_as.protocol = protocol

    return protocol_as

def fill_phase_transitions(session, owner:NsiPurchasePhase, transitions_obj:phaseTransitionsListType):
    owner.transitions = []
    if transitions_obj is None:
        return

    for transition_obj in transitions_obj.transition:
        transition_as = get_transition_association(session, owner, transition_obj)
        if transition_as:
            owner.transitions.append(transition_as)

def get_transition_association(session, owner:NsiPurchasePhase, transition_obj:phaseTransition):
    if transition_obj is None:
        return None

    protocol_code = transition_obj.protocolCode
    phase_code = transition_obj.phaseCode

    transition = [t_as.transition for t_as in owner.transitions if t_as.transition.protocol_code == protocol_code and t_as.transition.phase_code == phase_code]
    if transition:
        transition = transition[0]
    else:
        transition = session.query(NsiPurchasePhaseTransition).filter(NsiPurchasePhaseTransition.protocol_code == protocol_code, NsiPurchasePhaseTransition.phase_code == phase_code).one_or_none()

    if transition is None:
        transition = NsiPurchasePhaseTransition(
            protocol_code = protocol_code,
            phase_code = phase_code
        )

    transition_as = NsiPurchPhaseTransitionAs()
    transition_as.transition = transition

    return transition_as