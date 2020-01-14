from aiohttp import web
from aiohttp.web_request import Request
from docx import Document, document
from io import BytesIO

from utils import docx_to_html

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.get('/search')
async def search(request: Request):
    user_id: str = request.rel_url.query['user_id']
    search_query: str = request.rel_url.query['search_query']

    json_search_query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"file_content": search_query}},
                    {"term": {"user_id": user_id}}
                ]
            }
        }
    }

    async with request.app['session'].get(
            'http://localhost:9200/_search',
            json=json_search_query
    ) as response:
        elastic_response = await response.json()

        file_id = elastic_response["hits"]["hits"][0]["file_id"]

        url = f"{request.app['config']['URL']}/getfile?file_id={file_id}"

        async with request.app['session'].get(url) as response:
            file_path = (await response.json())['result']['file_path']
        url = f"https://api.telegram.org/file/bot{request.app['config']['token']}/{file_path}"

        async with request.app['session'].get(url) as response:
            source_stream = BytesIO(await response.content.read())
            doc: document.Document = Document(source_stream)
            html_content = docx_to_html(doc)

    return web.Response(text=html_content)
