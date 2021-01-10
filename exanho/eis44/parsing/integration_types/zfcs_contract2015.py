from ...ds.contracts.fcsExport import zfcs_contract2015Type
from ...ds.contracts.IntegrationTypes import suppliers, zfcs_contract2015SupplierType, legalEntityRF, legalEntityForeignState, individualPersonRF, individualPersonForeignState, individualPersonRFisCulture, individualPersonForeignStateisCulture

from exanho.core.common import Error
from ...model.contract import *

NOT_PUBLISHED_VALUE = '*'

def parse(session, contract_obj:zfcs_contract2015Type, update=True, **kwargs):
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
            execution_start_date = contract_obj.executionPeriod.startDate,
            execution_end_date = contract_obj.executionPeriod.endDate,

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
        contract.execution_start_date = contract_obj.executionPeriod.startDate
        contract.execution_end_date = contract_obj.executionPeriod.endDate

        contract.energy_service_info = contract_obj.energyServiceContractInfo
        contract.href = contract_obj.href

        contract.current_stage = contract_obj.currentContractStage
        contract.okpd2okved2 = contract_obj.okpd2okved2
        contract.is_invalid = contract_obj.isInvalid
        contract.scheme_version = contract_obj.schemeVersion

    if contract_obj.priceInfo.rightToConcludeContractPriceInfo is None:
        contract.price = contract_obj.priceInfo.price
        contract.price_type = contract_obj.priceInfo.priceType
        contract.price_formula = contract_obj.priceInfo.priceFormula
        contract.price_formula_specified = contract_obj.priceInfo.maxPriceAndPriceFormulaSpecified
        contract.currency_code = contract_obj.priceInfo.currency.code
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

def fill_suppliers(session, owner:ZfcsContract2015, suppliers_obj:suppliers):
    owner.suppliers = []
    if suppliers_obj is None:
        return

    for supplier_obj in suppliers_obj.supplier:
        supplier = get_supplier(session, supplier_obj)
        if supplier:
            owner.suppliers.append(supplier)

def get_supplier(session, supplier_obj:zfcs_contract2015SupplierType):
    supplier = None
    if supplier_obj is None:
        return supplier

    if supplier_obj.legalEntityRF:
        supplier = get_legal_entity_rf(session, supplier_obj.legalEntityRF)
    elif supplier_obj.individualPersonRF:
        pass
    elif supplier_obj.legalEntityForeignState:
        pass
    elif supplier_obj.individualPersonForeignState:
        pass
    elif supplier_obj.individualPersonRFisCulture:
        pass
    elif supplier_obj.individualPersonForeignStateisCulture:
        pass
    elif supplier_obj.notPublishedOnEIS:
        supplier = get_not_published_on_eis(session, supplier_obj.notPublishedOnEIS)
    else:
        raise Error(f'unknown zfcs_contract2015SupplierType')

    # session.add(supplier)
    return supplier

def get_legal_entity_rf(session, supplier_obj:legalEntityRF):
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.LERF
    )

    supplier.status = supplier_obj.status

    inn = supplier_obj.INN
    kpp = supplier_obj.KPP
    participant = get_participant(session, CntrParticipantKind.RF, inn, kpp)

def get_individual_person_rf(session, supplier_obj:individualPersonRF):
    pass

def get_legal_entity_fs(session, supplier_obj:legalEntityForeignState):
    pass

def get_individual_person_fs(session, supplier_obj:individualPersonForeignState):
    pass

def get_individual_culture_person_rf(session, supplier_obj:individualPersonRFisCulture):
    pass

def get_individual_culture_person_fs(session, supplier_obj:individualPersonForeignStateisCulture):
    pass

def get_not_published_on_eis(session, supplier_obj:bool):
    supplier = ZfcsContract2015Supplier(
        type = CntrSupplierType.NPEIS
    )
    supplier.participant = get_participant(session, CntrParticipantKind.RF, NOT_PUBLISHED_VALUE, NOT_PUBLISHED_VALUE)
    return supplier

def get_participant(session, kind:CntrParticipantKind, inn:str, kpp:str):
    participant = session.query(CntrParticipant).filter(CntrParticipant.inn == inn, CntrParticipant.kpp == kpp).one_or_none()
    if participant is None:
        participant = CntrParticipant(
            kind = kind,
            inn = inn,
            kpp = kpp
        )
        session.add(participant)

    return participant