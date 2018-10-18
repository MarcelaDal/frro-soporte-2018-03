from practico08.data import DatosSala, DatosUsuarios
from practico08.util import Singleton


class SalaException(Exception):
    pass


class LogicSala(metaclass=Singleton):
    def alta(self, sala):
        s = None
        # TODO validar que tiene una sala activa a la vez?
        # TODO Funcionalidad recortada debido a falta de presupuesto
        user = DatosUsuarios().buscar_por_id(sala.id_admin)
        if not user.token:
            raise SalaException("El lince no tiene spotify, es pobre")
        salita = DatosSala().buscar_por_id_admin(sala.id_admin)
        if salita:
            raise SalaException("usuario ya con sala")
        s = DatosSala().alta(sala)
        if s:
            return s
        else:
            return False

    def buscar_por_id(self, id):
        s = DatosSala().buscar_por_id(id)
        if s:
            return s
        else:
            return False

    def busca_por_codigo(self, link):
        """
        Busca una sala por link de invitacion. Si no lo encuentra devuelve None
        :type id:str
        :rtype: Usuario
        """
        s = DatosSala().buscar_por_link(link)
        if s:
            return s
        else:
            return False

    def modificar(self, sala):
        sala = DatosSala().modificar(sala)
        return sala

    def borrar_todos(self):
        DatosSala().borrar_todos()
