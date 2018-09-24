from practico08.presentation import Routes
from practico08.data.models import Voto, Votacion
from aiohttp.web import Request, json_response
import asyncio

@Routes.post('/voto')
def votar(request):
    """
    :type request: Request
    :rtype: json_response
    Para votar, parametros: sala, cancion, nombre de usuario listo :D
    """
    req = await request.json()
    cancion = req.get('cancion')
    sala_id = req.get('sala')
    usuario_id = req.get('usuario')
    if cancion and sala_id and usuario_id:
        logic = request.app['logic']
        usuario = logic.buscar_usuario_por_id(usuario_id)
        if not usuario:
            return json_response(status=400,data={'error':'usuario no registrado'})
        sala = logic.buscar_sala_por_codigo(sala_id)
        if not sala:
            return json_response(status=400, data={"error":"sala inexistente"})
        # session = logic.buscar_session(usuario.id, sala.id)
        # if not session:
        #     return json_response(status=400, data={"error":"no hay session"})
        """
        Aca iria el post al voto
        Copiar la parte de ClientSession en auth y buscar en la referencia de la api de spotift como buscar una cancion :D
        """
        if not sala.votacion_vijente:
            # Ver spotify para ver cuanto tiempo queda y calcular el tiempo de vida
            # Despues agregar aca el tiempo de vida
            votacion = logic.alta_votacion(Votacion(id_sala=sala.id, tiempo_vida=30))
            request.app['horario'].spawn(lanzar_votacion(request, votacion))
        voto = logic.alta_voto(Voto(id_usuario=usuario.id, id_votacion=sala.votacion_vijente, id_cancion=cancion))
        if(voto):
            return json_response(status=200, data={"id_voto": voto.id})
    else:
        return json_response(status=400, data={"error":"bad requests"})


async def lanzar_votacion(request, votacion):
    """
    Trabajo que cambia la cancion
    :type request:Request
    :type votacion:Votacion
    """
    await asyncio.sleep(votacion.tiempo_vida)
    logic = request.app['logic']
    logic.baja_votacion(votacion)
    # Cambiar la cancion