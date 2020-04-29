import datetime

def check_none_return_min(dt:datetime=None):
    return dt if dt else datetime.datetime(datetime.MINYEAR, 1, 1)

def check_none_return_max(dt:datetime=None):
    return dt if dt else datetime.datetime(datetime.MAXYEAR, 12, 31)