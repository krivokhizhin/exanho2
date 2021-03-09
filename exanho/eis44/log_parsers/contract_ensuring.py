import decimal
from sqlalchemy.orm.session import Session as OrmSession

from ..model.aggregate import CntrEnsuringWay, CntrEnsuringType, CntrEnsuringStatus, AggContract, AggContractEnsuring
from ..model.contract import CntrEnsuringKind, ZfcsContract2015Enforcement, CntrQualityGuaranteeInfo, ZfcsContract2015BgReturn

def handle_enforcement(session:OrmSession, contract:AggContract, enforcement_obj:ZfcsContract2015Enforcement, addition_only:bool):
    enforcement = None
    kind = CntrEnsuringType.MAINTENANCE if enforcement_obj.is_subsequent_maintenance else CntrEnsuringType.ENFORCEMENT

    if contract.ensuring:
        enforcement = [ensuring for ensuring in contract.ensuring if ensuring.kind == kind and ensuring.status == CntrEnsuringStatus.ACCEPT]
        if enforcement:
            enforcement = enforcement[0]
    else:
        contract.ensuring = list()

    way = CntrEnsuringWay.BG if enforcement_obj.kind == CntrEnsuringKind.BG else CntrEnsuringWay.CA
    amount = decimal.Decimal(enforcement_obj.amount) if enforcement_obj.amount else None
    if amount is None: amount = decimal.Decimal(enforcement_obj.amount_rur) if enforcement_obj.amount_rur else None

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
        if enforcement.amount is None: enforcement.amount = enforcement_obj.amount
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
            quality_guarantee = [ensuring for ensuring in contract.ensuring if ensuring.kind == CntrEnsuringType.QUALITY and ensuring.status == CntrEnsuringStatus.ACCEPT]
            if quality_guarantee:
                quality_guarantee = quality_guarantee[0]
        else:
            contract.ensuring = list()

        way = CntrEnsuringWay.BG if ensuring.kind == CntrEnsuringKind.BG else CntrEnsuringWay.CA
        amount = decimal.Decimal(ensuring.amount) if ensuring.amount else None
        if amount is None: amount = decimal.Decimal(ensuring.amount_rur) if ensuring.amount_rur else None

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
            if quality_guarantee.amount is None: quality_guarantee.amount = ensuring.amount
        else:
            quality_guarantee.way = way
            quality_guarantee.currency_code = ensuring.currency_code
            quality_guarantee.amount = ensuring.amount

    if qg_obj.guarantee_returns:
        pass

def handle_guarantee_return(session:OrmSession, contract:AggContract, qr_obj:ZfcsContract2015BgReturn, addition_only:bool):
    pass