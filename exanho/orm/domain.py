import types

from contextlib import contextmanager
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

class Domain:

    def __init__(self, url):
        self._engine = create_engine(url)
        self._session = scoped_session(sessionmaker(bind=self._engine))

    def dispose(self):
        self._engine.dispose()

    def validate(self, model_modules):
        self.dispose()
        self._load_models(model_modules)

        from sqlalchemy import inspect
        from exanho.orm.validator import Validator

        inspector = inspect(self._engine)
        
        validator = Validator(Base.metadata, inspector)
        validator.validate()

        return validator.is_valid, validator.error_messages, validator.warning_messages

    @property
    def Session(self):
        return self._session()

    def sessional(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session = self.Session
            result = None
            try:
                result = func(*args, **kwargs)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
            return result
        return wrapper

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.Session
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

Session = sessionmaker()

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
    engine = create_engine(url)
    Session.configure(bind=engine)

def recreate(url:str, models:list):
    load_models(models)

    engine = create_engine(url)
    Base.metadata.create_all(engine)

def validate(url:str, models:list):
    load_models(models)

    from sqlalchemy import inspect
    from exanho.orm.validator import Validator

    engine = create_engine(url)
    inspector = inspect(engine)
    
    validator = Validator(Base.metadata, inspector)
    validator.validate()

    return validator.is_valid, validator.error_messages, validator.warning_messages
    
def upgrade(self):
    pass

# def sessional(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         session = Session()
#         self, *_ = args
#         self.session = session
#         result = None
#         try:
#             result = func(*args, **kwargs)
#             session.commit()
#         except:
#             session.rollback()
#             raise
#         finally:
#             session.close()
#         return result
#     return wrapper

# @contextmanager
# def session_scope():
#     """Provide a transactional scope around a series of operations."""
#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()

@contextmanager
def session_scope(domain):
    """Provide a transactional scope around a series of operations."""
    session = domain.Session
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

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
