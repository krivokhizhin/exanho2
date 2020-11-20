from datetime import datetime, timezone

from exanho.core.common import Error

from ...ds.reference import nsiOrganization, nsiOrganizationDataType, customerMainInfoType, activitiesType, fz223typesType, contactInfoType24, SuccessionInfo, okvedType, okved2Type, businessStatusType
from ...model.nsi_organization import *

UNDEFINED_SECTION = '?'
NOT_VALIDATE_VALUE = '???'

def parse(session, root_obj:nsiOrganization, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_organization(session, item.nsiOrganizationData, update)
        except:
            raise
        

def parse_organization(session, org_obj:nsiOrganizationDataType, update=True):

    customer = get_customer(session, org_obj.mainInfo, update)
    if customer is None:
        raise Error('customer is None')

    exist_org = session.query(NsiOrganization).filter(NsiOrganization.customer == customer).one_or_none()
    
    if exist_org is None:

        new_org = NsiOrganization(
            guid = org_obj.guid,
            code = org_obj.code,
            code_assign_dt = org_obj.codeAssignDateTime,
            code_invalidate_dt = org_obj.codeInvalidateDateTime,
            create_dt = org_obj.createDateTime,
            change_dt = org_obj.changeDateTime,
            block_dt = org_obj.blockDateTime,
            change_esia_dt = org_obj.changeESIADateTime,
            start_date_active = org_obj.startDateActive,
            end_date_active = org_obj.endDateActive,

            status = org_obj.status,
            okfs = org_obj.classification.okfs,
            okopf = org_obj.classification.okopf,
            okato = org_obj.classification.okato,
            oktmo = org_obj.classification.oktmo,
            okpo = org_obj.classification.okpo if org_obj.classification.validate_codeOkpoType(org_obj.classification.okpo) else NOT_VALIDATE_VALUE,

            spz_code = org_obj.classification.spzCode,
            pgmu_code = org_obj.classification.pgmuCode,
            rf_subject_code = org_obj.classification.rfSubjectCode,

            is_ppo = False if org_obj.classification.ppo is None or org_obj.classification.ppo.isPpo is None else org_obj.classification.ppo.isPpo,
            ppo_code = None if org_obj.classification.ppo is None or org_obj.classification.ppo.code is None else org_obj.classification.ppo.code,
            ppo_name = None if org_obj.classification.ppo is None or org_obj.classification.ppo.name is None else org_obj.classification.ppo.name,

            time_zone_offset = org_obj.additionalInfo.timeZone.offset, # None if org_obj.additionalInfo is None or org_obj.additionalInfo.timeZone is None else org_obj.additionalInfo.timeZone.offset,
            time_zone_name = org_obj.additionalInfo.timeZone.name, # None if org_obj.additionalInfo is None or org_obj.additionalInfo.timeZone is None else org_obj.additionalInfo.timeZone.name,

            is_detached_department = org_obj.isDetachedDepartment,

            is_customer = False if org_obj.authority is None else org_obj.authority.isCustomer,
            is_customer_agent = False if org_obj.authority is None else org_obj.authority.isCustomerAgent,
            is_supervisor = False if org_obj.authority is None else org_obj.authority.isSupervisor,
            is_operator = False if org_obj.authority is None else org_obj.authority.isOperator,
            is_ovk = False if org_obj.authority is None else org_obj.authority.isOVK,
            is_purchase_audit = False if org_obj.authority is None else org_obj.authority.isPurchaseAudit,
            is_monitoring = False if org_obj.authority is None else org_obj.authority.isMonitoring,
            is_assessment = False if org_obj.authority is None else org_obj.authority.isAssessment,
            is_typal_order_clause = False if org_obj.authority is None else org_obj.authority.isTypalOrderClause,
            is_operator_em = False if org_obj.authority is None else org_obj.authority.isOperatorEM,

            comment = org_obj.comment
        )

        new_org.customer = customer
        session.add(new_org)

        fill_okved_activities(session, new_org, org_obj.classification.activities)
        fill_okved2_activities(session, new_org, org_obj.classification.activities)
        fill_fz223types(session, new_org, org_obj.classification.fz223types)
        new_org.contact = get_contact(session, org_obj.contactInfo)
        fill_successors(session, new_org, org_obj.successionInfo)

    else:
        exist_change_dt = exist_org.change_dt if exist_org.change_dt else datetime.fromtimestamp(0, tz=timezone.utc)
        new_change_dt = org_obj.changeDateTime if org_obj.changeDateTime else datetime.fromtimestamp(0, tz=timezone.utc)

        if update or (new_change_dt > exist_change_dt):
            exist_org.guid = org_obj.guid
            exist_org.code = org_obj.code
            exist_org.code_assign_dt = org_obj.codeAssignDateTime
            exist_org.code_invalidate_dt = org_obj.codeInvalidateDateTime
            exist_org.create_dt = org_obj.createDateTime
            exist_org.change_dt = org_obj.changeDateTime
            exist_org.block_dt = org_obj.blockDateTime
            exist_org.change_esia_dt = org_obj.changeESIADateTime
            exist_org.start_date_active = org_obj.startDateActive
            exist_org.end_date_active = org_obj.endDateActive

            exist_org.status = org_obj.status
            exist_org.okfs = org_obj.classification.okfs
            exist_org.okopf = org_obj.classification.okopf
            exist_org.okato = org_obj.classification.okato
            exist_org.oktmo = org_obj.classification.oktmo
            exist_org.okpo = org_obj.classification.okpo if org_obj.classification.validate_codeOkpoType(org_obj.classification.okpo) else NOT_VALIDATE_VALUE

            exist_org.spz_code = org_obj.classification.spzCode
            exist_org.pgmu_code = org_obj.classification.pgmuCode
            exist_org.rf_subject_code = org_obj.classification.rfSubjectCode

            exist_org.is_ppo = False if org_obj.classification.ppo is None or org_obj.classification.ppo.isPpo is None else org_obj.classification.ppo.isPpo
            exist_org.ppo_code = None if org_obj.classification.ppo is None or org_obj.classification.ppo.code is None else org_obj.classification.ppo.code
            exist_org.ppo_name = None if org_obj.classification.ppo is None or org_obj.classification.ppo.name is None else org_obj.classification.ppo.name

            exist_org.time_zone_offset = org_obj.additionalInfo.timeZone.offset # None if org_obj.additionalInfo is None or org_obj.additionalInfo.timeZone is None else org_obj.additionalInfo.timeZone.offset,
            exist_org.time_zone_name = org_obj.additionalInfo.timeZone.name # None if org_obj.additionalInfo is None or org_obj.additionalInfo.timeZone is None else org_obj.additionalInfo.timeZone.name,

            exist_org.is_detached_department = org_obj.isDetachedDepartment

            exist_org.is_customer = False if org_obj.authority is None else org_obj.authority.isCustomer
            exist_org.is_customer_agent = False if org_obj.authority is None else org_obj.authority.isCustomerAgent
            exist_org.is_supervisor = False if org_obj.authority is None else org_obj.authority.isSupervisor
            exist_org.is_operator = False if org_obj.authority is None else org_obj.authority.isOperator
            exist_org.is_ovk = False if org_obj.authority is None else org_obj.authority.isOVK
            exist_org.is_purchase_audit = False if org_obj.authority is None else org_obj.authority.isPurchaseAudit
            exist_org.is_monitoring = False if org_obj.authority is None else org_obj.authority.isMonitoring
            exist_org.is_assessment = False if org_obj.authority is None else org_obj.authority.isAssessment
            exist_org.is_typal_order_clause = False if org_obj.authority is None else org_obj.authority.isTypalOrderClause
            exist_org.is_operator_em = False if org_obj.authority is None else org_obj.authority.isOperatorEM

            exist_org.comment = org_obj.comment

            fill_okved_activities(session, exist_org, org_obj.classification.activities)
            fill_okved2_activities(session, exist_org, org_obj.classification.activities)
            fill_fz223types(session, exist_org, org_obj.classification.fz223types)
            exist_org.contact = get_contact(session, org_obj.contactInfo)
            fill_successors(session, exist_org, org_obj.successionInfo)

def get_customer(session, customer_obj:customerMainInfoType, update=True) -> NsiOrgCustomer:
    if customer_obj is None:
        return None

    inn = customer_obj.inn
    kpp = customer_obj.kpp
    ogrn = customer_obj.ogrn

    customer = session.query(NsiOrgCustomer).filter(NsiOrgCustomer.inn == inn, NsiOrgCustomer.kpp == kpp).one_or_none()
    if customer is None:
        customer = session.query(NsiOrgCustomer).filter(NsiOrgCustomer.ogrn == ogrn, NsiOrgCustomer.inn == inn, NsiOrgCustomer.kpp == kpp).one_or_none()

    if customer is None:
        customer = NsiOrgCustomer(
            full_name = customer_obj.fullName,
            short_name = customer_obj.shortName,
            iko = customer_obj.iko,

            inn = inn,
            kpp = kpp,
            ogrn = ogrn,

            legal_address = customer_obj.legalAddress,
            postal_address = customer_obj.postalAddress,
            phone = customer_obj.phone,
            fax = customer_obj.fax,
            email = customer_obj.email,

            okato = customer_obj.okato,
            okopf = customer_obj.okopf,
            okopf_name = customer_obj.okopfName,
            okpo = customer_obj.okpo,

            reg_date = customer_obj.customerRegistrationDate,
            time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset,
            time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name,
            region = customer_obj.region,
            assessed_compliance = customer_obj.customerAssessedCompliance,
            monitored_compliance = customer_obj.customerMonitoredCompliance
        )

        session.add(customer)
    elif update:
            customer.full_name = customer_obj.fullName
            customer.short_name = customer_obj.shortName
            customer.iko = customer_obj.iko

            customer.ogrn = ogrn

            customer.legal_address = customer_obj.legalAddress
            customer.postal_address = customer_obj.postalAddress
            customer.phone = customer_obj.phone
            customer.fax = customer_obj.fax
            customer.email = customer_obj.email

            customer.okato = customer_obj.okato
            customer.okopf = customer_obj.okopf
            customer.okopf_name = customer_obj.okopfName
            customer.okpo = customer_obj.okpo

            customer.reg_date = customer_obj.customerRegistrationDate
            customer.time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset
            customer.time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name
            customer.region = customer_obj.region
            customer.assessed_compliance = customer_obj.customerAssessedCompliance
            customer.monitored_compliance = customer_obj.customerMonitoredCompliance
    else:
        pass
    
    return customer

def fill_okved_activities(session, owner:NsiOrganization, activities_obj:activitiesType):
    owner.okved_list = []
    if activities_obj is None:
        return

    for okved_obj in activities_obj.okved:
        if okved_obj is None:
            continue

        code = okved_obj.code
        is_main = okved_obj.isMain
        name = okved_obj.name
        okved = session.query(NsiOrgOkved).filter(NsiOrgOkved.code == code, NsiOrgOkved.name == name, NsiOrgOkved.is_main == is_main).one_or_none()

        if okved is None:
            okved = NsiOrgOkved(
                code = code,
                is_main = is_main,
                name = name                
            )
            session.add(okved)
        
        if session.query(NsiOrgOkvedActivity).filter(NsiOrgOkvedActivity.org == owner, NsiOrgOkvedActivity.okved == okved).count() > 0:
            continue
        
        activity = NsiOrgOkvedActivity()
        activity.okved = okved
        session.add(activity)
        owner.okved_list.append(activity)

def fill_okved2_activities(session, owner:NsiOrganization, activities_obj:activitiesType) -> list:
    owner.okved2_list = []
    if activities_obj is None:
        return

    for okved2_obj in activities_obj.okved2:
        if okved2_obj is None:
            continue

        code = okved2_obj.code
        is_main = okved2_obj.isMain
        name = okved2_obj.name
        okved2 = session.query(NsiOrgOkved2).filter(NsiOrgOkved2.code == code, NsiOrgOkved2.name == name, NsiOrgOkved2.is_main == is_main).one_or_none()

        if okved2 is None:
            okved2 = NsiOrgOkved2(
                code = code,
                is_main = is_main,
                name = name                
            )
            session.add(okved2)
        
        if session.query(NsiOrgOkved2Activity).filter(NsiOrgOkved2Activity.org == owner, NsiOrgOkved2Activity.okved2 == okved2).count() > 0:
            continue
        
        activity = NsiOrgOkved2Activity()
        activity.okved2 = okved2
        session.add(activity)
        owner.okved2_list.append(activity)

def fill_fz223types(session, owner:NsiOrganization, fz223types_obj:fz223typesType) -> list:
    owner.fz223types = []
    if fz223types_obj is None:
        return

    for fz223type_obj in fz223types_obj.fz223type:
        if fz223type_obj.name is None or fz223type_obj.name == '':
            continue

        name = str(fz223type_obj.name).lower()
        fz223type = session.query(NsiOrgFz223type).filter(NsiOrgFz223type.name == name).one_or_none()

        if fz223type is None:
            fz223type = NsiOrgFz223type(name = name)
            session.add(fz223type)

        fz223type_as = NsiOrgFz223typeAs()
        fz223type_as.fz223type = fz223type
        session.add(fz223type_as)

        owner.fz223types.append(fz223type_as)
         
def get_contact(session, contact_obj:contactInfoType24) -> NsiOrgContact:
    if contact_obj is None:
        return None

    contact = NsiOrgContact(
        first_name = contact_obj.contactFirstName,
        middle_name = contact_obj.contactMiddleName,
        last_name = contact_obj.contactLastName,
        contact_email = contact_obj.contactEmail,

        phone = contact_obj.phone,
        fax = contact_obj.fax,
        email = contact_obj.email,
        website = contact_obj.website,
        additional = contact_obj.additional
    )
    session.add(contact)
    return contact

def fill_successors(session, owner:NsiOrganization, successors_obj:SuccessionInfo) -> list:
    owner.successors = []
    if successors_obj is None:
        return

    for successor_obj in successors_obj.successor:
        if successor_obj is None:
            continue

        successor = NsiOrgSuccessor(
            inn = successor_obj.inn,
            kpp = successor_obj.kpp,
            ogrn = successor_obj.ogrn,
            full_name = successor_obj.fullName,
            short_name = successor_obj.shortName
        )
        session.add(successor)
        owner.successors.append(successor)