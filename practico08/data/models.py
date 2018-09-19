from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,String, Column, DateTime, ForeignKey

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(255), unique=True)
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)


class Sala(Base):
    __tablename__ = 'sala'

    id = Column(Integer, autoincrement=True, primary_key=True)
    link = Column(String(255))
    id_dueno = Column(Integer, ForeignKey('usuarios.id'))
    id_votacion = Column(Integer, ForeignKey('votacion.id'), nullable=True)


class Sesion(Base):
    __tablename__ = 'usuario_sala'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_sala = Column(Integer, ForeignKey('sala.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))


class Votacion(Base):
    __tablename__ = 'votacion'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tiempo_vida = Column(DateTime)
    id_sala = Column(Integer, ForeignKey('sala.id'))

class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_votacion = Column(Integer, ForeignKey('votacion.id'))
    id_cancion = Column(String(255))