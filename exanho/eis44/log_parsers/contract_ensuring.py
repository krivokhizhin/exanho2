import decimal
from sqlalchemy.orm.session import Session as OrmSession

from ..model.aggregate import CntrEnsuringWay, CntrEnsuringType, CntrEnsuringStatus, AggContract, AggContractEnsuring
from ..model.contract import CntrEnsuringKind, ZfcsContract2015Enforcement, CntrQualityGuaranteeInfo, CntrBgReturnKind, ZfcsContract2015BgReturn

def handle_enforcement(session:OrmSession, contract:AggContract, enforcement_obj:ZfcsContract2015Enforcement, addition_only:bool):
    enforcement = None
    kind = CntrEnsuringType.MAINTENANCE if enforcement_obj.is_subsequent_maintenance else CntrEnsuringType.ENFORCEMENT

    if contract.ensuring:
        enforcement = [ensuring_ for ensuring_ in contract.ensuring if ensuring_.kind == kind and ensuring_.status == CntrEnsuringStatus.ACCEPT]
        if enforcement:
            enforcement = enforcement[0]
    else:
        contract.ensuring = list()

    way = CntrEnsuringWay.BG if enforcement_obj.kind == CntrEnsuringKind.BG else CntrEnsuringWay.CA
    amount = decimal.Decimal(enforcement_obj.amount) if enforcement_obj.amount else None
    if amount is None or amount == 0: amount = decimal.Decimal(enforcement_obj.amount_rur) if enforcement_obj.amount_rur else amount

    if not enforcement:
        enforcement = AggContractEnsuring(
            way = way,
            kind = kind,
            status = CntrEnsuringStatus.ACCEPT,
            currency_code = enforcement_obj.currency_code,
            amount = amount
        )
        contract.ensuring.append(enforcement)
        session.add(enforcement)
    elif addition_only:
        if enforcement.way is None: enforcement.way = way
        if enforcement.currency_code is None: enforcement.currency_code = enforcement_obj.currency_code
        if enforcement.amount is None or enforcement.amount == 0: enforcement.amount = enforcement_obj.amount
    else:
        enforcement.way = way
        enforcement.currency_code = enforcement_obj.currency_code
        enforcement.amount = enforcement_obj.amount

def handle_quality_guarantee(session:OrmSession, contract:AggContract, qg_obj:CntrQualityGuaranteeInfo, addition_only:bool):
    if not qg_obj.ensuring_way and not qg_obj.guarantee_returns:
        return

    if qg_obj.ensuring_way:
        ensuring:ZfcsContract2015Enforcement = qg_obj.ensuring_way
        quality_guarantee = None

        if contract.ensuring:
            quality_guarantee = [ensuring_ for ensuring_ in contract.ensuring if ensuring_.kind == CntrEnsuringType.QUALITY and ensuring_.status == CntrEnsuringStatus.ACCEPT]
            if quality_guarantee:
                quality_guarantee = quality_guarantee[0]
        else:
            contract.ensuring = list()

        way = CntrEnsuringWay.BG if ensuring.kind == CntrEnsuringKind.BG else CntrEnsuringWay.CA
        amount = decimal.Decimal(ensuring.amount) if ensuring.amount else None
        if amount is None or amount == 0: amount = decimal.Decimal(ensuring.amount_rur) if ensuring.amount_rur else amount

        if not quality_guarantee:
            quality_guarantee = AggContractEnsuring(
                way = way,
                kind = CntrEnsuringType.QUALITY,
                status = CntrEnsuringStatus.ACCEPT,
                currency_code = ensuring.currency_code,
                amount = amount
            )
            contract.ensuring.append(quality_guarantee)
            session.add(quality_guarantee)
        elif addition_only:
            if quality_guarantee.way is None: quality_guarantee.way = way
            if quality_guarantee.currency_code is None: quality_guarantee.currency_code = ensuring.currency_code
            if quality_guarantee.amount is None or quality_guarantee.amount == 0: quality_guarantee.amount = ensuring.amount
        else:
            quality_guarantee.way = way
            quality_guarantee.currency_code = ensuring.currency_code
            quality_guarantee.amount = ensuring.amount

    if qg_obj.guarantee_returns:
        pass

def handle_guarantee_return(session:OrmSession, contract:AggContract, qr_obj:ZfcsContract2015BgReturn, addition_only:bool):
    bg_status = None
    if qr_obj.kind == CntrBgReturnKind.RETURN:
        bg_status = CntrEnsuringStatus.RETURN
    elif qr_obj.kind == CntrBgReturnKind.WAIVER:
        bg_status = CntrEnsuringStatus.WAIVER
    elif qr_obj.kind == CntrBgReturnKind.NOT_PUBLISHED:
        bg_status = CntrEnsuringStatus.RETURN_OR_WAIVER
    else:
        return

    if qr_obj.contract_id:
        enforcement = None

        if contract.ensuring:
            enforcement = [ensuring_ for ensuring_ in contract.ensuring if ensuring_.way == CntrEnsuringWay.BG and ensuring_.kind == CntrEnsuringType.ENFORCEMENT]
            if enforcement:
                enforcement = enforcement[0]
        else:
            contract.ensuring = list()

        if not enforcement:
            enforcement = AggContractEnsuring(
                way = CntrEnsuringWay.BG,
                kind = CntrEnsuringType.ENFORCEMENT,
                status = bg_status
            )
            contract.ensuring.append(enforcement)
            session.add(enforcement)
        elif addition_only:
            if enforcement.status is None: enforcement.status = bg_status
        else:
            enforcement.status = bg_status


    elif qr_obj.quality_guarantee_id:
        quality_guarantee = None
            
        if contract.ensuring:
            quality_guarantee = [ensuring_ for ensuring_ in contract.ensuring if ensuring_.way == CntrEnsuringWay.BG and ensuring_.kind == CntrEnsuringType.QUALITY]
            if quality_guarantee:
                quality_guarantee = quality_guarantee[0]
        else:
            contract.ensuring = list()
         
        if not quality_guarantee:
            quality_guarantee = AggContractEnsuring(
                way = CntrEnsuringWay.BG,
                kind = CntrEnsuringType.QUALITY,
                status = bg_status
            )
            contract.ensuring.append(quality_guarantee)
            session.add(quality_guarantee)
        elif addition_only:
            if quality_guarantee.status is None: quality_guarantee.status = bg_status
        else:
            quality_guarantee.status = bg_status
   
    else:
        return