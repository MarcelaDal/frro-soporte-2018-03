from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()
from practico08.data.Models import *


class CapaDatos():
    def __init__(self):
        engine = create_engine('mysql+pymysql://spotifesta:spotifesta@localhost/spotifesta')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session
