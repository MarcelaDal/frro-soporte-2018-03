from aiohttp import web
from practico08.presentation import Routes
from practico08.config import config
import aiojobs
from practico08.presentation.views import  *


async def init():
    app = web.Application()
    app['horario'] = await aiojobs.create_scheduler(limit=None)
    app['config'] = config
    app.add_routes(Routes)
    # app.on_startup.append(init_logic)
    return app


if __name__ == '__main__':
    web.run_app(init())
