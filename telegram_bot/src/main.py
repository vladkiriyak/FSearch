import aiohttp

from src import client_utils

from aiohttp import web
import logging

from .utils import set_webhook, get_config
from .config import conf

async def init(app):
    app.add_routes(client_utils.routes)
    logging.basicConfig(level=logging.DEBUG)
    app['session'] = aiohttp.ClientSession()
    app['config'] = conf
    yield
    app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)
    set_webhook(app)

    web.run_app(app, port=app['config']['port'])


if __name__ == '__main__':
    main()
