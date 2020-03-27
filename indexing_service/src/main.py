import aiohttp

from .routes import routes

import logging
from aiohttp import web

from ..config import conf


async def init(app):
    app.add_routes(routes)
    logging.basicConfig(level=logging.DEBUG)
    app['config'] = conf

    app['session'] = aiohttp.ClientSession()
    yield
    await app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)
    web.run_app(app, port=conf['port'])


if __name__ == '__main__':
    main()
