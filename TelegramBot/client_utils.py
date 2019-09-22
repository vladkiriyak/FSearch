from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_requests import requests

from utils import get_message_type, get_file_content, save_file, indexing_file, create_telegraph_page, \
    send_telegram_message

routes = web.RouteTableDef()


@routes.get('/')
async def ff(request):
    return web.Response(text="eeeeeeeeeeeeeeeee")


@routes.post('/')
async def telegram_handler(request: Request):
    request: dict = await request.json()
    message_type = await get_message_type(request)

    if message_type == "text":
        user_id = request['message']['from']['id']
        text = request['message']['text']

        if text[:7] == '/search':
            search_query = ({"query": {"term": {"text": text[8:]}}})

            elastic_response = await (await requests.get('http://localhost:9200/_search', json=search_query)).json()

            page_url = await create_telegraph_page(
                "Hello, VLad",
                elastic_response["hits"]["hits"][0]['_source']['text']
            )

            await send_telegram_message(request['message']['from']['id'], page_url)

    elif message_type == "document":
        file_content = await get_file_content(request['message']['document']['file_id'])

        await indexing_file(
            request['message']['from']['id'],
            request['message']['document']['file_name'],
            file_content
        )
        await save_file(
            request['message']['from']['id'],
            request['message']['document']['file_name'],
            file_content
        )

    return web.Response(text='ok')
