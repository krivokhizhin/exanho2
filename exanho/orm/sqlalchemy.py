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

def validate(url):
    from sqlalchemy import inspect

    engine = create_engine(url)
    insp = inspect(engine)

    return validator(Base.metadata, insp)

def validator(*args):
    return False
    
def upgrade(self):
    pass