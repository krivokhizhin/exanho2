from exanho.purchbot.vk.utils.message_manager import extract_inn_kpp_from_text

def run():
    print('{}: {}'.format('1234567890 987654321', extract_inn_kpp_from_text('1234567890 987654321')))
    print('{}: {}'.format('151303803109', extract_inn_kpp_from_text('151303803109')))
    print('{}: {}'.format('987654321', extract_inn_kpp_from_text('987654321')))
    print('{}: {}'.format('INN1234567890 KPP987654321', extract_inn_kpp_from_text('INN1234567890 KPP987654321')))
    print('{}: {}'.format('INN1234567890KPP987654321', extract_inn_kpp_from_text('INN1234567890KPP987654321')))
    print('{}: {}'.format('1234567890\n987654321', extract_inn_kpp_from_text('1234567890\n987654321')))
    print('{}: {}'.format('INN1234567890\nKPP987654321', extract_inn_kpp_from_text('INN1234567890\nKPP987654321')))
    print('{}: {}'.format('dshgdfkjs dfglj dhfkj 1234567890 dfsg  dfl k 987654321', extract_inn_kpp_from_text('dshgdfkjs dfglj dhfkj 1234567890 dfsg  dfl k 987654321')))
    print('{}: {}'.format('dshgdfkjs dfglj dhfkj 123456789012 dfsg  dfl k dfghdfhfggf', extract_inn_kpp_from_text('dshgdfkjs dfglj dhfkj 123456789012 dfsg  dfl k dfghdfhfggf')))
    print('{}: {}'.format('dshgdfkjs dfgl\nj dhfkj 1234567890\ndfsg  df\nl k 987654321', extract_inn_kpp_from_text('dshgdfkjs dfgl\nj dhfkj 1234567890\ndfsg  df\nl k 987654321')))
    print('{}: {}'.format('dshgdfkjs dfgl\nj dhfkj 4321997890\ndfsg  df\nl k 98765\n4321', extract_inn_kpp_from_text('dshgdfkjs dfgl\nj dhfkj 4321997890\ndfsg  df\nl k 98765\n4321')))
