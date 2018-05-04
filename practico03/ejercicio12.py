from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,ForeignKey,Integer,String,Date
from sqlalchemy.orm import  sessionmaker
from datetime import date

Base = declarative_base()


class Persona(Base):
    __tablename__ = 'personas'
    idPersona = Column(Integer, primary_key=True)
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
    p.nombre = input("Ingresa el nombre")
    fecha= input('Ingresa una fecha en formato YYYY-MM-DD')
    year, month, day = map(int, fecha.split('-'))
    p.fecha_nacimiento=date(year,month,day)
    p.dni = input("Ingresa dni:")
    p.altura = int(input("Ingresa una altura en cm"))

    session.add(p)
    session.commit()


def list():
    lp = session.query(Persona).all()
    for p in lp:
        print('Persona: ', p.idPersona, p.nombre)


def baja():
    id = input("Ingrsa el id de la persona a remover:")
    p = session.query(Persona).filter(Persona.idPersona==id).first()
    session.delete(p)


op = int(input("Ingresar numero:"))
while op is not 0:
    if op == 1:
        alta()
    if op == 2:
        list()
    if op == 3:
        baja()
    op = int(input("Ingresar numero:"))