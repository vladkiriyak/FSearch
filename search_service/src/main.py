import aiohttp

from .routes import routes
from ..config import conf


from aiohttp import web
import logging


async def init(app):

    app.add_routes(routes)
    logging.basicConfig(level=logging.DEBUG)
    app['config'] = conf
    app['session'] = aiohttp.ClientSession()
    yield
    app['session'].close()


def main():
    app = web.Application()
    app.cleanup_ctx.append(init)

    web.run_app(app, port=conf['port'])


if __name__ == '__main__':
    main()
