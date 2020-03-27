from aiohttp.web_request import Request
import aiohttp
from aiohttp import web
from aiohttp.web_request import Request

from docx import Document, document
from io import BytesIO

from aiohttp.client_reqrep import ClientResponse

routes = web.RouteTableDef()


async def get_file_url(request: Request) -> str:
    file_id: str = request.rel_url.query['file_id']
    url = f"{request.app['config']['URL']}/getfile?file_id={file_id}"

    async with request.app['session'].get(url) as response:
        file_path = (await response.json())['result']['file_path']
    return f"https://api.telegram.org/file/bot{request.app['config']['token']}/{file_path}"


async def get_file_content(request: Request, file_url: str):
    async with request.app['session'].get(file_url) as response:
        source_stream = BytesIO(await response.content.read())
        doc: document.Document = Document(source_stream)

    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])


async def es_save(request: Request, file_content: str):
    user_id: int = int(request.rel_url.query['user_id'])
    file_id: str = request.rel_url.query['file_id']
    file_name: str = request.rel_url.query['file_name']

    doc_json = {
        'user_id': user_id,
        'file_id': file_id,
        'file_name': file_name,
        'file_content': file_content
    }

    async with request.app['session'].post(f'http://localhost:9200/fsearch/_doc', json=doc_json) as response:
        response: ClientResponse
        print(await response.json())
