from base64 import b64encode

from aiohttp import web, ClientSession
from practico08.data import Sala, Usuario, Sesion
from practico08.logic import LogicSala, LogicUsuario, LogicSesion
from practico08.server import Routes
from practico08.util import getRandomsString
import json

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
    usuario = logicUsuario.buscar_por_nombre(nombre, password)
    if usuario:
        try:
            nueva_sala = Sala()
            nueva_sala.id_admin = usuario.id
            nueva_sala.link_invitacion = getRandomsString()
            async with ClientSession() as session:
                token_nuevo = await session.post('https://accounts.spotify.com/api/token',
                                                 headers={
                                                     'Authorization': 'Basic ' + b64encode((request.app['config']['client_id'] + ':' + request.app['config']['secret_id']).encode('ascii')).decode('ascii')
                                                 },
                                                 data={
                                                     'grant_type': 'refresh_token',
                                                     'refresh_token': usuario.refresh_token
                                                 })
                if token_nuevo.status != 200:
                    error = await token_nuevo.text()
                    return web.Response(text=error)
                token_nuevo = await token_nuevo.json()
                usuario.token = token_nuevo['access_token']
                usuario = logicUsuario.modificar(usuario)
                if not usuario:
                    return web.json_response(data={'error': True, 'message': 'No se pudo crear la sala.'})
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
                        #TODO: agregué esto porq al momento de la votacion sino trae problemas
                        sesion = LogicSesion().alta(Sesion(id_sala=sala.id, id_usuario=usuario.id))
                        json_sala= {'id_sala': sala.id, 'id_playlist': sala.id_playlist, 'id_admin': sala.id_admin, 'link_invitacion': sala.link_invitacion, 'hay_votacion': sala.votacion_vigente}
                        return web.json_response(status=200, data={'message': 'La lista de reproducción para tu fiesta se creó con éxito!', 'error': False, 'body': json_sala })
                    else:
                        return web.json_response(status=resp.status, data=text)
        except Exception as e:
            return web.json_response(status=200, data={'message': 'Se produjo un error con la sala.', 'error': str(e)})
    else:
        return web.json_response(status=200, data={'message': 'Se produjo un error con el usuario.','error': True})


@Routes.get("/sala/{id_sala}/buscar_canciones")
async def buscar_canciones(request):
    ''' /sala/buscar_canciones?query=abba '''
    params = request.rel_url.query
    keywords = params['query']
    id_sala = request.match_info['id_sala']
    sala= LogicSala().buscar_por_id(id_sala)
    if keywords and sala:
        query = (keywords.replace(' ', '%20'))
        user = LogicUsuario().buscar_por_id(sala.id_admin)
        async with ClientSession() as session:
            async with session.get('https://api.spotify.com/v1/search?q=' + query + '&type=track',
                                   headers={'Content-Type': 'application/json',
                                            'Authorization': 'Bearer ' + user.token
                                            }) as resp:
                text = await resp.json()
                return web.json_response(status=200, data={'message': '', 'body': text, 'error': False})
    else:
        return web.json_response(status=200, data={'message': 'Bad Request', 'error': True})


@Routes.get("/sala/{id_sala}/users")
async def obtener_usuarios_de_sala(request):
    id_sala = request.match_info['id_sala']
    if id_sala:
        logicSala = LogicSala()
        sala = logicSala.buscar_por_id(id_sala)
        if type(sala) == Sala:
            # TODO pasar Sala a JSON
            logicSesion = LogicSesion()
            sesiones_en_sala = logicSesion.get_todos_por_id_sala(sala.id)
            usuarios = [LogicUsuario().buscar_por_id(sesion.id_usuario) for sesion in sesiones_en_sala]
            array_usuarios = [{'id': usuario.id, 'nombre': usuario.nombre} for usuario in usuarios]
            return web.json_response(status=200, data={'message': '', 'body': array_usuarios})
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
            return web.json_response(status=200, data={'message': '', 'body': {'id_sala': sala.id}, 'error': False})
        else:
            return web.json_response(status=200, data={'message': 'No existe sala con ese código de invitación.', 'error': True})

    else:
        return web.json_response(status=400, data={'message': 'Bad Request', 'error': True})


@Routes.post("/sala/add")
async def aniadir_usuario_sala(requests):
    #TODO: habría que buscar el usuario x id
    req = await requests.json()
    id_sala = req.get("id_sala")
    nombre = req.get("nombre")
    password = req.get("password")
    if not id_sala or not nombre or not password:
        return web.json_response(status=400, data={"message": "Bad Request"})
    usuario = LogicUsuario().buscar_por_nombre(nombre, password)
    if not usuario:
        return web.json_response(status=200, data={"message": "No existe usuario con ese nombre.", 'error': True})
    sala = LogicSala().buscar_por_id(id_sala)
    if not sala:
        return web.json_response(status=400, data={"message": "No existe sala con ese id.", 'error': True})
    try:
        sesion = LogicSesion().alta(Sesion(id_sala=sala.id, id_usuario=usuario.id))
        return web.json_response(status=200, data={'message': 'Session registrada con éxito', 'error': False, 'body': {'user_id': usuario.id}})
    except Exception as e:
        return web.json_response(status=200, data={"error": True, 'message': str(e)})


@Routes.post("/sala/user/remove")
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
        return web.json_response(status=400, data={"message": "Credenciales erroneas", 'error': True})
    sesion = LogicSesion().buscar(id_usuario, id_sala)
    if not sesion:
        return web.json_response(status=400, data={"message": "Credenciales erroneas", 'error': True})
    baja = LogicSesion().baja(sesion)
    if baja:
        return web.json_response(status=200, data={'message': 'Usuario eliminado de la sala', 'error': False})
    else:
        return web.json_response(status=200, data={'message': 'error desconocido', 'error': True})


@Routes.post("/sala/playlist/modificar")
async def modificar_playlist(request):
    req = await request.json()
    id_sala = req.get("id_sala")
    playlist_name = req.get('playlist_name')
    playlist_description = req.get('playlist_description')
    if not id_sala or not playlist_name or not playlist_description:
        return web.json_response(status=400, data={'message': 'Bad Request'})
    sala = LogicSala().buscar_por_id(id_sala)
    if type(sala) == Sala:
        usuario = LogicUsuario().buscar_por_id(sala.id_admin)
        async with ClientSession() as session:
            id_playlist = sala.id_playlist
            async with session.put('https://api.spotify.com/v1/playlists/' + id_playlist,
                                   headers={
                                       'Content-Type': 'application/json',
                                       'Authorization': 'Bearer ' + usuario.token
                                   },
                                   data={
                                       "name": "Updated Playlist Name",
                                       "description": "Updated playlist description",
                                       "public": 'false'
                                   }
                                   ) as resp:
                text = await resp.json()
                if text['error']:
                    return web.json_response(status=text['error']['status'], data={'message': text['error']['message'], 'error': True})
                else:
                    return web.json_response(status=200, data={'message': '', 'body': text, 'error': False})

    else:
        return web.json_response(status=500, data={'message': 'Se produjo un error.'})


@Routes.post("/sala/playlist/addTracks")
async def agregar_canciones(request):
    req = await request.json()
    id_sala = req.get("id_sala")
    array_uris = req.get("uris")
    if not id_sala or not array_uris:
        return web.json_response(status=400, data={'message': 'Bad Request'})
    sala = LogicSala().buscar_por_id(id_sala)
    if type(sala) == Sala:
        usuario = LogicUsuario().buscar_por_id(sala.id_admin)
        async with ClientSession() as session:
            id_playlist = sala.id_playlist
            uris = ''
            for uri in array_uris:
                rep= uri.replace(':', '%3A')
                uris += rep + '%2C'

#            uris= 'spotify%3Atrack%3A4iV5W9uYEdYUVa79Axb7Rh%2Cspotify%3Atrack%3A1301WleyT98MSxVHPZCA6M'
            async with session.post('https://api.spotify.com/v1/playlists/' + id_playlist + '/tracks?position=0&uris=' + uris  ,
                                    headers={
                                        'Content-Type': 'application/json',
                                        'Authorization': 'Bearer ' + usuario.token
                                    }
                                    ) as resp:
                text = await resp.json()
                if resp.status not in [200,201]:
                    return web.json_response(status=text['error']['status'], data={'message': text['error']['message'], 'error': True})
                else:
                    return web.json_response(status=200, data={'message': 'Se han agregado las canciones con éxito', 'body': text, 'error': False})

    else:
        return web.json_response(status=500, data={'message': 'Se produjo un error.'})

if __name__ == '__main__':
    import asyncio
    async def main():
        from practico08.config import config
        usuario = LogicUsuario().buscar_por_nombre("Thomirotho","theend1969")
        async with ClientSession() as session:
            async with session.post('https://accounts.spotify.com/api/token',
                                    headers={
                                        'Authorization': 'Basic ' + b64encode((config['client_id']+':'+config['secret_id']).encode('ascii')).decode('ascii')
                                    },
                                    json={
                                        'grant_type': 'refresh_token',
                                        'refresh_token': usuario.refresh_token
                                    }) as resp:
                text = await resp.text()
                print(text)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
