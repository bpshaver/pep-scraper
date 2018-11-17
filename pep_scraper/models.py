import settings

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def db_connect():
    """
    Unpacks the db setting from the settings module into a 
    utility that creates a URL string for SQLalchemy. Pretty cool!
    """

    return create_engine(URL(**settings.DATABASE))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Pepscrape(DeclarativeBase):
    """
    Pep scrape SQL table
    """
    __tablename__="pepinfo"

    ID = Column(Integer, primary_key=True)
    short_typ = Column('short_type', String)
    short_num = Column('short_num')
    short_tit = Column('short_tit', String)
    short_aut = Column('short_aut', String)
    url = Column('url', String)
    PEP = Column('PEP', nullable=True)
    Title = Column('Title', String, nullable=True)
    Author = Column('Author', String, nullable=True)
    Status = Column('Status', String, nullable=True)
    Type = Column('Type', String, nullable=True)
    Created = Column('Created', String, nullable=True)
    Post_History = Column('Post_History', String, nullable=True)
    Python_Version = Column('Python_Version', String, nullable=True)

