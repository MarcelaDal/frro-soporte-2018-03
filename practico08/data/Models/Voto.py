from sqlalchemy import Integer,Column, ForeignKey, String
from practico08.data import Base


class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_votacion = Column(Integer, ForeignKey('votacion.id'))
    id_cancion = Column(String(255))