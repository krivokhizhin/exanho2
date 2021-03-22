from hashlib import blake2b

from exanho.eis44.model.contract.participant import CntrParticipantForeign
from sqlalchemy.orm import with_polymorphic
from sqlalchemy.orm.session import Session as OrmSession

from ...ds.contracts.fcsExport import zfcs_contract2015Type
from ...ds.contracts.IntegrationTypes import suppliers, zfcs_contract2015SupplierType, corr_supplierLegalEntityRF, corr_supplierLegalEntityForeignState, corr_supplierIndividualPersonRF, corr_supplierIndividualPersonForeignState, individualPersonRFisCulture, individualPersonForeignStateisCulture
from ...ds.contracts.IntegrationTypes import zfcs_contract2015EnforcementType, qualityGuaranteeInfo, zfcs_contract2015BankGuaranteeReturnType, bankGuarantee, cashAccount, guaranteeReturn

from exanho.core.common import Error
from ...model.contract import *

NOT_PUBLISHED_VALUE = '*'
IP_FORM = 'ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНИМАТЕЛЬ'
IP_SHORT_FORM = 'ИП'
INN_LENGTH = 12

def parse(session, contract_obj:zfcs_contract2015Type, update=True, **kwargs):
    content_id = kwargs.get('content_id')

    doc_id = contract_obj.id
    external_id = contract_obj.externalId

    contract = session.query(ZfcsContract2015).filter(ZfcsContract2015.doc_id == doc_id, ZfcsContract2015.external_id == external_id).one_or_none()

    if contract is None:
        contract = ZfcsContract2015(
            doc_id = doc_id,
            external_id = external_id,
            direct_dt = contract_obj.directDate,
            publish_dt = contract_obj.publishDate,
            version_number = contract_obj.versionNumber,

            conclusion_st95_ch17_1 = contract_obj.conclusionContractSt95Ch17_1,
            protocol_date = contract_obj.protocolDate,
            doc_base = contract_obj.documentBase,
            doc_code = contract_obj.documentCode,
            sign_date = contract_obj.signDate,
            reg_num = contract_obj.regNum,
            number = contract_obj.number,
            subject = contract_obj.contractSubject,

            group_build_code = contract_obj.constructionWorksInfo.constructionWorkGroup.code if contract_obj.constructionWorksInfo else None,

            defense_number = contract_obj.defenseContractNumber,
            is_goz = contract_obj.isGOZ,
            igk = contract_obj.IGK,
            life_cycle = contract_obj.contractLifeCycle,

            is_smpo_or_sono_tender = contract_obj.isSMPOrSONOTender,
            is_smpo_or_sono_engage = contract_obj.isSMPOrSONOEngage,

            quantity_stages = contract_obj.quantityContractStages,
            execution_start_date = contract_obj.executionPeriod.startDate if contract_obj.executionPeriod else None,
            execution_end_date = contract_obj.executionPeriod.endDate if contract_obj.executionPeriod else None,

            energy_service_info = contract_obj.energyServiceContractInfo,
            href = contract_obj.href,

            current_stage = contract_obj.currentContractStage,
            okpd2okved2 = contract_obj.okpd2okved2,
            is_invalid = contract_obj.isInvalid,
            scheme_version = contract_obj.schemeVersion
        )
        session.add(contract)
    elif not update:
        return
    else:
        contract.direct_dt = contract_obj.directDate
        contract.publish_dt = contract_obj.publishDate
        contract.version_number = contract_obj.versionNumber

        contract.conclusion_st95_ch17_1 = contract_obj.conclusionContractSt95Ch17_1
        contract.protocol_date = contract_obj.protocolDate
        contract.doc_base = contract_obj.documentBase
        contract.doc_code = contract_obj.documentCode
        contract.sign_date = contract_obj.signDate
        contract.reg_num = contract_obj.regNum
        contract.number = contract_obj.number
        contract.subject = contract_obj.contractSubject

        contract.group_build_code = contract_obj.constructionWorksInfo.constructionWorkGroup.code if contract_obj.constructionWorksInfo else None

        contract.defense_number = contract_obj.defenseContractNumber
        contract.is_goz = contract_obj.isGOZ
        contract.igk = contract_obj.IGK
        contract.life_cycle = contract_obj.contractLifeCycle

        contract.is_smpo_or_sono_tender = contract_obj.isSMPOrSONOTender
        contract.is_smpo_or_sono_engage = contract_obj.isSMPOrSONOEngage

        contract.quantity_stages = contract_obj.quantityContractStages
        if contract_obj.executionPeriod: contract.execution_start_date = contract_obj.executionPeriod.startDate
        if contract_obj.executionPeriod: contract.execution_end_date = contract_obj.executionPeriod.endDate

        contract.energy_service_info = contract_obj.energyServiceContractInfo
        contract.href = contract_obj.href

        contract.current_stage = contract_obj.currentContractStage
        contract.okpd2okved2 = contract_obj.okpd2okved2
        contract.is_invalid = contract_obj.isInvalid
        contract.scheme_version = contract_obj.schemeVersion

    contract.content_id = content_id

    if contract_obj.priceInfo and contract_obj.priceInfo.rightToConcludeContractPriceInfo is None:
        contract.price = contract_obj.priceInfo.price
        contract.price_type = contract_obj.priceInfo.priceType
        contract.price_formula = contract_obj.priceInfo.priceFormula
        contract.price_formula_specified = contract_obj.priceInfo.maxPriceAndPriceFormulaSpecified
        if contract_obj.priceInfo.currency: contract.currency_code = contract_obj.priceInfo.currency.code
        if contract_obj.priceInfo.currencyRate:
            contract.currency_rate = contract_obj.priceInfo.currencyRate.rate
            contract.currency_raiting = contract_obj.priceInfo.currencyRate.raiting
        contract.price_rur = contract_obj.priceInfo.priceRUR
        contract.price_vat = contract_obj.priceInfo.priceVAT
        contract.price_vat_rur = contract_obj.priceInfo.priceVATRUR
        contract.reduced_by_taxes = contract_obj.priceInfo.amountsReducedByTaxes
    else:
        contract.right_to_conclude = True

    if contract_obj.advancePaymentSum:
        contract.advance_payment_percents = contract_obj.advancePaymentSum.sumInPercents
        contract.advance_payment_value = contract_obj.advancePaymentSum.priceValue
        contract.advance_payment_value_rur = contract_obj.advancePaymentSum.priceValueRUR

    if contract_obj.subContractorsSum:
        contract.sub_contractors_percents = contract_obj.subContractorsSum.sumInPercents
        contract.sub_contractors_value_rur = contract_obj.subContractorsSum.priceValueRUR

    fill_suppliers(session, contract, contract_obj.suppliers)

    contract.enforcements = list()
    enforcement = get_enforcement(session, contract_obj.enforcement, False)
    if enforcement:
        contract.enforcements.append(enforcement)
    subsequent_maintenance_enforcement = get_enforcement(session, contract_obj.subsequentMaintenanceEnforcement, True)
    if subsequent_maintenance_enforcement:
        contract.enforcements.append(subsequent_maintenance_enforcement)

    contract.guarantee_returns = []
    contract.quality_guarantee = get_quality_guarantee(session, contract_obj.qualityGuaranteeInfo)

    fill_guarantee_returns(session, contract, contract_obj.guaranteeReturns)


def fill_suppliers(session, owner:ZfcsContract2015, suppliers_obj:suppliers):
    owner.suppliers = []
    if suppliers_obj is None:
        return

    order = 0
    for supplier_obj in suppliers_obj.supplier:
        supplier = get_supplier(session, supplier_obj)
        if supplier:
            order += 1
            supplier.order = order
            owner.suppliers.append(supplier)

def get_supplier(session, supplier_obj:zfcs_contract2015SupplierType):
    supplier = None
    if supplier_obj is None:
        return supplier

    if supplier_obj.legalEntityRF:
        supplier = get_legal_entity_rf(session, supplier_obj.legalEntityRF)
    elif supplier_obj.individualPersonRF:
        supplier = get_individual_person_rf(session, supplier_obj.individualPersonRF)
    elif supplier_obj.legalEntityForeignState:
        supplier = get_legal_entity_fs(session, supplier_obj.legalEntityForeignState)
    elif supplier_obj.individualPersonForeignState:
        supplier = get_individual_person_fs(session, supplier_obj.individualPersonForeignState)
    elif supplier_obj.individualPersonRFisCulture:
        supplier = get_individual_culture_person_rf(session, supplier_obj.individualPersonRFisCulture)
    elif supplier_obj.individualPersonForeignStateisCulture:
        supplier = get_individual_culture_person_fs(session, supplier_obj.individualPersonForeignStateisCulture)
    elif supplier_obj.notPublishedOnEIS:
        supplier = get_not_published_on_eis(session, supplier_obj.notPublishedOnEIS)
    else:
        raise Error(f'unknown zfcs_contract2015SupplierType')

    return supplier

def get_legal_entity_rf(session, supplier_obj:corr_supplierLegalEntityRF):

    contact = None
    if supplier_obj.contactInfo:
        contact = get_contact(session, supplier_obj.contactInfo.lastName, supplier_obj.contactInfo.firstName, supplier_obj.contactInfo.middleName)

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.LERF,
        status = supplier_obj.status,
        ersmsp_inclusion_date = supplier_obj.ERSMSPInclusionDate,
        contract_price = supplier_obj.contractPrice,
        personal_account = supplier_obj.personalAccount,
        address = supplier_obj.address,
        mailing_adress = None if supplier_obj.postAdressInfo is None else supplier_obj.postAdressInfo.mailingAdress,
        mail_facility_name = None if supplier_obj.postAdressInfo is None else supplier_obj.postAdressInfo.mailFacilityName,
        post_box_number = None if supplier_obj.postAdressInfo is None else supplier_obj.postAdressInfo.postBoxNumber,
        post_address = supplier_obj.postAddress,
        
        contact_email = supplier_obj.contactEMail,
        contact_phone = supplier_obj.contactPhone
    )

    inn = supplier_obj.INN
    kpp = supplier_obj.KPP
    if inn is None:
        raise Error('inn is None')
    participant = get_participant(session, CntrParticipantKind.RF, inn, kpp)

    if supplier_obj.legalForm:
        participant.okopf_code = supplier_obj.legalForm.code
        participant.okopf_name = supplier_obj.legalForm.singularName

    if supplier_obj.fullName: participant.full_name = supplier_obj.fullName
    if supplier_obj.shortName: participant.short_name = supplier_obj.shortName
    if supplier_obj.firmName: participant.firm_name = supplier_obj.firmName

    if supplier_obj.OKPO: participant.okpo = supplier_obj.OKPO
    if supplier_obj.registrationDate: participant.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        participant.oktmo_code = supplier_obj.OKTMO.code
        participant.oktmo_name = supplier_obj.OKTMO.name

    supplier.participant = participant

    if supplier_obj.contactInfo:
        supplier.contact = contact

    return supplier

def get_individual_person_rf(session, supplier_obj:corr_supplierIndividualPersonRF):
    contact = get_contact(session, supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPRF,
        status = supplier_obj.status,
        ersmsp_inclusion_date = supplier_obj.ERSMSPInclusionDate,
        personal_account = supplier_obj.personalAccount,
        address = supplier_obj.address,
        mailing_adress = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailingAdress,
        mail_facility_name = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailFacilityName,
        post_box_number = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.postBoxNumber,
        post_address = supplier_obj.postAddress,
        
        contact_email = supplier_obj.contactEMail,
        contact_phone = supplier_obj.contactPhone,

        is_ip = supplier_obj.isIP,
        is_culture = supplier_obj.isCulture
    )

    inn = supplier_obj.INN
    if supplier_obj.isIP and inn is None:
        raise Error('inn is None')
    if inn is None:
        inn = hash_str_raw('{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else '')
    participant = get_participant(session, CntrParticipantKind.RF, inn)

    if supplier_obj.isIP:
        participant.full_name = '{0} {1} {2}'.format(IP_FORM, contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
        participant.short_name = '{0} {1} {2}.'.format(IP_SHORT_FORM, contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''
    else:
        participant.full_name = '{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
        participant.short_name = '{0} {1}.'.format(contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''

    if supplier_obj.registrationDate: participant.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        participant.oktmo_code = supplier_obj.OKTMO.code
        participant.oktmo_name = supplier_obj.OKTMO.name

    supplier.participant = participant
    supplier.contact = contact

    return supplier

def get_legal_entity_fs(session, supplier_obj:corr_supplierLegalEntityForeignState):

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.LEFS,
        status = supplier_obj.status,
        personal_account = supplier_obj.personalAccount
    )

    inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else str(supplier_obj.taxPayerCode)[:INN_LENGTH]
    kpp = supplier_obj.registerInRFTaxBodies.KPP if supplier_obj.registerInRFTaxBodies else str(supplier_obj.taxPayerCode)[INN_LENGTH:]
    if supplier_obj.registerInRFTaxBodies is None and len(str(supplier_obj.taxPayerCode))> 2*INN_LENGTH:
        raise Error(f'len({supplier_obj.taxPayerCode}) is more then {2*INN_LENGTH} symbols')

    if inn is None:
        raise Error('inn is None')
    participant = get_participant(session, CntrParticipantKind.FS, inn, kpp)

    if supplier_obj.fullName: participant.full_name = supplier_obj.fullName
    if supplier_obj.shortName: participant.short_name = supplier_obj.shortName
    if supplier_obj.firmName: participant.firm_name = supplier_obj.firmName
    if supplier_obj.fullNameLat: participant.full_name_lat = supplier_obj.fullNameLat
    if supplier_obj.taxPayerCode: participant.tax_payer_code = supplier_obj.taxPayerCode

    if supplier_obj.registerInRFTaxBodies and supplier_obj.registerInRFTaxBodies.registrationDate: participant.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate

    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            participant.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            participant.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: participant.address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: participant.post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: participant.email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: participant.phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            participant.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            participant.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.mailingAdress
        supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.mailFacilityName
        supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone

    supplier.participant = participant

    return supplier

def get_individual_person_fs(session, supplier_obj:corr_supplierIndividualPersonForeignState):
    contact = get_contact(session, supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)
    
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPFS,
        personal_account = supplier_obj.personalAccount,
        is_culture = supplier_obj.isCulture
    )

    inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else str(supplier_obj.taxPayerCode)[:INN_LENGTH]
    if supplier_obj.registerInRFTaxBodies is None and len(str(supplier_obj.taxPayerCode))> INN_LENGTH:
        inn = hash_str_raw(str(supplier_obj.taxPayerCode))

    if inn is None:
        inn = hash_str_raw('{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else '')
    participant = get_participant(session, CntrParticipantKind.FS, inn)

    participant.full_name = '{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
    participant.short_name = '{0} {1}.'.format(contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''

    participant.full_name_lat = '{0}{1}{2}'.format(supplier_obj.lastNameLat if supplier_obj.lastNameLat else '', ' '+supplier_obj.firstNameLat if supplier_obj.firstNameLat else '', ' '+supplier_obj.middleNameLat if supplier_obj.middleNameLat else '').strip()
    participant.tax_payer_code = supplier_obj.taxPayerCode

    if supplier_obj.registerInRFTaxBodies:
        if supplier_obj.registerInRFTaxBodies.registrationDate: participant.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate
        # if supplier_obj.registerInRFTaxBodies.status: supplier.status = supplier_obj.registerInRFTaxBodies.status
        # if supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate: supplier.ersmsp_inclusion_date = supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate
        # if supplier_obj.registerInRFTaxBodies.isIP: supplier.is_ip = supplier_obj.registerInRFTaxBodies.isIP
    
    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            participant.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            participant.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: participant.address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: participant.post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: participant.email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: participant.phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            participant.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            participant.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        # supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailingAdress
        # supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailFacilityName
        # supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone

    supplier.participant = participant
    supplier.contact = contact

    return supplier

def get_individual_culture_person_rf(session, supplier_obj:individualPersonRFisCulture):
    contact = get_contact(session, supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPRFC,
        status = supplier_obj.status,
        ersmsp_inclusion_date = supplier_obj.ERSMSPInclusionDate,
        personal_account = supplier_obj.personalAccount,
        address = supplier_obj.address,
        mailing_adress = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailingAdress,
        mail_facility_name = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailFacilityName,
        post_box_number = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.postBoxNumber,
        post_address = supplier_obj.postAddress,
        
        contact_email = supplier_obj.contactEMail,
        contact_phone = supplier_obj.contactPhone,

        is_ip = supplier_obj.isIP
    )

    inn = supplier_obj.INN
    if inn is None:
        inn = hash_str_raw('{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else '')
    participant = get_participant(session, CntrParticipantKind.RF, inn)

    if supplier_obj.isIP:
        participant.full_name = '{0} {1} {2}'.format(IP_FORM, contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
        participant.short_name = '{0} {1} {2}.'.format(IP_SHORT_FORM, contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''
    else:
        participant.full_name = '{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
        participant.short_name = '{0} {1}.'.format(contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''

    if supplier_obj.registrationDate: participant.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        participant.oktmo_code = supplier_obj.OKTMO.code
        participant.oktmo_name = supplier_obj.OKTMO.name

    supplier.participant = participant
    supplier.contact = contact

    return supplier

def get_individual_culture_person_fs(session, supplier_obj:individualPersonForeignStateisCulture):
    contact = get_contact(session, supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPFSC,
        personal_account = supplier_obj.personalAccount
    )

    inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else str(supplier_obj.taxPayerCode)[:INN_LENGTH]
    if supplier_obj.registerInRFTaxBodies is None and len(str(supplier_obj.taxPayerCode))> INN_LENGTH:
        raise Error(f'len({supplier_obj.taxPayerCode}) is more then {INN_LENGTH} symbols')

    if inn is None:
        inn = hash_str_raw('{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else '')
    participant = get_participant(session, CntrParticipantKind.FS, inn)

    participant.full_name = '{0} {1}'.format(contact.last_name, contact.first_name) + ' {0}'.format(contact.middle_name) if contact.middle_name else ''
    participant.short_name = '{0} {1}.'.format(contact.last_name, contact.first_name[0]) + '{0}.'.format(contact.middle_name[0]) if contact.middle_name else ''

    participant.full_name_lat = '{0}{1}{2}'.format(supplier_obj.lastNameLat if supplier_obj.lastNameLat else '', ' '+supplier_obj.firstNameLat if supplier_obj.firstNameLat else '', ' '+supplier_obj.middleNameLat if supplier_obj.middleNameLat else '').strip()
    participant.tax_payer_code = supplier_obj.taxPayerCode

    if supplier_obj.registerInRFTaxBodies:
        if supplier_obj.registerInRFTaxBodies.registrationDate: participant.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate
        # if supplier_obj.registerInRFTaxBodies.status: supplier.status = supplier_obj.registerInRFTaxBodies.status
        # if supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate: supplier.ersmsp_inclusion_date = supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate
        # if supplier_obj.registerInRFTaxBodies.isIP: supplier.is_ip = supplier_obj.registerInRFTaxBodies.isIP
    
    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            participant.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            participant.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: participant.address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: participant.post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: participant.email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: participant.phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            participant.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            participant.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        # supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailingAdress
        # supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailFacilityName
        # supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone

    supplier.participant = participant
    supplier.contact = contact

    return supplier

def get_not_published_on_eis(session, supplier_obj:bool):
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.NPEIS
    )
    supplier.participant = get_participant(session, CntrParticipantKind.RF, NOT_PUBLISHED_VALUE, NOT_PUBLISHED_VALUE)
    return supplier

def get_participant(session:OrmSession, kind:CntrParticipantKind, inn:str, kpp:str = None) -> CntrParticipantForeign:
    # rf_plus_fs = with_polymorphic(CntrParticipant, CntrParticipantForeign)
    participant = session.query(with_polymorphic(CntrParticipant, CntrParticipantForeign)).\
        filter(CntrParticipant.inn == inn, CntrParticipant.kpp == kpp).one_or_none()
    if participant is None:
        if kind == CntrParticipantKind.RF:
            participant = CntrParticipant(
                inn = inn,
                kpp = kpp
            )
        elif kind == CntrParticipantKind.FS:
            participant = CntrParticipantForeign(
                inn = inn,
                kpp = kpp
            )
        else:
            raise Error(f'Unknown participant kind ("{kind}")')
        # session.add(participant)
    elif kind != participant.kind and kind == CntrParticipantKind.FS:
        participant.kind = kind
        session.flush([participant])
        session.expire(participant)
        del participant
        participant = session.query(with_polymorphic(CntrParticipant, CntrParticipantForeign)).\
            filter(CntrParticipant.inn == inn, CntrParticipant.kpp == kpp).\
                one()
    else:
        pass

    return participant

def get_contact(session, last_name:str, first_name:str, middle_name:str) -> CntrContact:
    last_name = last_name.upper()
    first_name = first_name.upper()
    middle_name = middle_name.upper() if middle_name else None
    contact = session.query(CntrContact).filter(CntrContact.last_name == last_name, CntrContact.first_name == first_name, CntrContact.middle_name == middle_name).one_or_none()
    if contact is None:
        contact = CntrContact(
            last_name = last_name,
            first_name = first_name,
            middle_name = middle_name
        )
        # session.add(contact)

    return contact

def hash_str_raw(raw:str, lenght:int=6):
    h = blake2b(digest_size=lenght)
    h.update(raw.encode(encoding='utf-8'))
    return h.hexdigest()

def get_enforcement(session:OrmSession, enforcement_obj:zfcs_contract2015EnforcementType, is_maintenance:bool=False) -> ZfcsContract2015Enforcement:
    enforcement = None
    if enforcement_obj is None:
        return enforcement

    if enforcement_obj.bankGuarantee:
        enforcement = get_bg_enforcement(enforcement_obj.bankGuarantee)
        enforcement.is_subsequent_maintenance = is_maintenance
        session.add(enforcement)
    elif enforcement_obj.cashAccount:
        enforcement = get_ca_enforcement(enforcement_obj.cashAccount)
        enforcement.is_subsequent_maintenance = is_maintenance
        session.add(enforcement)
    else:
        pass

    return enforcement

def get_bg_enforcement(bg_enforcement_obj:bankGuarantee) -> ZfcsContract2015Enforcement:
    if bg_enforcement_obj is None:
        return None

    amount = bg_enforcement_obj.guaranteeAmount if bg_enforcement_obj.guaranteeAmount else bg_enforcement_obj.amount
    amount_rur = bg_enforcement_obj.guaranteeAmountRUR if bg_enforcement_obj.guaranteeAmountRUR else bg_enforcement_obj.amountRUR

    return ZfcsContract2015Enforcement(
        kind = CntrEnsuringKind.BG,
        currency_code = bg_enforcement_obj.currency.code if bg_enforcement_obj.currency else None,
        amount = amount,
        currency_rate = bg_enforcement_obj.currencyRate.rate if bg_enforcement_obj.currencyRate else None,
        currency_raiting = bg_enforcement_obj.currencyRate.raiting if bg_enforcement_obj.currencyRate else None,
        amount_rur = amount_rur,

        reg_number = bg_enforcement_obj.regNumber,
        reg_number_not_published = bg_enforcement_obj.regNumberNotPublishedOnEIS,
        doc_number = bg_enforcement_obj.docNumber,
        doc_number_not_published = bg_enforcement_obj.docNumberNotPublishedOnEIS
    )

def get_ca_enforcement(ca_enforcement_obj:cashAccount) -> ZfcsContract2015Enforcement:
    if ca_enforcement_obj is None:
        return None

    return ZfcsContract2015Enforcement(
        kind = CntrEnsuringKind.CA,
        currency_code = ca_enforcement_obj.currency.code if ca_enforcement_obj.currency else None,
        amount = ca_enforcement_obj.amount,
        currency_rate = ca_enforcement_obj.currencyRate.rate if ca_enforcement_obj.currencyRate else None,
        currency_raiting = ca_enforcement_obj.currencyRate.raiting if ca_enforcement_obj.currencyRate else None,
        amount_rur = ca_enforcement_obj.amountRUR
    )

def get_quality_guarantee(session:OrmSession, quality_guarantee_obj:qualityGuaranteeInfo) -> CntrQualityGuaranteeInfo:
    quality_guarantee = None
    if quality_guarantee_obj is None:
        return quality_guarantee

    quality_guarantee = CntrQualityGuaranteeInfo(
        warranty_reqs_text = quality_guarantee_obj.warrantyReqsText,
        manufacturer_warranty_reqs_text = quality_guarantee_obj.manufacturerWarrantyReqsText,
        isQAEnsuramceRequired = quality_guarantee_obj.isQAEnsuramceRequired
    )

    if quality_guarantee_obj.providedPeriod:
        quality_guarantee.from_date = quality_guarantee_obj.providedPeriod.fromDate
        quality_guarantee.to_date = quality_guarantee_obj.providedPeriod.toDate
        quality_guarantee.other_period_text = quality_guarantee_obj.providedPeriod.otherPeriodText
    else:
        quality_guarantee.period_not_published = quality_guarantee_obj.notPublishedOnEIS

    if quality_guarantee_obj.execObligationsGuaranteeInfo:
        if quality_guarantee_obj.execObligationsGuaranteeInfo.ensuringWay:
            ensuring_way = None
            if quality_guarantee_obj.execObligationsGuaranteeInfo.ensuringWay.bankGuarantee:
                ensuring_way = get_bg_enforcement(quality_guarantee_obj.execObligationsGuaranteeInfo.ensuringWay.bankGuarantee)
            elif quality_guarantee_obj.execObligationsGuaranteeInfo.ensuringWay.cashAccount:
                ensuring_way = get_ca_enforcement(quality_guarantee_obj.execObligationsGuaranteeInfo.ensuringWay.cashAccount)

            if ensuring_way:                
                session.add(ensuring_way)
                quality_guarantee.ensuring_way = ensuring_way

        if quality_guarantee_obj.execObligationsGuaranteeInfo.guaranteeReturns:
            fill_guarantee_returns_for_obligations(session, quality_guarantee, quality_guarantee_obj.execObligationsGuaranteeInfo.guaranteeReturns)

    return quality_guarantee

def fill_guarantee_returns(session:OrmSession, owner:ZfcsContract2015, guarantee_returns_obj:zfcs_contract2015BankGuaranteeReturnType):    
    if guarantee_returns_obj is None:
        return

    for guarantee_return_obj in guarantee_returns_obj.guaranteeReturn:
        guarantee_return = get_guarantee_return(guarantee_return_obj)
        if guarantee_return:
            session.add(guarantee_return)
            owner.guarantee_returns.append(guarantee_return)

def fill_guarantee_returns_for_obligations(session:OrmSession, owner:CntrQualityGuaranteeInfo, guarantee_returns_obj:zfcs_contract2015BankGuaranteeReturnType):
    if guarantee_returns_obj is None:
        return

    for guarantee_return_obj in guarantee_returns_obj.guaranteeReturn:
        guarantee_return = get_guarantee_return(guarantee_return_obj)
        if guarantee_return:
            session.add(guarantee_return)
            owner.guarantee_returns.append(guarantee_return)

def get_guarantee_return(guarantee_return_obj:guaranteeReturn) -> ZfcsContract2015BgReturn:
    guarantee_return = None
    if guarantee_return_obj is None:
        return guarantee_return

    if guarantee_return_obj.bankGuaranteeReturn:
        guarantee_return = ZfcsContract2015BgReturn(
            kind = CntrBgReturnKind.RETURN,
            reg_number = guarantee_return_obj.bankGuaranteeReturn.regNumber,
            doc_number = guarantee_return_obj.bankGuaranteeReturn.docNumber,
            date = guarantee_return_obj.bankGuaranteeReturn.returnDate,
            reason = guarantee_return_obj.bankGuaranteeReturn.returnReason,
            publish_dt = guarantee_return_obj.bankGuaranteeReturn.returnPublishDate
        )
    elif guarantee_return_obj.waiverNotice:
        guarantee_return = ZfcsContract2015BgReturn(
            kind = CntrBgReturnKind.WAIVER,
            reg_number = guarantee_return_obj.waiverNotice.regNumber,
            doc_number = guarantee_return_obj.waiverNotice.docNumber,
            date = guarantee_return_obj.waiverNotice.noticeDate,
            reason = guarantee_return_obj.waiverNotice.noticeReason,
            publish_dt = guarantee_return_obj.waiverNotice.noticePublishDate,
            notice_number = guarantee_return_obj.waiverNotice.noticeNumber
        )
    elif guarantee_return_obj.notPublishedOnEIS:
        guarantee_return = ZfcsContract2015BgReturn(
            kind = CntrBgReturnKind.NOT_PUBLISHED
        )
    else:
        pass

    return guarantee_return