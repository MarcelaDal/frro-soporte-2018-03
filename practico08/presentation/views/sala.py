from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.util import getRandomsString
from practico08.data.models import Sala, Usuario, Sesion
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


@Routes.get("/sala/buscar_canciones")
async def buscar_canciones(request):
    req = request.rel_url
    keywords = req.get('keywords')
    if keywords:
        async with ClientSession() as session:
            query = ""
            async with session.get('https://api.spotify.com/v1/search?q=abba&type=track&market=US',
                                   headers={'Content-Type': 'application/json',
                                       #ver autorizacion
                                            'Authorization': 'Bearer ' + request.app['token']
                                            }) as resp:
                    text = await resp.json()
                    miresp = web.json_response(status=200, data=text)
                    return miresp

    else:
        return web.Response(status=400)


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
<<<<<<< HEAD
=======


@Routes.post("/sala/add")
async def aniadir_usuario_sala(requests):
    req = await requests.json()
    id_sala = req.get("id_sala")
    if not id_sala:
        return web.json_response(status=400, data={"error":"Falta pararmetro id_sala"})
    id_usuario = req.get("id_usuario")
    if not id_usuario:
        return web.json_response(status=400, data={"error":"Falta pararmetro id_usuario"})
    usuario = requests.app['logic'].usuario.buscar_usuario_por_id(id_usuario)
    if not usuario:
        return web.json_response(status=400, data={"error":"Usuario invalido"})
    sala = requests.app['logic'].sala.buscar_sala_por_id(id_sala)
    if not sala:
        return web.json_response(status=400, data={"error":"Sala invalida"})
    sesion = requests.app['logic'].sesion.alta_sesion(Sesion(id_sala=id_sala,id_usuario=id_usuario))
    if sesion:
        return web.Response(status=200)
    else:
        return web.json_response(status=200, data={"error":"intente mas tarde"})
>>>>>>> practico08
