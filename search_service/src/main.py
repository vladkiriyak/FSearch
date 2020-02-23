import aiohttp

from src import routes

from aiohttp import web
import logging

from src.utils import get_config
from .config import conf

async def init(app):
    app.add_routes(routes.routes)
    logging.basicConfig(level=logging.DEBUG)
    app['config'] = conf
    app['session'] = aiohttp.ClientSession()
    yield
    app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)
    app['config'] = get_config('../../telegram_bot/config.json')
    web.run_app(app, port=app['config']['port'])


if __name__ == '__main__':
    main()