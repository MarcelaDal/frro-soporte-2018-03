from practico08.data import DatosSala
from practico08.util import Singleton


class LogicSala(metaclass=Singleton):
    def alta(self, sala):
        s = None
        # TODO validar que tiene una sala activa a la vez?
        # TODO Funcionalidad recortada debido a falta de presupuesto
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
