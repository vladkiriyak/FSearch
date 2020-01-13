import client_utils

from aiohttp import web
import logging

from utils import set_webhook, get_config


def init(app):
    app.add_routes(client_utils.routes)
    app['config'] = get_config('config.json')

    logging.basicConfig(level=logging.DEBUG)
    set_webhook(app)


def main():
    app = web.Application()
    init(app)
    web.run_app(app, port=app['config']['port'])


if __name__ == '__main__':
    main()
