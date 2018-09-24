from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.data.models import Usuario, Sala
from practico08.presentation import Routes


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
        if not req.get('nombre'):
            return web.Response(status=400, text='sin nombre')  # Modificar eso XD
        nombre = req.get('nombre')
        logic = self.request.app['logic']
        usuario = logic.alta_usuario(Usuario(nombre=nombre))
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
                return web.Response(status=200, text="Usuario registrado")
        else:
            return web.json_response(status=400, text=usuario)

    """
    No se que tan buena practica es implementarlo asi pero bue..., puse el retorno al que llamaria spotify dentro del misma entrada pero por get
    Basicamente hace el post a spotify le agrega el el token a al usuario y le creamos una sala
    """

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
                        logic = self.request.app.get('logic')
                        user = logic.buscar_usuario_por_id(state)
                        user.token = text['access_token']
                        user.refresh_token = text['refresh_token']
                        user = logic.modificar_usuario(user)
                        miresp = web.Response(status=200, text='Se ha registrado usuario')
                        return miresp
        return web.Response(status=502)
