import aiohttp
from aiohttp import web
from aiohttp.web_request import Request
from .utils import get_file_url, get_file_content, es_save
routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.post('/indexing')
async def indexing(request: Request):
    file_url = await get_file_url(request)
    file_content = await get_file_content(request, file_url)
    await es_save(request, file_content)
    return web.Response(text='ok')
