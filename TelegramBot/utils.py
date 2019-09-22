import os

import aiofiles as aiof
from aiohttp import ClientResponse
from aiohttp_requests import requests
from upload_config import config


async def set_webhook():
    await requests.get(f"https://api.telegram.org/bot{config['token']}/setWebhook?url={config['tunneling_url']}")


async def get_file_content(file_id: int):
    from upload_config import config

    file_info_response: ClientResponse = await requests.get(f"{config['URL']}/getfile?file_id={file_id}")
    file_info: dict = await file_info_response.json()
    file_path = file_info['result']['file_path']

    file_content: bytes = await (await requests.get(
        f"https://api.telegram.org/file/bot{config['token']}/{file_path}")).read()

    return file_content.decode(encoding='utf-8', errors='ignore')


async def create_telegraph_page(title: str, body: str) -> str:
    content = '[{"tag":"p","children":["' + body + '"]}]'

    page_url = (await (
        await requests.get(
            "https://api.telegra.ph/createPage? " +
            f"access_token={config['telegraph_access_token']}" +
            f"&title={title}" +
            f"&content={content}"
        )
    ).json())['result']['url']

    return page_url


async def indexing_file(user_id: int, file_name: str, file_content: str):
    indexing_json = {
        'user_id': user_id,
        'file_name': file_name,
        'file_content': file_content
    }
    await requests.post(f'http://localhost:9200/documents/doc', json=indexing_json)


async def send_telegram_message(user_id: int, message: str):
    await requests.get(f"{config['URL']}/sendMessage?chat_id={user_id}&text={message}")


async def save_file(user_id: int, file_name: str, file_content: str):
    if str(user_id) not in os.listdir("/home/vlad/FSearch/DocumentStorage"):
        os.system(f"mkdir /home/vlad/FSearch/DocumentStorage/{user_id}")

    async with aiof.open(f"/home/vlad/FSearch/DocumentStorage/{user_id}/{file_name}", mode='w') as file:
        await file.write(file_content)
        await file.flush()


async def get_message_type(request: dict):
    if "message" in request.keys():
        if "document" in request['message'].keys():
            return "document"
        elif "text" in request['message'].keys():
            return "text"
    else:
        return None
