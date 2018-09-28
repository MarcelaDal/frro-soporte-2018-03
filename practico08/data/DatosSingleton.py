from practico08.util import Singleton
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from practico08.data.models import Base


class DatosSingleton(metaclass=Singleton):
    engine = create_engine('mysql+pymysql://spotifesta:spotifesta@localhost/spotifesta')
    Base.metadata.bind = engine
    db_session = sessionmaker()
    db_session.bind = engine
    session = db_session()
