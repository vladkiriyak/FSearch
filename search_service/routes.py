import aiohttp
from aiohttp import web
from aiohttp.web_request import Request

routes = web.RouteTableDef()


@routes.get('/')
async def main(request: Request):
    return web.Response(text="Ok")


@routes.get('/search')
async def search(request: Request):
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

    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:9200/_search', json=json_search_query) as response:
            elastic_response = await response.json()

    return web.json_response(elastic_response)
