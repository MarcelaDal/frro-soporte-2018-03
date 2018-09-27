from practico08.presentation import Routes
from practico08.data.models import Voto, Votacion
from aiohttp import ClientSession
from aiohttp.web import Request, json_response
import asyncio
from practico08.logic import LogicController


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
    if cancion and sala_id and usuario_id:
        logic = request.app['logic']
        logicUsuario = logic.usuario
        logicSala = logic.sala
        logicVoto = logic.voto
        usuario = logicUsuario.buscar_usuario_por_id(usuario_id)
        if not usuario:
            return json_response(status=400,data={'error':'usuario no registrado'})
        sala = logicSala.buscar_sala_por_id(sala_id)
        if not sala:
            return json_response(status=400, data={"error":"sala inexistente"})
        # session = logic.buscar_session(usuario.id, sala.id)
        # if not session:
        #     return json_response(status=400, data={"error":"no hay session"})
        votacion = logicVoto.buscar_votacion_por_id_sala(sala.id)
        print(sala.votacion_vigente)
        if not sala.votacion_vigente:
            votacion = logicVoto.alta_votacion(Votacion(id_sala=sala.id, tiempo_vida=0))
            sala.votacion_vigente = True
            sala = logicSala.modificar_sala(sala)
            job = await request.app['horario'].spawn(lanzar_votacion(sala, votacion, request.app))
        voto = logicVoto.alta_voto(Voto(id_usuario=usuario.id, id_votacion=votacion.id, id_cancion=cancion))
        if voto:
            return json_response(status=200, data={"id_voto": voto.id})
    else:
        return json_response(status=400, data={"error":"bad requests"})


async def lanzar_votacion(sala, votacion, app):
    """
    Trabajo que cambia la cancion
    :type logic: LogicController
    :type votacion:Votacion
    """
    user = app['logic'].usuario.buscar_usuario_por_id_sala(sala.id)
    auth_str = "Authorization: Bearer " + user.token
    async with ClientSession() as session:
        reproduccion_actual = await session.get("https://api.spotify.com/v1/me/player/currently-playing",
                                                headers={
                                                    'Authorization': auth_str
                                                })
        reproduccion_actual_json = await reproduccion_actual.json()
        tiempo_vida = (int(reproduccion_actual_json['item']['duration_ms']) - int(reproduccion_actual_json['progress_ms'])) / 1000 - 10
        await asyncio.sleep(tiempo_vida)
        sala = app['logic'].sala.buscar_sala_por_id(sala.id)
        cancion = app['logic'].obtener_resultado_votacion(votacion, sala)
        print(cancion)
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
        print(json_resp)


@Routes.post('/add')
async def add(request):
    async with ClientSession() as session:
        async with session.post('https://api.spotify.com/v1/playlists/3XHCgLC96373KxA6bVeh4s/tracks',
                                headers={
                                    'Authorization': "Authorization: Bearer BQCtIbzspAmhxxOOwrsF1FW8FQ8TILKLyoX0zvYv9NCHW7D6WqS-hJHtCevq06n48jEw_yxgw2K0SLCaqLbioxd7hMqi1pRCZDYR2CaJxW0NpcYrapDna8MEGsueieIVVpinOKZsWp_-ggDZXbtqHKBPjwHQ6jYwEFhwIVj48OETt4nVAOoI1fw3o6pgaImp6fwGaoHPI3em27JVTcDoHqCGHw",
                                    'Content-Type': 'application/json'
                                },
                                json={
                                    'uris': ["spotify:track:5ghIJDpPoe3CfHMGu71E6T"],
                                    'position': 0
                                }) as resp:
            resp_json = await resp.json()
            return json_response(data=resp_json)