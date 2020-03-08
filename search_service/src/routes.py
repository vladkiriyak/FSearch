from aiohttp import web
from aiohttp.web_request import Request
from docx import Document, document
from io import BytesIO

from .utils import es_search, get_file

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.get('/doc')
async def search(request: Request):
    doc = await get_file(request)

    return web.json_response(
        {
            "doc": doc
        }

    )


@routes.get('/search')
async def search(request: Request):
    search_query: str = request.rel_url.query['search_query']

    docs = await es_search(request)

    return web.json_response(
        {
            "search_words": search_query.split(),
            "docs": docs
        }

    )
