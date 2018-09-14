from sqlalchemy import Integer,String,Column, ForeignKey
from practico08.data import Base

class Sala(Base):
        __tablename__ = 'sala'

        id = Column(Integer, autoincrement=True, primary_key=True)
        link = Column(String(255))
        id_dueno = Column(Integer, ForeignKey('usuario.id'))
        id_votacion = Column(Integer, ForeignKey('votacion.id'), nullable=True)

