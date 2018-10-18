from practico08.data import DatosSesion
from practico08.logic import LogicSingleton


class SesionException(Exception):
    pass


class LogicSesion(LogicSingleton):
    def alta(self, sesion):
        ses = self.buscar(sesion.id_usuario, sesion.id_sala)
        if ses:
            raise SesionException("Session vijente")
        s = DatosSesion().alta(sesion)
        return s

    def buscar(self, id_usuario, id_sala):
        s = DatosSesion().buscar(id_usuario, id_sala)
        return s

    def baja(self, sesion):
        bajamiento = DatosSesion().baja(sesion)
        return bajamiento

    def get_todos_por_id_sala(self, id_sala):
        todos = DatosSesion().todos()
        todos_por_id_sala = list(filter(lambda x: x.id_sala ==id_sala, todos))
        return todos_por_id_sala

    def borrar_todos(self):
        DatosSesion().borrar_todos()