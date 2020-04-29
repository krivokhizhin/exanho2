import datetime

def max_or_none(val1, val2):
    if val1 is None and val2 is None:
        return None

    if val1 is None and (type(val2) in [datetime.datetime, datetime.date, datetime.time]):
        val1 = type(val2).min

    if val2 is None and (type(val1) in [datetime.datetime, datetime.date, datetime.time]):
        val2 = type(val1).min

    return max([val1, val2])

def min_or_none(val1, val2):
    if val1 is None and val2 is None:
        return None

    if val1 is None and (type(val2) in [datetime.datetime, datetime.date, datetime.time]):
        val1 = type(val2).max

    if val2 is None and (type(val1) in [datetime.datetime, datetime.date, datetime.time]):
        val2 = type(val1).max

    return min([val1, val2])