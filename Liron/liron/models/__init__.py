from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql://liron:liron@localhost:3306/liron', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

from liron.models.persons import *
from liron.models.seminar import *
