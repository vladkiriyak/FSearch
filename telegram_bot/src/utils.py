from aiohttp.web_request import Request

import requests


def set_webhook(app):
    requests.get(
        f"https://api.telegram.org/bot{app['config']['token']}/setWebhook?url={app['config']['tunneling_url']}")


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


async def send_telegram_message(app, user_id: int, message: str):
    async with app['session'].get(
            f"{app['config']['URL']}/sendMessage?chat_id={user_id}&text={message}"
    ) as response:
        pass
