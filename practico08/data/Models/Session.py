from sqlalchemy import Integer,Column, ForeignKey
from practico08.data import Base


class Sesion(Base):
        __tablename__ = 'usuario_sala'

        id = Column(Integer, autoincrement=True, primary_key=True)
        id_sala = Column(Integer, ForeignKey('sala.id'))
        id_usuario = Column(Integer, ForeignKey('usuario.id'))