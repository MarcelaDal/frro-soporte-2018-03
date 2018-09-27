from practico08.data import CapaDatos
from practico08.data.models import Usuario, Voto, Sala, Votacion
from practico08.logic.UsuarioLogic import UsuarioLogic
from practico08.logic.SalaLogic import SalaLogic
from practico08.logic.VotoLogic import VotoLogic
from practico08.logic.SesionLogic import SesionLogic
from collections import Counter
from urllib.parse import unquote


async def init_logic(app):
    logica = LogicController()
    app['logic'] = logica


class LogicController:
    """
    Clase que encapsula toda la logica
    """
    def __init__(self):
        self.datos = CapaDatos()
        self.usuario = UsuarioLogic(datos=self.datos)
        self.sala = SalaLogic(datos=self.datos)
        self.voto = VotoLogic(datos=self.datos)
        self.sesion = SesionLogic(datos=self.datos)

    def obtener_resultado_votacion(self, votacion, sala):
        resultado = unquote(Counter([voto.id_cancion for voto in self.voto.votos_get_all(votacion.id)]).most_common(1)[0][0])
        self.voto.baja_votacion(votacion.id)
        sala.votacion_vigente = False
        sala.puntero += 1
        self.sala.modificar_sala(sala)
        return resultado, sala.puntero - 1






