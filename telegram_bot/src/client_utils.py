from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_requests import requests

from src.messages import get_message_type
from .utils import send_telegram_message, processing_text_message, processing_document_message

from log import loging

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello")


@routes.post('/')
async def telegram_handler(request: Request):
    request_json: dict = await request.json()
    message_type = get_message_type(request_json)

    username = request_json['message']['from'].get('username')
    user_message = request_json['message'].get('text')
    user_id = request_json['message']['from'].get('id')

    if message_type == "text":

        await loging.put_log_in_file(f" | {user_id} | {username} | {user_message}")

        await processing_text_message(request, request_json)

    elif message_type == "document":

        await loging.put_log_in_file(f" | {username} | UPLOAD FILE")

        try:
            await processing_document_message(requests, request_json)
        except Exception as exception:

            print(f"\x1b[0;31;48m{exception}\x1b[0m")

            await send_telegram_message(
                request.app,
                request_json['message']['from']['id'],
                "Данный формат файла не доступен"
            )

    return web.Response(text='ok')
