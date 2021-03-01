from collections import namedtuple

ParticipantInfo = namedtuple('ParticipantInfo', 'id name inn kpp')

ContractInfo = namedtuple('ContractInfo', 'reg_num state publish_dt subject price currency_code right_to_conclude supplier_number href start_date end_date')
ContractShortInfo = namedtuple('ContractShortInfo', 'reg_num state price currency start_date href')
SummaryContracts = namedtuple('SummaryContracts', 'state count sum currency first_start_date last_end_date')

ParticipantCurrentActivityInfo = namedtuple('ParticipantCurrentActivityInfo',[
    'participant_id',
    'cntr_count',
    'cntr_rur_sum',
    'cntr_currencies',
    'cntr_cur_count',
    'cntr_cur_sum',
    'cntr_right_to_conclude_count',
    'cntr_first_start_date',
    'cntr_last_end_date'
])

ParticipantExperienceInfo = namedtuple('ParticipantExperienceInfo',[
    'participant_id',
    'cntr_ec_count',
    'cntr_ec_rur_sum',
    'cntr_ec_cur_count',
    'cntr_et_count',
    'cntr_et_rur_sum',
    'cntr_et_cur_count',
    'cntr_in_count',
    'cntr_in_rur_sum',
    'cntr_in_cur_count',
    'cntr_first_start_date',
    'cntr_last_end_date'
])