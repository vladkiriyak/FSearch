from aiohttp.web_request import Request


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

        docs = list(map(lambda doc: doc['_source'], elastic_response["hits"]["hits"]))

    return docs


async def get_file(request: Request):
    file_id: str = request.rel_url.query['file_id']

    json_search_query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"file_id": file_id}},

                ]
            }
        }

    }

    async with request.app['session'].get(
            'http://localhost:9200/_search',
            json=json_search_query
    ) as response:
        elastic_response = await response.json()

        doc = elastic_response["hits"]["hits"][0]['_source']

    return doc
