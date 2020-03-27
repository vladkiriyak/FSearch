import pytest
from aiohttp import web, ClientSession
from config import conf
from src import routes

pytest_plugins = [
]


@pytest.yield_fixture()
def main_app():
    app = web.Application()
    app.add_routes(routes.routes)
    app['config'] = conf
    app['session'] = ClientSession()

    yield app
    app['session'].close()
