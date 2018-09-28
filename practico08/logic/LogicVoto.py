from practico08.data import DatosVotos
from practico08.logic import LogicSingleton


class LogicVoto(LogicSingleton):
    def __init__(self, datos):
        super().__init__(datos)

    def alta_voto(self, voto):
        v = DatosVotos().alta(voto)
        return v

    def todos_por_id_votacion(self,id_votacion):
        votos = DatosVotos().todos_por_id_votacion(id_votacion)
        return votos
