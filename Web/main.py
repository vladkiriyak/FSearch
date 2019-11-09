import aiohttp_jinja2
import jinja2
from aiohttp import web
import logging

import routes


async def init_app():
    app = web.Application()
    app.add_routes(routes.routes)

    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader(package_name="main", package_path="templates"))
    app.router.add_static('/static/', path='./static', name='static')

    logging.basicConfig(level=logging.DEBUG)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
