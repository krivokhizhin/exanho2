from .reference import nsi_okato
from .reference import nsi_okv
from .reference import nsi_okved
from .reference import nsi_okved2

parsers = {
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkato' : nsi_okato.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkv' : nsi_okv.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkved' : nsi_okved.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkved2' : nsi_okved2.parse
}
