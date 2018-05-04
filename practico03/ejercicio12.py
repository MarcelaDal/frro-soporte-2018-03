from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,ForeignKey,Integer,String,Date
from sqlalchemy.orm import  sessionmaker

Base = declarative_base()


class Persona(Base):
    __tablename__ = 'Persona'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    fecha_nacimiento = Column(Date)
    dni = Column(String(13))
    altura = Column(Integer)


engine = create_engine('mysql+pymysql://root@localhost/tp3')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def alta():
    p = Persona()
    session.add(p)
    session.commit()


def list():
    lp = session.quert(Persona).all()
    for p in lp:
        print('Persona: ', p.id, p.nombre)


def baja():
    ide = "H"
    p = session.query.filter_by(id=ide).first()
    session.remove(p)


op = input("Ingresar numero:")
while op is not 0:
    if op == 1:
        alta()
    if op == 2:
        list()
    if op == 3:
        baja()