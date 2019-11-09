from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_requests import requests

from utils import get_message_type, get_file_content, save_file, indexing_file, create_telegraph_page, \
    send_telegram_message, processing_document_message, processing_text_message

from log import loging

routes = web.RouteTableDef()


@routes.get('/')
async def ff(request):
    return web.Response(text="Hello")


@routes.post('/')
async def telegram_handler(request: Request):
    request: dict = await request.json()
    message_type = await get_message_type(request)

    username = request['message']['from'].get('username')
    user_message = request['message'].get('text')
    user_id = request['message']['from'].get('id')

    if message_type == "text":

        await loging.put_log_in_file(f" | {user_id} | {username} | {user_message}")

        await processing_text_message(request)

    elif message_type == "document":

        await loging.put_log_in_file(f" | {username} | UPLOAD FILE")

        try:
            await processing_document_message(request)
        except Exception as exception:
            print(f"\x1b[0;31;48m{exception}\x1b[0m")
            await send_telegram_message(
                request['message']['from']['id'],
                "Sorry, we have problem with document processing"
            )

    return web.Response(text='ok')
