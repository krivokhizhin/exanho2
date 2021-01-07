from .integration_types import zfcs_contract2015
from .integration_types import zfcs_contract_procedure2015

parsers = {
    '{http://zakupki.gov.ru/oos/export/1}contract' : zfcs_contract2015.parse,
    '{http://zakupki.gov.ru/oos/export/1}contractProcedure' : zfcs_contract_procedure2015.parse
}
