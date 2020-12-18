from datetime import datetime, timezone

from exanho.core.common import Error

from ...ds.customer_registry import nsiCustomer, customerRegistryDataType, contactInfoType
from ...model.nsi_registry import *
from ...model.nsi_customer import NsiFz223type
from ..types.customer_registry_info import get_customer_registry_info

UNDEFINED_SECTION = '?'
NOT_VALIDATE_VALUE = '???'

def parse(session, root_obj:nsiCustomer, update=True, **kwargs):
    for item in root_obj.body.item:
        try:
            with session.begin_nested():
                parse_customer(session, item.customerRegistryData, update)
        except:
            raise
        

def parse_customer(session, cust_reg_obj:customerRegistryDataType, update=True):

    customer = get_customer_registry_info(session, cust_reg_obj.customerRegistryMainInfo, update)
    if customer is None:
        raise Error('customer is None')

    reg_number = cust_reg_obj.registrationNumber

    exist_cust_reg = session.query(NsiCustomerRegistry).filter(NsiCustomerRegistry.registration_number == reg_number).one_or_none()
    
    if exist_cust_reg is None:

        new_cust_reg = NsiCustomerRegistry(
            registration_number = reg_number,
            version = cust_reg_obj.version,
            version_creation_dt = cust_reg_obj.versionCreationDate,
            status = cust_reg_obj.registryStatus,
            added_dt = cust_reg_obj.addedToRegistryDate,
            removed_dt = cust_reg_obj.removedFromRegistryDate,

            okpo = cust_reg_obj.classification.okpo if cust_reg_obj.classification.validate_codeOkpoType(cust_reg_obj.classification.okpo) else NOT_VALIDATE_VALUE,
            okpo_name = cust_reg_obj.classification.okpoName,
            okato = cust_reg_obj.classification.okato,
            okato_name = cust_reg_obj.classification.okatoName,
            oktmo = cust_reg_obj.classification.oktmo,
            oktmo_name = cust_reg_obj.classification.oktmoName,
            okfs = cust_reg_obj.classification.okfs,
            okfs_name = cust_reg_obj.classification.okfsName,
            okopf = cust_reg_obj.classification.okopf,
            okopf_name = cust_reg_obj.classification.okopfName,

            is_customer = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isCustomer,
            is_customer_representative = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isCustomerRepresentative,
            is_supervisor = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isSupervisor,
            is_operator = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOperator,
            is_ovk = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOVK,
            is_purchase_audit = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isPurchaseAudit,
            is_monitoring = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isMonitoring,
            is_assessment = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isAssessment,
            is_typal_order_clause = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isTypalOrderClause,
            is_operator_em = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOperatorEM,

            is_ppo = False if cust_reg_obj.ppo is None or cust_reg_obj.ppo.isPpo is None else cust_reg_obj.ppo.isPpo,
            ppo_code = None if cust_reg_obj.ppo is None or cust_reg_obj.ppo.code is None else cust_reg_obj.ppo.code,
            ppo_name = None if cust_reg_obj.ppo is None or cust_reg_obj.ppo.name is None else cust_reg_obj.ppo.name,
        )

        new_cust_reg.customer = customer
        session.add(new_cust_reg)

        fill_ikuls(session, new_cust_reg, cust_reg_obj.ikuls)
        fill_okved_activities(session, new_cust_reg, cust_reg_obj.classification.okved)
        fill_okved2_activities(session, new_cust_reg, cust_reg_obj.classification.okved2)
        fill_fz223types(session, new_cust_reg, cust_reg_obj.classification.fz223types)

        new_cust_reg.contact = get_contact(session, cust_reg_obj.contactInfo)

        fill_granted_users(session, new_cust_reg, cust_reg_obj.grantedUsersWoAttorney)
        fill_capital_stock_agencies(session, new_cust_reg, cust_reg_obj.capitalStockAgencies)

    else:
        exist_version_creation_dt = exist_cust_reg.version_creation_dt if exist_cust_reg.version_creation_dt else datetime.min
        new_version_creation_dt = cust_reg_obj.versionCreationDate if cust_reg_obj.versionCreationDate else datetime.min

        if update or (new_version_creation_dt > exist_version_creation_dt):
            exist_cust_reg.customer = customer

            exist_cust_reg.registration_number = reg_number
            exist_cust_reg.version = cust_reg_obj.version
            exist_cust_reg.version_creation_dt = new_version_creation_dt
            exist_cust_reg.status = cust_reg_obj.registryStatus
            exist_cust_reg.added_dt = cust_reg_obj.addedToRegistryDate
            exist_cust_reg.removed_dt = cust_reg_obj.removedFromRegistryDate

            exist_cust_reg.okpo = cust_reg_obj.classification.okpo
            exist_cust_reg.okpo_name = cust_reg_obj.classification.okpoName
            exist_cust_reg.okato = cust_reg_obj.classification.okato
            exist_cust_reg.okato_name = cust_reg_obj.classification.okatoName
            exist_cust_reg.oktmo = cust_reg_obj.classification.oktmo
            exist_cust_reg.oktmo_name = cust_reg_obj.classification.oktmoName
            exist_cust_reg.okfs = cust_reg_obj.classification.okfs
            exist_cust_reg.okfs_name = cust_reg_obj.classification.okfsName
            exist_cust_reg.okopf = cust_reg_obj.classification.okopf
            exist_cust_reg.okopf_name = cust_reg_obj.classification.okopfName

            exist_cust_reg.is_customer = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isCustomer
            exist_cust_reg.is_customer_representative = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isCustomerRepresentative
            exist_cust_reg.is_supervisor = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isSupervisor
            exist_cust_reg.is_operator = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOperator
            exist_cust_reg.is_ovk = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOVK
            exist_cust_reg.is_purchase_audit = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isPurchaseAudit
            exist_cust_reg.is_monitoring = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isMonitoring
            exist_cust_reg.is_assessment = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isAssessment
            exist_cust_reg.is_typal_order_clause = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isTypalOrderClause
            exist_cust_reg.is_operator_em = False if cust_reg_obj.authority is None else cust_reg_obj.authority.isOperatorEM

            exist_cust_reg.is_ppo = False if cust_reg_obj.ppo is None or cust_reg_obj.ppo.isPpo is None else cust_reg_obj.ppo.isPpo
            exist_cust_reg.ppo_code = None if cust_reg_obj.ppo is None or cust_reg_obj.ppo.code is None else cust_reg_obj.ppo.code
            exist_cust_reg.ppo_name = None if cust_reg_obj.ppo is None or cust_reg_obj.ppo.name is None else cust_reg_obj.ppo.name

            fill_ikuls(session, exist_cust_reg, cust_reg_obj.ikuls)
            fill_okved_activities(session, exist_cust_reg, cust_reg_obj.classification.okved)
            fill_okved2_activities(session, exist_cust_reg, cust_reg_obj.classification.okved2)
            fill_fz223types(session, exist_cust_reg, cust_reg_obj.classification.fz223types)

            exist_cust_reg.contact = get_contact(session, cust_reg_obj.contactInfo)

            fill_granted_users(session, exist_cust_reg, cust_reg_obj.grantedUsersWoAttorney)
            fill_capital_stock_agencies(session, exist_cust_reg, cust_reg_obj.capitalStockAgencies)

def fill_ikuls(session, owner:NsiCustomerRegistry, ikuls_obj:list):
    owner.ikuls = []
    if ikuls_obj is None:
        return

    for ikul_obj in ikuls_obj:
        if ikul_obj is None:
            continue

        ikul = NsiRegIkul(
                code = ikul_obj.ikulCode,
                name = ikul_obj.ikulName,
                assignment_dt = ikul_obj.assignmentDate
            )
        session.add(ikul)
        owner.ikuls.append(ikul)

def fill_okved_activities(session, owner:NsiCustomerRegistry, okveds_obj:list):
    owner.okved_list = []
    if okveds_obj is None:
        return

    for okved_obj in okveds_obj:
        if okved_obj is None:
            continue

        code = okved_obj.code
        is_main = okved_obj.isMain
        name = okved_obj.name
        okved = session.query(NsiRegOkved).filter(NsiRegOkved.code == code, NsiRegOkved.name == name, NsiRegOkved.is_main == is_main).one_or_none()

        if okved is None:
            okved = NsiRegOkved(
                code = code,
                is_main = is_main,
                name = name                
            )
            session.add(okved)
        
        if session.query(NsiRegOkvedActivity).filter(NsiRegOkvedActivity.customer == owner, NsiRegOkvedActivity.okved == okved).count() > 0:
            continue
        
        activity = NsiRegOkvedActivity()
        activity.okved = okved
        session.add(activity)
        owner.okved_list.append(activity)

def fill_okved2_activities(session, owner:NsiCustomerRegistry, okved2s_obj:list) -> list:
    owner.okved2_list = []
    if okved2s_obj is None:
        return

    for okved2_obj in okved2s_obj:
        if okved2_obj is None:
            continue

        code = okved2_obj.code
        is_main = okved2_obj.isMain
        name = okved2_obj.name
        okved2 = session.query(NsiRegOkved2).filter(NsiRegOkved2.code == code, NsiRegOkved2.name == name, NsiRegOkved2.is_main == is_main).one_or_none()

        if okved2 is None:
            okved2 = NsiRegOkved2(
                code = code,
                is_main = is_main,
                name = name                
            )
            session.add(okved2)
        
        if session.query(NsiRegOkved2Activity).filter(NsiRegOkved2Activity.customer == owner, NsiRegOkved2Activity.okved2 == okved2).count() > 0:
            continue
        
        activity = NsiRegOkved2Activity()
        activity.okved2 = okved2
        session.add(activity)
        owner.okved2_list.append(activity)

def fill_fz223types(session, owner:NsiCustomerRegistry, fz223types_obj:list) -> list:
    owner.fz223types = []
    if fz223types_obj is None:
        return

    for fz223type_obj in fz223types_obj:

        code = fz223type_obj.code
        fz223type = session.query(NsiFz223type).filter(NsiFz223type.code == code).one_or_none()

        if fz223type is None:
            fz223type = NsiFz223type(
                code = code,
                name = fz223type_obj.name
            )
            session.add(fz223type)

        fz223type_as = NsiRegClassificationFz223type()
        fz223type_as.fz223type = fz223type
        session.add(fz223type_as)

        owner.fz223types.append(fz223type_as)
         
def get_contact(session, contact_obj:contactInfoType) -> NsiRegContact:
    if contact_obj is None:
        return None

    contact = NsiRegContact(
        first_name = contact_obj.firstName,
        middle_name = contact_obj.middleName,
        last_name = contact_obj.lastName,

        phone = contact_obj.phone,
        fax = contact_obj.fax,
        email = contact_obj.email,
        additional = contact_obj.additionalContactInfo
    )
    session.add(contact)
    return contact

def fill_granted_users(session, owner:NsiCustomerRegistry, granted_users_obj:list):
    owner.granted_users = []
    if granted_users_obj is None:
        return

    for granted_user_obj in granted_users_obj:
        if granted_user_obj is None:
            continue

        granted_user = NsiRegGrantedUser(
            last_name = granted_user_obj.lastName,
            first_name = granted_user_obj.firstName,
            middle_name = granted_user_obj.middleName,
            inn = granted_user_obj.inn,
            position = granted_user_obj.position
            )
        session.add(granted_user)
        owner.granted_users.append(granted_user)

def fill_capital_stock_agencies(session, owner:NsiCustomerRegistry, capital_stock_agencies_obj:list) -> list:
    owner.capital_stock_agencies = []
    if capital_stock_agencies_obj is None:
        return

    for capital_stock_agency_obj in capital_stock_agencies_obj:
        if capital_stock_agency_obj is None:
            continue

        capital_stock_agency = NsiRegCapitalStockAgency(
            full_name = capital_stock_agency_obj.fullName,
            ogrn = capital_stock_agency_obj.ogrn,
            inn = capital_stock_agency_obj.inn,
            kpp = capital_stock_agency_obj.kpp
        )
        session.add(capital_stock_agency)
        owner.capital_stock_agencies.append(capital_stock_agency)