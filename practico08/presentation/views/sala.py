from aiohttp import web, ClientSession
from practico08.data import Sala, Usuario, Sesion
from practico08.logic import LogicSala, LogicUsuario, LogicSesion
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
    nombre = req.get('nombre')
    password = req.get('password')
    if not password or not nombre:
        return web.json_response(status=400, text={'message': 'Bad Request'})
    playlist_name = req.get('playlist_name')
    playlist_description = req.get('playlist_description')
    logicUsuario = LogicUsuario()
    usuario = logicUsuario.buscar_por_nombre(nombre,password)
    if type(usuario) == Usuario:
        nueva_sala = Sala()
        nueva_sala.id_admin = usuario.id
        nueva_sala.link_invitacion = getRandomsString()
        async with ClientSession() as session:
            id_usuario_spotify = usuario.id_usuario_spotify
            data = {'public': 'false'}
            data['name'] = playlist_name if playlist_name else "Spotifesta"
            if playlist_description:
                data['description'] = playlist_description
            async with session.post('https://api.spotify.com/v1/users/'+str(id_usuario_spotify)+'/playlists',
                                     headers={
                                        'Content-Type': 'application/json',
                                        'Authorization': 'Bearer ' + usuario.token
                                    },
                                    json=data
                                   ) as resp:
                text = await resp.json()
                if resp.status in [200, 201]:
                    nueva_sala.id_playlist = str(text['id'])
                    logicSala = LogicSala()
                    sala = logicSala.alta(nueva_sala)
                    if type(sala) == Sala:
                        return web.json_response(status=200, data={'message': 'La lista de reproducción para tu fiesta se creó con éxito!'})
                    else:
                        return web.json_response(status=500, data={'message': 'Se produjo un error.'})
                else:
                    return web.json_response(status=resp.status, data=text)
    else:
        return web.json_response(status=500, data={'message': 'Se produjo un error.'})


@Routes.get("/sala/buscar_canciones")
async def buscar_canciones(request):
    ''' /sala/buscar_canciones?q=abba '''
    params = request.rel_url.query
    keywords = params['q']
    query = (keywords.replace(' ', '%20'))
    if keywords:
        async with ClientSession() as session:
            #TODO ver como funciona con parámetros que tienen espacios
            async with session.get('https://api.spotify.com/v1/search?q=' + query + '&type=track',
                                   headers={'Content-Type': 'application/json',
                                       #TODO ver autorizacion
                                            'Authorization': 'Bearer ' + request.app['token']
                                            }) as resp:
                    text = await resp.json()
                    return web.json_response(status=200, data={'message': '', 'body': text, 'error': False})
    else:
        return web.json_response(status=400, data={'message': 'Bad Request', 'error': True})


@Routes.get("/sala/users")
async def obtener_usuario_de_sala(request):
    req = await request.json()
    id_sala = req.get("id_sala")
    if id_sala:
        logicSala = LogicSala()
        sala = logicSala.buscar_por_id(id_sala)
        if type(sala) == Sala:
            # TODO pasar Sala a JSON
            logicSesion = LogicSesion()
            sesiones_en_sala = logicSesion.get_todos_por_id_sala(sala.id)
            usuarios = [LogicUsuario().buscar_por_id(sesion.id_usuario) for sesion in sesiones_en_sala]
            usuarios_pelados = [{'id': usuario.id, 'nombre': usuario.nombre} for usuario in usuarios]
            return web.json_response(status=200, data={'message': '', 'body': usuarios_pelados})
        else:
            return web.json_response(status=200, data={'message': 'No existe sala con ese código de invitación.', 'error': True})

    else:
        return web.json_response(status=400, data={'message': 'Bad Request', 'error': True})

@Routes.get("/sala/{link_invitacion}")
async def obtener_sala_por_link(request):
    code = request.match_info['link_invitacion']
    if code:
        logicSala = LogicSala()
        sala = logicSala.busca_por_codigo(code)
        if type(sala) == Sala:
            #TODO pasar Sala a JSON
            return web.json_response(status=200, data={'message': '', 'body': sala.id})
        else:
            return web.json_response(status=200, data={'message': 'No existe sala con ese código de invitación.', 'error': True})

    else:
        return web.json_response(status=400, data={'message': 'Bad Request', 'error':True})


@Routes.post("/sala/add")
async def aniadir_usuario_sala(requests):
    req = await requests.json()
    id_sala = req.get("id_sala")
    nombre = req.get("nombre")
    password = req.get("password")
    if not id_sala or not nombre or not password:
        return web.json_response(status=400, data={"message": "Bad Request"})
    usuario = LogicUsuario().buscar_por_nombre(nombre,password)
    if not usuario:
        return web.json_response(status=400, data={"message": "No existe usuario con ese id."})
    sala = LogicSala().buscar_por_id(id_sala)
    if not sala:
        return web.json_response(status=400, data={"message": "No existe sala con ese id."})

    sesion = LogicSesion().alta(Sesion(id_sala=sala.id,id_usuario=usuario.id))
    if sesion:
        return web.json_response(status=200, data={'message': 'Session reistrada con éxito'})
    else:
        return web.json_response(status=500, data={"error": True, 'message': 'Se produjo un error.'})





@Routes.post("/sala/remove")
async def remove_user(request):
    req = await request.json()
    id_sala = req.get("id_sala")
    id_usuario = req.get("id_usuario")
    admin = req.get("admin")
    password = req.get("password")
    if not id_sala or not id_usuario or not password or not admin:
        return web.json_response(status=400, data={"message": "Bad Request"})
    usuario = LogicUsuario().buscar_por_nombre(admin, password)
    if not usuario:
        return web.json_response(status=400, data={"message": "Credenciales erroneas"})
    sesion = LogicSesion().buscar(id_usuario, id_sala)
    if not sesion:
        return web.json_response(status=400, data={"message": "Credenciales erroneas"})
    bajamiento = LogicSesion().baja(sesion)
    if bajamiento:
        return web.json_response(status=200, data={'message': 'usuario eliminado de la sala'})
    else:
        return web.json_response(status=200, data={'message': 'error desconocido'})
