from contextlib import contextmanager
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker()


def configure(url):
    engine = create_engine(url)
    Session.configure(bind=engine)

def recreate(url):
    engine = create_engine(url)
    Base.metadata.create_all(engine)

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