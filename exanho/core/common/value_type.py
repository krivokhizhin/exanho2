import enum
import datetime
from typing import Tuple

DEFAULT_STRING_LENGTH = 100

class ValueType(enum.Enum):
    str = 1 # for DEFAULT_STRING_LENGTH
    int = 2
    datetime = 3
    zdatetime = 4

def convert_str_to_value(value_type:ValueType, value_str:str):

    if value_type == ValueType.str:
        return value_str

    if value_type == ValueType.int:
        return int(value_str)

    if value_type == ValueType.datetime:
        return datetime.datetime.fromisoformat(value_str)

    if value_type == ValueType.zdatetime:
        return datetime.datetime.fromisoformat(value_str)

    raise Exception(f'Unknown value type: {value_type}')

def convert_value_to_str(typed_value) -> Tuple(str, ValueType):

    if type(typed_value) == str:
        if len(typed_value) < DEFAULT_STRING_LENGTH+1:
            raise Exception(f'Strings longer than {DEFAULT_STRING_LENGTH} are not supported')
        return typed_value, ValueType.str

    if type(typed_value) == int:
        return str(typed_value), ValueType.int

    if type(typed_value) == datetime.datetime:
        if typed_value.utcoffset() is None:
            return typed_value.isoformat(), ValueType.datetime
        else:
            return typed_value.isoformat(), ValueType.zdatetime

    raise Exception(f'Unknown value type: {type(typed_value)}')