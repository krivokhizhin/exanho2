import datetime

def check_none_return_min(dt:datetime=None):
    return dt if dt else datetime.datetime(datetime.MINYEAR, 1, 1)

def check_none_return_max(dt:datetime=None):
    return dt if dt else datetime.datetime(datetime.MAXYEAR, 12, 31)

def max_or_none(val1, val2):
    if val1 is None and val2 is None:
        return None

    return max([check_none_return_min(val1), check_none_return_min(val2)])

def min_or_none(val1, val2):
    if val1 is None and val2 is None:
        return None

    return min([check_none_return_max(val1), check_none_return_max(val2)])