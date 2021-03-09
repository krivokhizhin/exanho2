from .contract import *
from .aggregate import *

type_matching = {
    'cntrsuppliertype': 'VARCHAR(5)',
    'cntrparticipantkind': 'VARCHAR(2)',

    'cntrensuringkind': 'VARCHAR(2)',
    'cntrbgreturnkind':'VARCHAR(13)',

    'cntrensuringway': 'VARCHAR(2)',
    'cntrensuringtype':'VARCHAR(11)',
    'cntrensuringstatus':'VARCHAR(11)',

    'eistablename': 'VARCHAR(34)',
    'aggcontractstate': 'VARCHAR(12)'
}