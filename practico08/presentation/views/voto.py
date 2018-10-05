from aiohttp import ClientSession
from aiohttp.web import Request, json_response
import asyncio
from practico08.data.models import Voto, Votacion
from practico08.logic import LogicUsuario, LogicVoto,LogicSala, LogicSesion, LogicVotacion
from practico08.presentation import Routes


@Routes.post('/voto')
async def votar(request):
    """
    :type request: Request
    :rtype: json_response
    Para votar, parametros: sala, cancion, nombre de usuario listo :D
    """
    req = await request.json()
    cancion = req.get('cancion')
    sala_id = req.get('sala')
    usuario_id = req.get('usuario')
    if not cancion or not sala_id or not usuario_id:
        return json_response(status=400, data={"error":True, 'message': 'Bad Request '})
    if cancion and sala_id and usuario_id:
        logicUsuario = LogicUsuario()
        logicSala = LogicSala()
        logicVoto = LogicVoto()
        logicVotacion = LogicVotacion()
        logicSesion = LogicSesion()
        usuario = logicUsuario.buscar_por_id(usuario_id)
        if not usuario:
            return json_response(status=400, data={'message': 'No existe usuario registrado con ese id.'})
        sala = logicSala.buscar_por_id(sala_id)
        if not sala:
            return json_response(status=400, data={'message': 'No existe sala registrada con ese id.'})
        session = logicSesion.buscar(usuario.id, sala.id)
        if not session:
            # TODO mejorar mensaje de error
            return json_response(status=400, data={'message': "No existe sesión"})
        votacion = logicVotacion.buscar_por_id_sala(sala.id)
        if not sala.votacion_vigente:
            votacion = logicVotacion.alta(Votacion(id_sala=sala.id, tiempo_vida=0))
            sala.votacion_vigente = True
            sala = logicSala.modificar(sala)
            job = await request.app['horario'].spawn(lanzar_votacion(sala, votacion, request.app))
        voto = logicVoto.alta(Voto(id_usuario=usuario.id, id_votacion=votacion.id, id_cancion=cancion))
        if voto:
            return json_response(status=200, data={'messaje': 'El voto se efectuó con éxito!', 'body': {'id_voto': voto.id}})
    else:
        return json_response(status=400, data={'message': 'Bad Request'})


async def lanzar_votacion(sala, votacion, app):
    """
    Trabajo que cambia la cancion
    :type logic: LogicController
    :type votacion:Votacion
    """
    logicUsuario = LogicUsuario()
    logicSala = LogicSala()
    logicVotacion = LogicVotacion()
    user = logicUsuario.buscar_por_id_sala(sala.id)
    auth_str = "Authorization: Bearer " + user.token
    async with ClientSession() as session:
        reproduccion_actual = await session.get("https://api.spotify.com/v1/me/player/currently-playing",
                                                headers={
                                                    'Authorization': auth_str
                                                })
        reproduccion_actual_json = await reproduccion_actual.json()
        tiempo_vida = (int(reproduccion_actual_json['item']['duration_ms']) - int(reproduccion_actual_json['progress_ms'])) / 1000 - 10
        await asyncio.sleep(tiempo_vida)
        sala = logicSala.buscar_por_id(sala.id)
        cancion = logicVotacion.obtener_resultado(votacion, sala)
        resp = await session.post('https://api.spotify.com/v1/playlists/' + sala.id_playlist + '/tracks',
                                headers={
                                    'Authorization': auth_str,
                                    'Content-Type': 'application/json'
                                },
                                json={
                                    'uris': [cancion[0]],
                                    'position': cancion[1]
                                })
        json_resp = await resp.json()
