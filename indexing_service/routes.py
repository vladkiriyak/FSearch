import aiohttp
from aiohttp import web
from aiohttp.web_request import Request

from docx import Document, document
from io import BytesIO

from aiohttp.client_reqrep import ClientResponse

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.post('/indexing')
async def indexing(request: Request):
    user_id: int = int(request.rel_url.query['user_id'])
    file_id: str = request.rel_url.query['file_id']
    file_name: str = request.rel_url.query['file_name']

    # file_id = 'BQADAgADuAUAAl51sUgh15w__uncFRYE'

    url = f"{request.app['config']['URL']}/getfile?file_id={file_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file_path = (await response.json())['result']['file_path']
        url = f"https://api.telegram.org/file/bot{request.app['config']['token']}/{file_path}"

        async with session.get(url) as response:
            source_stream = BytesIO(await response.content.read())
            doc: document.Document = Document(source_stream)

        file_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

        indexing_json = {
            'user_id': user_id,
            'file_id': file_id,
            'file_name': file_name,
            'file_content': file_content
        }

        async with session.post(f'http://localhost:9200/fsearch/doc', json=indexing_json) as response:
            response: ClientResponse
            print(await response.json())

    return web.Response(text='ok')
