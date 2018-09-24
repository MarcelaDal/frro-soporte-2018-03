from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.util import getRandomsString
from practico08.data.models import Sala, Usuario
from practico08.presentation import Routes
from practico08.util import getRandomsString

@Routes.post("/sala/new")
#pasa en el body el id del admin
async def crear_sala(request):
    """
   Crear nueva sala
    """
    req = await request.json()
    if not req.get('id_admin'):
        return web.Response(text='Bad Request', code=400)
    id_admin = req.get('id_admin')
    logic = request.app['logic']
    usuario = logic.buscar_usuario_por_id(id_admin)
    if type(usuario) == Usuario:
        nueva_sala = Sala()
        nueva_sala.id_admin = usuario.id
        nueva_sala.link_invitacion = getRandomsString()
        sala = logic.alta_sala(nueva_sala)

        if type(sala) == Sala:
            async with ClientSession() as session:
                    id_usuario_spotify = usuario.id_usuario_spotify
                    async with session.post('https://api.spotify.com/v1/playlists',
                                             headers={
                                                'Accept': 'application/json',
                                                'Content-Type': 'application/json',
                                                'Authorization': 'Bearer BQAWchdDbseX4Izz9sqC4DoNBj1gSfDZ4C3ADu_OrkQWsBibbi4DwSp1vRFqg6gUgRU3nCME_PPVC4oxxaMvlNeCAqme8XwlIkGIrdxo8eDbauJ'
                                            },
                                            data={
                                                'name': 'New Playlist',
                                                'description': 'New playlist description',
                                                'public': 'false'
                                            }
                                           ) as resp:
                        if resp:
                            text = await resp.json()
                            resp = resp.status
                            miresp = web.Response(status=200, text=str(resp))
                            return miresp
                        else:
                            return resp
            #return web.Response(text="Sala creada")
        else:
            return web.Response(text="No se ha podido crear una nueva sala. Intente más tarde.")

@Routes.get("/sala/{link_invitacion}")
async def obtener_sala_por_link(request):
    code = request.match_info['link_invitacion']
    if code:
        logic = request.app['logic']
        sala = logic.buscar_sala_por_codigo(code)
        miresp = web.json_response(status=200, data={"id_sala": sala.id, "id_admin": sala.id_admin})
        return miresp

