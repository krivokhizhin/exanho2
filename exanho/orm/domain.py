import types

from contextlib import contextmanager
from functools import wraps

Base = None

class Domain:

    def __init__(self, url):
        self._engine = None
        self._session = None

    def dispose(self):
        pass

    def validate(self, model_modules):
        return True, [], []

    @property
    def Session(self):
        return None

    def sessional(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except:
                raise
            return result
        return wrapper

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session
        try:
            yield session
        except:
            raise

Session = None

def load_models(model_modules):
    if not isinstance(model_modules, list):
        raise TypeError(model_modules)

    from .validator import type_matching

    from importlib import import_module
    for model_module in model_modules:
        mod = import_module(model_module)
        if hasattr(mod, 'type_matching'):
            type_matching.update(mod.type_matching)

def configure(url):
    engine = None

def recreate(url:str, models:list):
    load_models(models)

    engine = None

def validate(url:str, models:list):
    return True, [], []
    
def upgrade(self):
    pass

@contextmanager
def session_scope(domain):
    """Provide a transactional scope around a series of operations."""
    session = domain.Session
    try:
        yield session
    except:
        raise

class Sessional:

    domain = None

    def __init__(self, func):
        wraps(func)(self)
        self.session = None

    def __call__(self, *args, **kwargs):
        with session_scope(self.__class__.domain) as session:
            self.session = session
            return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
