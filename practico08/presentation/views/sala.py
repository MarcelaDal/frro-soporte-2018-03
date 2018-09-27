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
    # pasar los datos de la playlist en el body
    req = await request.json()
    if not req.get('id_admin'):
        return web.Response(text='Bad Request', status=400)
    id_admin = req.get('id_admin')
    playlist_name = req.get('playlist_name')
    playlist_description = req.get('playlist_description')
    logicUsuario = request.app['logic'].usuario
    usuario = logicUsuario.buscar_usuario_por_id(id_admin)
    if type(usuario) == Usuario:
        nueva_sala = Sala()
        nueva_sala.id_admin = usuario.id
        nueva_sala.link_invitacion = getRandomsString()
        async with ClientSession() as session:
                id_usuario_spotify = usuario.id_usuario_spotify
                async with session.post('https://api.spotify.com/v1/users/'+str(id_usuario_spotify)+'/playlists',
                                         headers={
                                            'Content-Type': 'application/json',
                                            'Authorization': 'Bearer ' + usuario.token
                                        },
                                        json={
                                            'name': playlist_name,
                                            'description': playlist_description,
                                            'public': 'false'
                                        }
                                       ) as resp:
                    text = await resp.json()
                    nueva_sala.id_playlist = text['id']
                    logicSala = request.app['logic'].sala
                    sala = logicSala.alta_sala(nueva_sala)
                    miresp = web.Response(status=200, text="Sala creada")
                    return miresp
            #return web.Response(text="Sala creada")
            #return web.Response(text="No se ha podido crear una nueva sala. Intente más tarde.")

@Routes.get("/sala/{link_invitacion}")
async def obtener_sala_por_link(request):
    code = request.match_info['link_invitacion']
    if code:
        logic = request.app['logic'].sala
        sala = logic.buscar_sala_por_codigo(code)
        miresp = web.json_response(status=200, data={"id_sala": sala.id, "id_admin": sala.id_admin})
        return miresp
    else:
        return web.Response(status=400)

