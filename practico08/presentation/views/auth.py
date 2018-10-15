from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.data.models import Usuario, Sala
from practico08.logic import LogicUsuario
from practico08.presentation import Routes
import json

@Routes.view("/auth")
class Auth(web.View):
    """
    Punto de entrada para registrar un usuario
    En la request tiene que venir el nombre y si vincula cuenta de spotify
    El nombre es obligatorio
    Si viene con hasSpotify redirije a spotify para que lo autorize
    Si el usuario tiene refresh token o token significa que ya fue authentificado una ves
    """

    async def post(self):
        req = await self.request.json()
        nombre = req.get('nombre')
        password = req.get('password')
        if not nombre or not password:
            return web.json_response(status=400, data={'message': 'Bad Request'})
        nuevo_usuario = Usuario()
        nuevo_usuario.nombre = nombre
        nuevo_usuario.password = password
        logicUsuario = LogicUsuario()
        usuario = logicUsuario.alta(nuevo_usuario)
        if type(usuario) == Usuario:
            if req.get('hasSpotify') and not (usuario.token or usuario.refresh_token):
                return web.json_response(status=200, data={"url": 'https://accounts.spotify.com/authorize?' +
                                                                  urlencode({'response_type': 'code',
                                                                             'client_id': self.request.app['config']['client_id'],
                                                                             'scope': self.request.app['config']['scope'],
                                                                             'redirect_uri': self.request.app['config']['callback_uri'],
                                                                             'state': str(usuario.id)
                                                                             })})
            else:
                return web.json_response(status=200, data={'message': 'Usuario registrado con éxito'})
        else:
            return web.json_response(status=200, data=({'error':True, 'message':str(usuario)}))

    async def get(self):
        code = self.request.rel_url.query.get('code')
        state = self.request.rel_url.query.get('state')
        if code:
            async with ClientSession() as session:
                async with session.post('https://accounts.spotify.com/api/token',
                                        data={'grant_type': "authorization_code",
                                              'code': code,
                                              'redirect_uri': self.request.app['config']['callback_uri'],
                                              'client_id': self.request.app['config']['client_id'],
                                              'client_secret': self.request.app['config']['secret_id']}) as resp:
                    if resp.status == 200:
                        text = await resp.json()
                        logicUsuario = LogicUsuario()
                        user = logicUsuario.buscar_por_id(state)
                        user.token = text['access_token']
                        user.refresh_token = text['refresh_token']
                        user_data = await session.get('https://api.spotify.com/v1/me',
                                                      headers={'Authorization': 'Bearer '+ user.token}
                                                      )
                        user_data_json = await user_data.json()
                        user.id_usuario_spotify = user_data_json['id']
                        user = logicUsuario.modificar(user)
                        if type(user) == Usuario:
                            return web.json_response(status=200, data={'message': 'Usuario registrado con éxito!', 'error': False})
                        else:
                            return web.json_response(status=500, data={'message': 'Se produjo un error.', 'error': True})
                    else:
                        return web.json_response(status=resp.status, data={'message': resp.json, 'error': True})

        else:
            return web.json_response(status=400, data={'message': 'Bad Request', 'error': True})
