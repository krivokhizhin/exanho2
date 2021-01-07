from .integration_types import zfcs_contract2015

parsers = {
    '{http://zakupki.gov.ru/oos/export/1}contract' : zfcs_contract2015.parse
}
