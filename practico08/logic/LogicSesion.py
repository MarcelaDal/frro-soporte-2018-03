from practico08.data import DatosSesion
from practico08.logic import LogicSingleton


class LogicSesion(LogicSingleton):
    def alta(self, session):
        s = DatosSesion().alta(session)
        return s

    def buscar(self, id_usuario, id_sala):
        s = DatosSesion().buscar(id_usuario, id_sala)
        return s

