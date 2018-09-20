from urllib.parse import urlencode
from aiohttp import web, ClientSession
from practico08.util import getRandomsString
from practico08.data.models import Sala
from practico08.presentation import Routes

@Routes.view("/sala/new")
#pasa en el body el id del admin
class Sala(web.View):
    """
   Crear nueva sala
    """
    async def post(self):
        req = await self.request.json()
        if not req.get('id_admin'):
            return web.Response(text='Que me estas pasando???') #Modificar eso XD
        id_admin = req.get('id_admin')
        logic = self.request.app['logic']
        sala = logic.alta_sala(Sala(id_admin = id_admin))
        if sala:
            return web.Response(text="Sala creada")
        else:
            return web.Response(text="") # Esto tendria que devolver un json
