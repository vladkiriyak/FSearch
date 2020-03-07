from aiohttp import web, ClientSession


async def test_elasticsearch_connection():
    async with ClientSession() as session:
        async with session.get('http://localhost:9200/') as resp:
            assert resp.status == 200

# async def test_hello(main_app, aiohttp_client):
#     client = await aiohttp_client(main_app)
#
#     resp = await client.get('/')
#     assert resp.status == 200
#     text = await resp.text()
#     assert 'Hello, world' in text
#
