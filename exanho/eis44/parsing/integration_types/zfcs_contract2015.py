from sqlalchemy.orm.session import Session as OrmSession

from ...ds.contracts.fcsExport import zfcs_contract2015Type
from ...ds.contracts.IntegrationTypes import suppliers, zfcs_contract2015SupplierType, corr_supplierLegalEntityRF, corr_supplierLegalEntityForeignState, corr_supplierIndividualPersonRF, corr_supplierIndividualPersonForeignState, individualPersonRFisCulture, individualPersonForeignStateisCulture
from ...ds.contracts.IntegrationTypes import zfcs_contract2015EnforcementType, qualityGuaranteeInfo, zfcs_contract2015BankGuaranteeReturnType, bankGuarantee, cashAccount, guaranteeReturn

from exanho.core.common import Error
from ...model.contract import *

IP_FORM = 'ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНИМАТЕЛЬ'
IP_SHORT_FORM = 'ИП'

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

    fill_suppliers(contract, contract_obj.suppliers)

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


def fill_suppliers(owner:ZfcsContract2015, suppliers_obj:suppliers):
    owner.suppliers = []
    if suppliers_obj is None:
        return

    order = 0
    for supplier_obj in suppliers_obj.supplier:
        supplier = get_supplier(supplier_obj)
        if supplier:
            order += 1
            supplier.order = order
            owner.suppliers.append(supplier)

def get_supplier(supplier_obj:zfcs_contract2015SupplierType) -> ZfcsContract2015Supplier:
    supplier = None
    if supplier_obj is None:
        return supplier

    if supplier_obj.legalEntityRF:
        supplier = get_legal_entity_rf(supplier_obj.legalEntityRF)
    elif supplier_obj.individualPersonRF:
        supplier = get_individual_person_rf(supplier_obj.individualPersonRF)
    elif supplier_obj.legalEntityForeignState:
        supplier = get_legal_entity_fs(supplier_obj.legalEntityForeignState)
    elif supplier_obj.individualPersonForeignState:
        supplier = get_individual_person_fs(supplier_obj.individualPersonForeignState)
    elif supplier_obj.individualPersonRFisCulture:
        supplier = get_individual_culture_person_rf(supplier_obj.individualPersonRFisCulture)
    elif supplier_obj.individualPersonForeignStateisCulture:
        supplier = get_individual_culture_person_fs(supplier_obj.individualPersonForeignStateisCulture)
    elif supplier_obj.notPublishedOnEIS:
        supplier = get_not_published_on_eis(supplier_obj.notPublishedOnEIS)
    else:
        raise Error(f'unknown zfcs_contract2015SupplierType')

    return supplier

def get_legal_entity_rf(supplier_obj:corr_supplierLegalEntityRF) -> ZfcsContract2015Supplier:

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.LERF,

        inn = supplier_obj.INN,
        kpp = supplier_obj.KPP,

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

    if supplier_obj.legalForm:
        supplier.okopf_code = supplier_obj.legalForm.code
        supplier.okopf_name = supplier_obj.legalForm.singularName

    if supplier_obj.fullName: supplier.full_name = supplier_obj.fullName
    if supplier_obj.shortName: supplier.short_name = supplier_obj.shortName
    if supplier_obj.firmName: supplier.firm_name = supplier_obj.firmName

    if supplier_obj.OKPO: supplier.okpo = supplier_obj.OKPO
    if supplier_obj.registrationDate: supplier.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        supplier.oktmo_code = supplier_obj.OKTMO.code
        supplier.oktmo_name = supplier_obj.OKTMO.name

    if supplier_obj.contactInfo:
        supplier.contact_last_name = supplier_obj.contactInfo.lastName
        supplier.contact_first_name = supplier_obj.contactInfo.firstName
        supplier.contact_middle_name = supplier_obj.contactInfo.middleName

    return supplier

def get_individual_person_rf(supplier_obj:corr_supplierIndividualPersonRF) -> ZfcsContract2015Supplier:

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPRF,

        inn = supplier_obj.INN,

        status = supplier_obj.status,
        ersmsp_inclusion_date = supplier_obj.ERSMSPInclusionDate,
        personal_account = supplier_obj.personalAccount,
        address = supplier_obj.address,
        mailing_adress = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailingAdress,
        mail_facility_name = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailFacilityName,
        post_box_number = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.postBoxNumber,
        post_address = supplier_obj.postAddress,
        
        contact_last_name = supplier_obj.lastName if supplier_obj.lastName else '',
        contact_first_name = supplier_obj.firstName if supplier_obj.firstName else '',
        contact_middle_name = supplier_obj.middleName if supplier_obj.middleName else '',
        contact_email = supplier_obj.contactEMail,
        contact_phone = supplier_obj.contactPhone,

        is_ip = supplier_obj.isIP,
        is_culture = supplier_obj.isCulture
    )
    
    supplier.full_name = form_full_name_by_fio(supplier.contact_last_name, supplier.contact_first_name, supplier.contact_middle_name)
    supplier.short_name = form_short_name_by_fio(supplier.contact_last_name, supplier.contact_first_name, supplier.contact_middle_name)

    if supplier_obj.isIP:
        supplier.full_name = '{0} {1}'.format(IP_FORM, supplier.full_name)
        supplier.short_name = '{0} {1}'.format(IP_SHORT_FORM, supplier.short_name)

    if supplier_obj.registrationDate: supplier.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        supplier.oktmo_code = supplier_obj.OKTMO.code
        supplier.oktmo_name = supplier_obj.OKTMO.name

    return supplier

def get_legal_entity_fs(supplier_obj:corr_supplierLegalEntityForeignState) -> ZfcsContract2015Supplier:

    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.LEFS,

        inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else None,
        kpp = supplier_obj.registerInRFTaxBodies.KPP if supplier_obj.registerInRFTaxBodies else None,

        full_name = supplier_obj.fullName,
        short_name = supplier_obj.shortName,
        firm_name = supplier_obj.firmName,
        full_name_lat = supplier_obj.fullNameLat,
        tax_payer_code = supplier_obj.taxPayerCode,

        status = supplier_obj.status,
        personal_account = supplier_obj.personalAccount
    )

    if supplier_obj.registerInRFTaxBodies and supplier_obj.registerInRFTaxBodies.registrationDate: supplier.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate

    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            supplier.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            supplier.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: supplier.fs_address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: supplier.fs_post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: supplier.fs_email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: supplier.fs_phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            supplier.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            supplier.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.mailingAdress
        supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.mailFacilityName
        supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAdressInfo is None else supplier_obj.placeOfStayInRF.postAdressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone

    return supplier

def get_individual_person_fs(supplier_obj:corr_supplierIndividualPersonForeignState) -> ZfcsContract2015Supplier:
    
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPFS,

        inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else None,

        personal_account = supplier_obj.personalAccount,

        contact_last_name = supplier_obj.lastName if supplier_obj.lastName else '',
        contact_first_name = supplier_obj.firstName if supplier_obj.firstName else '',
        contact_middle_name = supplier_obj.middleName if supplier_obj.middleName else '',

        is_culture = supplier_obj.isCulture
    )

    supplier.full_name = form_full_name_by_fio(supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)
    supplier.short_name = form_short_name_by_fio(supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)

    supplier.full_name_lat = form_full_name_by_fio(supplier_obj.lastNameLat, supplier_obj.firstNameLat, supplier_obj.middleNameLat)
    supplier.tax_payer_code = supplier_obj.taxPayerCode

    if supplier_obj.registerInRFTaxBodies:
        if supplier_obj.registerInRFTaxBodies.registrationDate: supplier.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate
        # if supplier_obj.registerInRFTaxBodies.status: supplier.status = supplier_obj.registerInRFTaxBodies.status
        # if supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate: supplier.ersmsp_inclusion_date = supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate
        # if supplier_obj.registerInRFTaxBodies.isIP: supplier.is_ip = supplier_obj.registerInRFTaxBodies.isIP
    
    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            supplier.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            supplier.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: supplier.fs_address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: supplier.fs_post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: supplier.fs_email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: supplier.fs_phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            supplier.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            supplier.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        # supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailingAdress
        # supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailFacilityName
        # supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone
    
    return supplier

def get_individual_culture_person_rf(supplier_obj:individualPersonRFisCulture) -> ZfcsContract2015Supplier:
    
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPRFC,

        inn = supplier_obj.INN,

        status = supplier_obj.status,
        ersmsp_inclusion_date = supplier_obj.ERSMSPInclusionDate,
        personal_account = supplier_obj.personalAccount,
        address = supplier_obj.address,
        mailing_adress = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailingAdress,
        mail_facility_name = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.mailFacilityName,
        post_box_number = None if supplier_obj.postAddressInfo is None else supplier_obj.postAddressInfo.postBoxNumber,
        post_address = supplier_obj.postAddress,
        
        contact_last_name = supplier_obj.lastName if supplier_obj.lastName else '',
        contact_first_name = supplier_obj.firstName if supplier_obj.firstName else '',
        contact_middle_name = supplier_obj.middleName if supplier_obj.middleName else '',
        contact_email = supplier_obj.contactEMail,
        contact_phone = supplier_obj.contactPhone,

        is_ip = supplier_obj.isIP
    )

    supplier.full_name = form_full_name_by_fio(supplier.contact_last_name, supplier.contact_first_name, supplier.contact_middle_name)
    supplier.short_name = form_short_name_by_fio(supplier.contact_last_name, supplier.contact_first_name, supplier.contact_middle_name)

    if supplier_obj.isIP:
        supplier.full_name = '{0} {1}'.format(IP_FORM, supplier.full_name)
        supplier.short_name = '{0} {1}'.format(IP_SHORT_FORM, supplier.short_name)

    if supplier_obj.registrationDate: supplier.registration_date = supplier_obj.registrationDate
    if supplier_obj.OKTMO:
        supplier.oktmo_code = supplier_obj.OKTMO.code
        supplier.oktmo_name = supplier_obj.OKTMO.name

    return supplier

def get_individual_culture_person_fs(supplier_obj:individualPersonForeignStateisCulture) -> ZfcsContract2015Supplier:
    
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.IPFSC,
        inn = supplier_obj.registerInRFTaxBodies.INN if supplier_obj.registerInRFTaxBodies else None,

        contact_last_name = supplier_obj.lastName if supplier_obj.lastName else '',
        contact_first_name = supplier_obj.firstName if supplier_obj.firstName else '',
        contact_middle_name = supplier_obj.middleName if supplier_obj.middleName else '',

        personal_account = supplier_obj.personalAccount
    )

    supplier.full_name = form_full_name_by_fio(supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)
    supplier.short_name = form_short_name_by_fio(supplier_obj.lastName, supplier_obj.firstName, supplier_obj.middleName)

    supplier.full_name_lat = form_full_name_by_fio(supplier_obj.lastNameLat, supplier_obj.firstNameLat, supplier_obj.middleNameLat)
    supplier.tax_payer_code = supplier_obj.taxPayerCode

    if supplier_obj.registerInRFTaxBodies:
        if supplier_obj.registerInRFTaxBodies.registrationDate: supplier.registration_date = supplier_obj.registerInRFTaxBodies.registrationDate
        # if supplier_obj.registerInRFTaxBodies.status: supplier.status = supplier_obj.registerInRFTaxBodies.status
        # if supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate: supplier.ersmsp_inclusion_date = supplier_obj.registerInRFTaxBodies.ERSMSPInclusionDate
        # if supplier_obj.registerInRFTaxBodies.isIP: supplier.is_ip = supplier_obj.registerInRFTaxBodies.isIP
    
    if supplier_obj.placeOfStayInRegCountry:
        if supplier_obj.placeOfStayInRegCountry.country:
            supplier.country_code = supplier_obj.placeOfStayInRegCountry.country.countryCode
            supplier.country_full_name = supplier_obj.placeOfStayInRegCountry.country.countryFullName

        if supplier_obj.placeOfStayInRegCountry.address: supplier.fs_address = supplier_obj.placeOfStayInRegCountry.address
        if supplier_obj.placeOfStayInRegCountry.postAddress: supplier.fs_post_address = supplier_obj.placeOfStayInRegCountry.postAddress
        if supplier_obj.placeOfStayInRegCountry.contactEMail: supplier.fs_email = supplier_obj.placeOfStayInRegCountry.contactEMail
        if supplier_obj.placeOfStayInRegCountry.contactPhone: supplier.fs_phone = supplier_obj.placeOfStayInRegCountry.contactPhone


    if supplier_obj.placeOfStayInRF:
        if supplier_obj.placeOfStayInRF.OKTMO:
            supplier.oktmo_code = supplier_obj.placeOfStayInRF.OKTMO.code
            supplier.oktmo_name = supplier_obj.placeOfStayInRF.OKTMO.name

        supplier.address = supplier_obj.placeOfStayInRF.address
        # supplier.mailing_adress = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailingAdress
        # supplier.mail_facility_name = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.mailFacilityName
        # supplier.post_box_number = None if supplier_obj.placeOfStayInRF.postAddressInfo is None else supplier_obj.placeOfStayInRF.postAddressInfo.postBoxNumber
        supplier.post_address = supplier_obj.placeOfStayInRF.postAddress

        supplier.contact_email = supplier_obj.placeOfStayInRF.contactEMail
        supplier.contact_phone = supplier_obj.placeOfStayInRF.contactPhone

    return supplier

def get_not_published_on_eis(supplier_obj:bool) -> ZfcsContract2015Supplier:
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.NPEIS
    )
    return supplier

def form_full_name_by_fio(last_name:str, first_name:str, middle_name:str) -> str:
    if last_name is None and first_name is None and middle_name is None:
        return None

    last_name = last_name.upper() if last_name else ''
    first_name = first_name.upper() if first_name else ''
    middle_name = middle_name.upper() if middle_name else ''

    return f'{last_name} {first_name} {middle_name}'.strip()

def form_short_name_by_fio(last_name:str, first_name:str, middle_name:str) -> str:
    if last_name is None and first_name is None and middle_name is None:
        return None

    last_name = last_name.upper() if last_name else ''
    first_name = f'{first_name.upper()[0]}.' if first_name else ''
    middle_name = f'{middle_name.upper()[0]}.' if middle_name else ''

    return f'{last_name} {first_name} {middle_name}'.strip()

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