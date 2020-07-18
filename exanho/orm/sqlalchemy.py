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

    def recreate(self):
        Base.metadata.create_all(self._engine)

    def dispose(self):
        self._engine.dispose()

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

def configure(url):
    engine = create_engine(url)
    Session.configure(bind=engine)

def validate(url):
    from sqlalchemy import inspect
    from exanho.orm.validators.sqlalchemy import Validator

    engine = create_engine(url)
    inspector = inspect(engine)
    
    validator = Validator(Base.metadata, inspector)
    validator.validate()

    return validator.is_valid, validator.error_messages, validator.warning_messages
    
def upgrade(self):
    pass

def sessional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()
        self, *_ = args
        self.session = session
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
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def has_domain(cls):
    cls.domain = None
    return cls