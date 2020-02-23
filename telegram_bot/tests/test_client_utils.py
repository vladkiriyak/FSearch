from aiohttp import web

from src.client_utils import hello


async def test_hello(aiohttp_client, loop, my_fixture):
    app = web.Application()
    app.router.add_get('/', hello)

    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello' in text
