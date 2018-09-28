from practico08.data import DatosSesion
from practico08.logic import LogicSingleton


class LogicSession(LogicSingleton):
    def __init__(self, datos):
        super().__init__(datos)

    def alta(self, session):
        s = DatosSesion().alta(session)
        return s

    def buscar_sesion(self, id_usuario, id_sala):
        s = DatosSesion().buscar(id_usuario, id_sala)
        return s

