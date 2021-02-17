from collections import namedtuple

ContractInfo = namedtuple('ContractInfo', 'reg_num state publish_dt subject price currency_code right_to_conclude supplier_number href start_date end_date')
ContractShortInfo = namedtuple('ContractShortInfo', 'reg_num state price currency start_date href')
SummaryContracts = namedtuple('SummaryContracts', 'state count sum currency first_start_date last_end_date')
