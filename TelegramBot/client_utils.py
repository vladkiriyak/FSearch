from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_requests import requests

from utils import get_message_type, get_file_content, save_file, indexing_file, create_telegraph_page, \
    send_telegram_message, processing_document_message, processing_text_message

routes = web.RouteTableDef()


@routes.get('/')
async def ff(request):
    return web.Response(text="Hello")


@routes.post('/')
async def telegram_handler(request: Request):
    request: dict = await request.json()
    message_type = await get_message_type(request)

    if message_type == "text":
        await processing_text_message(request)

    elif message_type == "document":
        await processing_document_message(request)

    return web.Response(text='ok')
