import json

import client_utils

from aiohttp import web
import logging

from utils import set_webhook


async def init_app():
    app = web.Application()
    app.add_routes(client_utils.routes)
    app['config'] = {}

    await set_webhook()

    logging.basicConfig(level=logging.DEBUG)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
