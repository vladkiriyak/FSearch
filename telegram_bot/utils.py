import base64
import json
import os

import aiofiles as aiof
import aiohttp
import textract
from aiohttp import ClientResponse
from aiohttp.web_request import Request

import requests


def set_webhook(app):
    requests.get(
        f"https://api.telegram.org/bot{app['config']['token']}/setWebhook?url={app['config']['tunneling_url']}")


#
# async def decode_document_bytes(content: bytes, user_id: int) -> str:
#     async with aiof.open(f"/home/vlad/FSearch/DocumentStorage/temp_file_{str(user_id)}.docx", mode='wb') as file:
#         await file.write(content)
#         await file.flush()
#
#     return textract.process(f"/home/vlad/FSearch/DocumentStorage/temp_file_{str(user_id)}.docx").decode()


# async def get_file_content(file_id: int, user_id: int) -> str:
#     file_info_response: ClientResponse = await requests.get(f"{app['config']['URL']}/getfile?file_id={file_id}")
#     file_info: dict = await file_info_response.json()
#     file_path = file_info['result']['file_path']
#
#     file_content: bytes = await (await requests.get(
#         f"https://api.telegram.org/file/bot{app['config']['token']}/{file_path}")).read()
#
#     return await decode_document_bytes(file_content, user_id)


# async def create_telegraph_page(title: str, body: str) -> str:
#     content = {
#         'access_token': app['config']["telegraph_access_token"],
#         'title': title,
#         'content': [{"tag": "p", "children": [body]}],
#     }
#
#     page_url = (await (
#         await requests.post(
#             "https://api.telegra.ph/createPage", json=content
#         )
#     ).json())['result']['url']
#
#     return page_url


# async def indexing_file(user_id: int, file_name: str, file_content: str):
#     indexing_json = {
#         'user_id': user_id,
#         'file_name': file_name,
#         'file_content': file_content
#     }
#     await requests.post(f'http://localhost:9200/my_index/doc', json=indexing_json)


async def processing_text_message(request: Request, json_request: dict):
    user_id = request['message']['from']['id']
    text = request['message']['text']

    if text[:8] != '/search ':
        await send_telegram_message(
            request, json_request['message']['from']['id'],
            "Для поиска введите: '/search  ваш поисковый запрос'"
        )
    else:
        await send_telegram_message(
            request, json_request['message']['from']['id'],
            "http://localhost:8080/search/user_id&search_query"
        )


async def processing_document_message(request: Request, json_request: dict):
    url = f"http://0.0.0.0:8001/indexing" \
          f"?user_id={request['message']['from']['id']}&" \
          f"file_id={request['message']['document']['file_id']}&" \
          f"file_name={request['message']['document']['file_name']}"

    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            print(await response.json())

    await send_telegram_message(
        request, json_request['message']['from']['id'],
        "Загрузка файла прошла успешно"
    )


async def send_telegram_message(app, user_id: int, message: str):
    await requests.get(f"{app['config']['URL']}/sendMessage?chat_id={user_id}&text={message}")


def get_config(path_to_config: str) -> dict:
    with open(path_to_config) as config_file:
        config = json.load(config_file)
    return config
