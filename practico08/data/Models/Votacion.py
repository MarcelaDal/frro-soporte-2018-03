from sqlalchemy import Integer, Column, ForeignKey, DateTime
from practico08.data import Base


class Votacion(Base):
        __tablename__ = 'votacion'

        id = Column(Integer, autoincrement=True, primary_key=True)
        tiempo_vida = Column(DateTime)
        id_sala = Column(Integer, ForeignKey('sala.id'))
