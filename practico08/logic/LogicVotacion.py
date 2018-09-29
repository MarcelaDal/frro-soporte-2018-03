from collections import Counter
from urllib.parse import unquote
from practico08.data import DatosVotacion
from practico08.logic import LogicSingleton
from practico08.logic import LogicSala
from practico08.logic import LogicVoto


class LogicVotacion(LogicSingleton):
    def obtener_resultado(self, votacion, sala):
        resultado = unquote(Counter([voto.id_cancion for voto in LogicVoto().todos_por_id_votacion(votacion.id)]).most_common(1)[0][0])
        self.baja(votacion.id)
        sala.votacion_vigente = False
        sala.puntero += 1
        LogicSala().modificar(sala)
        return resultado, sala.puntero - 1

    def buscar_por_id_sala(self, id_sala):
        votacion = None
        sala = LogicSala().buscar_por_id(id_sala)
        if sala:
            votacion = DatosVotacion().buscar_por_id_sala(sala.id)
        return votacion

    def buscar_por_id(self, id):
        votacion = DatosVotacion().buscar_por_id(id)
        return votacion

    def baja(self, id):
        votacion = self.buscar_por_id(id)
        DatosVotacion().baja(votacion)

    def alta(self, votacion):
        v = DatosVotacion().alta(votacion)
        return v
