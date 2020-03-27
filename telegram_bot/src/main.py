import aiohttp

from . import client_utils

from aiohttp import web
import logging

from .utils import set_webhook
from ..config import conf


async def init(app):
    app.add_routes(client_utils.routes)
    logging.basicConfig(level=logging.DEBUG)
    app['session'] = aiohttp.ClientSession()
    app['config'] = conf
    yield
    await app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)
    set_webhook(conf)

    web.run_app(app, port=conf['port'])


if __name__ == '__main__':
    main()
