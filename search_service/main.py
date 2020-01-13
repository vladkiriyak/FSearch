import routes

from aiohttp import web
import logging

from utils import get_config


def init(app):
    app.add_routes(routes.routes)
    app['config'] = get_config('config.json')
    logging.basicConfig(level=logging.DEBUG)


def main():
    app = web.Application()
    init(app)
    web.run_app(app, port=app['config']['port'])


if __name__ == '__main__':
    main()
