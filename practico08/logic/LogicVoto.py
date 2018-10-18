from practico08.data import DatosVotos
from practico08.logic import LogicSingleton


class VotoException(Exception):
    pass


class LogicVoto(LogicSingleton):
    def alta(self, voto):
        votos = self.todos_por_id_votacion(voto.id_votacion)
        print(voto.id_votacion)
        for vot in votos:
            if vot.id_usuario == voto.id_usuario:
                raise VotoException("El usuario ya voto")
        v = DatosVotos().alta(voto)
        return v

    def todos_por_id_votacion(self,id_votacion):
        votos = DatosVotos().todos_por_id_votacion(id_votacion)
        return votos

    def buscar_por_id_sesion(self,id_sesion):
        voto = DatosVotos().buscar_por_id_sesion(id_sesion)
        return voto

    def borrar_todos(self):
        DatosVotos().borrar_todos()
