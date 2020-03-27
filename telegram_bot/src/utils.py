from aiohttp.web_request import Request

import requests


def set_webhook(conf):
    requests.get(
        f"https://api.telegram.org/bot{conf['token']}/setWebhook?url={conf['tunneling_url']}")


async def processing_text_message(request: Request, json_request: dict):
    user_id = json_request['message']['from']['id']
    text = json_request['message']['text']

    if text[:8] != '/search ':
        await send_telegram_message(
            request, json_request['message']['from']['id'],
            "Для поиска введите: '/search  ваш поисковый запрос'"
        )
    else:
        await send_telegram_message(
            request, json_request['message']['from']['id'],
            "http://localhost:8080/search/doc?file_id="
        )


async def processing_document_message(request: Request, json_request: dict):
    url = f"http://0.0.0.0:8001/indexing" \
          f"?user_id={json_request['message']['from']['id']}&" \
          f"file_id={json_request['message']['document']['file_id']}&" \
          f"file_name={json_request['message']['document']['file_name']}"

    async with request.app['session'].post(url) as response:
        if response.status == 200:
            await send_telegram_message(
                request, json_request['message']['from']['id'],
                "Загрузка файла прошла успешно"
            )
        else:
            await send_telegram_message(
                request, json_request['message']['from']['id'],
                "Данный формат файла не поддерживается"
            )


async def send_telegram_message(request, user_id: int, message: str):
    async with request.app['session'].get(
            f"{request.app['config']['URL']}/sendMessage?chat_id={user_id}&text={message}"
    ) as response:
        pass
