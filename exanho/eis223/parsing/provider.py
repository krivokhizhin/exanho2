from .reference import nsi_okato
from .reference import nsi_okdp
from .reference import nsi_okei
from .reference import nsi_okfs
from .reference import nsi_okogu
from .reference import nsi_okopf
from .reference import nsi_okpd2
from .reference import nsi_oktmo
from .reference import nsi_okv
from .reference import nsi_okved
from .reference import nsi_okved2

parsers = {
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkato' : nsi_okato.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkdp' : nsi_okdp.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkei' : nsi_okei.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkfs' : nsi_okfs.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkogu' : nsi_okogu.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkopf' : nsi_okopf.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkpd2' : nsi_okpd2.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOktmo' : nsi_oktmo.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkv' : nsi_okv.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkved' : nsi_okved.parse,
    '{http://zakupki.gov.ru/223fz/reference/1}nsiOkved2' : nsi_okved2.parse
}
