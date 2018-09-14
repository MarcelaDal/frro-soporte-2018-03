from sqlalchemy import Integer,String,Column
from practico08.data import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(255), unique=True)
    token = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)