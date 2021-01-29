import pickle
from functools import wraps

def serialize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return pickle.dumps(result)
    return wrapper

def deserialize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return pickle.loads(result)
    return wrapper
