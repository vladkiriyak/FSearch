from aiohttp import web
from aiohttp.web_request import Request
from docx import Document, document
from io import BytesIO

from src.utils import es_search

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.get('/search')
async def search(request: Request):
    search_query: str = request.rel_url.query['search_query']

    file_content = await es_search(request)

    return web.json_response(
        {
            "search_words": search_query.split(),
            "file_content": file_content
        }

    )
