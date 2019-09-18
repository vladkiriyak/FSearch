from aiohttp import web
from aiohttp.web_request import Request

from utils import get_message_type, get_file_content, upload_file

routes = web.RouteTableDef()


@routes.post('/')
async def main(request: Request):
    request: dict = await request.json()
    message_type = await get_message_type(request)

    if message_type == "text":
        user_id = request['message']['from']['id']
        text = request['message']['text']

        if text == '/search':
            print("Поиск")


    elif message_type == "document":
        file_content = await get_file_content(request['message']['document']['file_id'])

        await upload_file(
            request['message']['from']['id'],
            request['message']['document']['file_name'],
            file_content
        )

    return web.Response(text='ok')
