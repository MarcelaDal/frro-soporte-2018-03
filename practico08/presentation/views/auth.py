from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.util import getRandomsString
from practico08.data.Models import Usuario, Sala


class Auth(web.Views):
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
            return web.Response(text='Que me estas pasando???') #Modificar eso XD
        nombre = req.get('nombre')
        logic = self.request.app['logic']
        usuario = logic.getUserByName(nombre)
        if(not usuario):
            usuario = Usuario()
            usuario.nombre = nombre
            logic.saveUser(usuario) #Implementar Metodo
        if req.get('hasSpotify') and not (usuario.token or usuario.refresh_token):
            usuario = logic.getUserPorNombre('nombre') #Implementar Metodo
            return web.HTTPFound('https://accounts.spotify.com/authorize?'
                                 + urlencode({'response_type': 'code',
                                              'client_id': self.request.app['config']['client_id'],
                                              'scope': 'user-modify-playback-state',
                                              'redirect_uri': self.request.app['config']['callback_uri'],
                                              'state':  str(usuario.id)
                                              }))
        else:
            web.Response(text="Nada que hacer :P") #Modificar esto tambien XD
    """
    No se que tan buena practica es implementarlo asi pero bue..., puse el retorno al que llamaria spotify dentro del misma entrada pero por get
    Basicamente hace el post a spotify le agrega el el token a al usuario y le creamos una sala
    """
    async def get(self):
        code = self.request.rel_uri.query.get('code')
        state = self.request.rel_uri.query.get('state')
        if code:
            async with ClientSession() as session:
                async with session.post('https://accounts.spotify.com/api/token',
                                        data={'grant_type': "authorization_code",
                                              'code': code,
                                              'redirect_uri': self.request.app['config']['callback_uri'],
                                              'client_id': self.request.app['config']['client_id'],
                                              'client_secret': self.request.app['config']['client_secret']}) as resp:
                    text = await resp.json()
                    logic = self.request.app.get('logic')
                    user = logic.getUserById(state)
                    user.token = text['access_token']
                    user.refresh_token = text['refresh_token']
                    logic.saveUser(user)
                    sala_nueva = Sala()
                    sala_nueva.id_usuario = user.id
                    sala_nueva.link = getRandomsString()
                    logic.saveSala(sala_nueva)
                    return web.Response(text='Se ha registrado alto usuario wachim') #Cambiar esto tambien XD