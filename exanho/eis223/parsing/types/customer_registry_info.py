from ...ds.customer_registry import customerRegistryInfoType
from ...model.nsi_customer import *


def get_customer_registry_info(session, customer_obj:customerRegistryInfoType, update=True) -> CustomerRegistryInfo:
    if customer_obj is None:
        return None

    ogrn = '' if customer_obj.ogrn is None else customer_obj.ogrn
    inn = '' if customer_obj.inn is None else customer_obj.inn
    kpp = '' if customer_obj.kpp is None else customer_obj.kpp
    customer = None

    if inn:
        customer = session.query(CustomerRegistryInfo).filter(CustomerRegistryInfo.inn == inn, CustomerRegistryInfo.kpp == kpp).one_or_none()
    if customer is None:
        customer = session.query(CustomerRegistryInfo).filter(CustomerRegistryInfo.ogrn == ogrn, CustomerRegistryInfo.inn == inn, CustomerRegistryInfo.kpp == kpp).one_or_none()

    if customer is None:
        customer = CustomerRegistryInfo(
            full_name = customer_obj.fullName,

            ogrn = ogrn,
            inn = inn,
            kpp = kpp,

            reg_date = customer_obj.customerRegistrationDate,
            legal_address = customer_obj.legalAddress,
            website = customer_obj.website,
            iko = customer_obj.iko,
            create_iko_dt = customer_obj.createIkoDate,

            time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset,
            time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name,

            postal_address = customer_obj.postalAddress,
            email_system = customer_obj.emailSystem,
            email = customer_obj.email,
            phone = customer_obj.phone,
            fax = customer_obj.fax
        )

        session.add(customer)
    elif update:
        customer.full_name = customer_obj.fullName

        if customer.ogrn is None: customer.ogrn = ogrn

        customer.reg_date = customer_obj.customerRegistrationDate
        customer.legal_address = customer_obj.legalAddress
        customer.website = customer_obj.website
        customer.iko = customer_obj.iko
        customer.create_iko_dt = customer_obj.createIkoDate

        customer.time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset
        customer.time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name

        customer.postal_address = customer_obj.postalAddress
        customer.email_system = customer_obj.emailSystem
        customer.email = customer_obj.email
        customer.phone = customer_obj.phone
        customer.fax = customer_obj.fax
    else:
        if customer.full_name is None: customer.full_name = customer_obj.fullName

        if customer.ogrn is None: customer.ogrn = ogrn

        if customer.reg_date is None: customer.reg_date = customer_obj.customerRegistrationDate
        if customer.legal_address is None: customer.legal_address = customer_obj.legalAddress
        if customer.website is None: customer.website = customer_obj.website
        if customer.iko is None: customer.iko = customer_obj.iko
        if customer.create_iko_dt is None: customer.create_iko_dt = customer_obj.createIkoDate

        if customer.time_zone_offset is None: customer.time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset
        if customer.time_zone_name is None: customer.time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name

        if customer.postal_address is None: customer.postal_address = customer_obj.postalAddress
        if customer.email_system is None: customer.email_system = customer_obj.emailSystem
        if customer.email is None: customer.email = customer_obj.email
        if customer.phone is None: customer.phone = customer_obj.phone
        if customer.fax is None: customer.fax = customer_obj.fax
    
    return customer