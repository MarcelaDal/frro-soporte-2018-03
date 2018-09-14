from aiohttp import  web
from practico08.logic import init_logic
from practico08.presentation import Routes
from practico08.config import config
from practico08.presentation.views import  *
if __name__ == '__main__':
    app = web.Application()
    app.add_routes(Routes)
    app.on_startup.append(init_logic)
    app['config'] = config
