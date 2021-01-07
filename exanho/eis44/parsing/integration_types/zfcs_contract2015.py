from ...ds.export_types import zfcs_contract2015Type
from ...model.contract import *

def parse(session, contract_obj:zfcs_contract2015Type, update=True, **kwargs):
    doc_id = contract_obj.id
    external_id = contract_obj.externalId

    if session.query(ZfcsContract2015).filter(ZfcsContract2015.doc_id == doc_id, ZfcsContract2015.external_id == external_id).count() > 0:
        return

    new_contract = ZfcsContract2015(
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
    session.add(new_contract)

    if contract_obj.priceInfo.rightToConcludeContractPriceInfo is None:
        new_contract.price = contract_obj.priceInfo.price
        new_contract.price_type = contract_obj.priceInfo.priceType
        new_contract.price_formula = contract_obj.priceInfo.priceFormula
        new_contract.price_formula_specified = contract_obj.priceInfo.maxPriceAndPriceFormulaSpecified
        new_contract.currency_code = contract_obj.priceInfo.currency.code
        new_contract.currency_rate = contract_obj.priceInfo.currencyRate.rate
        new_contract.currency_raiting = contract_obj.priceInfo.currencyRate.raiting
        new_contract.price_rur = contract_obj.priceInfo.priceRUR
        new_contract.price_vat = contract_obj.priceInfo.priceVAT
        new_contract.price_vat_rur = contract_obj.priceInfo.priceVATRUR
        new_contract.reduced_by_taxes = contract_obj.priceInfo.amountsReducedByTaxes
    else:
        new_contract.right_to_conclude = True

    if contract_obj.advancePaymentSum:
        new_contract.advance_payment_percents = contract_obj.advancePaymentSum.sumInPercents
        new_contract.advance_payment_value = contract_obj.advancePaymentSum.priceValue
        new_contract.advance_payment_value_rur = contract_obj.advancePaymentSum.priceValueRUR

    if contract_obj.subContractorsSum:
        new_contract.sub_contractors_percents = contract_obj.subContractorsSum.sumInPercents
        new_contract.sub_contractors_value_rur = contract_obj.subContractorsSum.priceValueRUR