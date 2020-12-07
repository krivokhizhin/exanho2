from ...ds.reference import customerMainInfoType
from ...model.nsi_customer import *


def get_customer_main_info(session, customer_obj:customerMainInfoType, update=True) -> CustomerMainInfo:
    if customer_obj is None:
        return None

    inn = customer_obj.inn
    kpp = customer_obj.kpp
    ogrn = customer_obj.ogrn

    customer = session.query(CustomerMainInfo).filter(CustomerMainInfo.inn == inn, CustomerMainInfo.kpp == kpp).one_or_none()
    if customer is None:
        customer = session.query(CustomerMainInfo).filter(CustomerMainInfo.ogrn == ogrn, CustomerMainInfo.inn == inn, CustomerMainInfo.kpp == kpp).one_or_none()

    if customer is None:
        customer = CustomerMainInfo(
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
        if customer.full_name is None: customer.full_name = customer_obj.fullName
        if customer.short_name is None: customer.short_name = customer_obj.shortName
        if customer.iko is None: customer.iko = customer_obj.iko

        if customer.ogrn is None: customer.ogrn = ogrn

        if customer.legal_address is None: customer.legal_address = customer_obj.legalAddress
        if customer.postal_address is None: customer.postal_address = customer_obj.postalAddress
        if customer.phone is None: customer.phone = customer_obj.phone
        if customer.fax is None: customer.fax = customer_obj.fax
        if customer.email is None: customer.email = customer_obj.email

        if customer.okato is None: customer.okato = customer_obj.okato
        if customer.okopf is None: customer.okopf = customer_obj.okopf
        if customer.okopf_name is None: customer.okopf_name = customer_obj.okopfName
        if customer.okpo is None: customer.okpo = customer_obj.okpo

        if customer.reg_date is None: customer.reg_date = customer_obj.customerRegistrationDate
        if customer.time_zone_offset is None: customer.time_zone_offset = None if customer_obj.timeZone is None else customer_obj.timeZone.offset
        if customer.time_zone_name is None: customer.time_zone_name = None if customer_obj.timeZone is None else customer_obj.timeZone.name
        if customer.region is None: customer.region = customer_obj.region
        if customer.assessed_compliance is None: customer.assessed_compliance = customer_obj.customerAssessedCompliance
        if customer.monitored_compliance is None: customer.monitored_compliance = customer_obj.customerMonitoredCompliance
    
    return customer