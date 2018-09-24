from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,String, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(255), unique=True)
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    id_usuario_spotify = Column(String(255), nullable=True)

    #salas = relationship('Sesion', secondary=Sesion, lazy='subquery',
     #                    backref=backref('usuarios', lazy=True))

    #votos = relationship('Voto', uselist=True, backref='votos')


class Sala(Base):
    __tablename__ = 'sala'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_admin = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    link_invitacion = Column(String(250), default=0)
    votacion_vigente = Column(Boolean, nullable=False, default=0)
    id_playlist = Column(String(255))
    puntero = Column(Integer, default=1)


class Sesion(Base):
    __tablename__ = 'usuario_sala'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_sala = Column(Integer, ForeignKey('sala.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))


class Votacion(Base):
    __tablename__ = 'votacion'

    id = Column(Integer, autoincrement=True, primary_key=True)
    tiempo_vida = Column(Integer) #Esto por como funciona ahora se podria sascar
    id_sala = Column(Integer, ForeignKey('sala.id'))

    #votos = relationship('voto', uselist=True, backref='votos')


class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_votacion = Column(Integer, ForeignKey('votacion.id'))
    id_cancion = Column(String(255))
