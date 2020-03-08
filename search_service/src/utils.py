from aiohttp import web
from aiohttp.web_request import Request
from docx import Document, document
from io import BytesIO


async def es_search(request: Request):
    user_id: str = request.rel_url.query['user_id']
    search_query: str = request.rel_url.query['search_query']
    json_search_query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"file_content": search_query}},
                    {"term": {"user_id": user_id}}
                ]
            }
        }
    }

    async with request.app['session'].get(
            'http://localhost:9200/_search',
            json=json_search_query
    ) as response:
        elastic_response = await response.json()

        file_content = elastic_response["hits"]["hits"][0]["file_content"]

    return file_content
