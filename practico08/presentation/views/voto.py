from practico08.presentation import Routes
from practico08.data.models import Voto, Votacion
from aiohttp import ClientSession
from aiohttp.web import Request, json_response
import asyncio
from practico08.logic import Logic

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
            votacion = logic.alta_votacion(Votacion(id_sala=sala.id, tiempo_vida=30))
            request.app['horario'].spawn(lanzar_votacion(logic, votacion, request.app))
        voto = logic.alta_voto(Voto(id_usuario=usuario.id, id_votacion=sala.votacion_vijente, id_cancion=cancion))
        if(voto):
            return json_response(status=200, data={"id_voto": voto.id})
    else:
        return json_response(status=400, data={"error":"bad requests"})


async def lanzar_votacion(logic, votacion, app):
    """
    Trabajo que cambia la cancion
    :type logic: Logic
    :type votacion:Votacion
    """
    # Ver spotify para ver cuanto tiempo queda y calcular el tiempo de vida
    # Despues agregar aca el tiempo de vida la posicion de la siguiente cancion, etc
    user = logic.buscar_usuario_por_id(votacion.id_sala)
    auth_str = "Authorization: Bearer " + user.token
    async with ClientSession() as session:
        reproduccion_actual = await session.get("https://api.spotify.com/v1/me/player/currently-playing",
                                                headers={
                                                    'Authorization': auth_str
                                                })
        reproduccion_actual_json = await reproduccion_actual.json()
        playlist_id = reproduccion_actual_json
        await asyncio.sleep()
        logic.baja_votacion(votacion)
        # Cambiar la cancion

        await session.post('https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks',
                                headers={
                                    'Authorization': auth_str,
                                    'Content-Type': 'application/json'
                                },
                                json={
                                    'uris': ['spotify:track:4EchqUKQ3qAQuRNKmeIpnf'],
                                    'position': 3
                                })