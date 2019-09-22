f = {'took': 1, 'timed_out': False, '_shards': {'total': 4, 'successful': 4, 'skipped': 0, 'failed': 0},
     'hits': {'total': {'value': 3, 'relation': 'eq'}, 'max_score': 0.3438858, 'hits': [
         {'_index': '1234', '_type': 'doc', '_id': '1', '_score': 0.3438858,
          '_source': {'data': '19', 'text': 'Мама кушает салат'}},
         {'_index': '1234', '_type': 'doc', '_id': '2', '_score': 0.3438858,
          '_source': {'data': '19', 'text': 'Папа кушает курицу'}},
         {'_index': '1234', '_type': 'doc', '_id': '3', '_score': 0.3438858,
          '_source': {'data': '19', 'text': 'Сын кушает шоколад'}}]}}
fg = {
    "took": 0,
    "timed_out": False,
    "_shards": {
        "total": 4,
        "successful": 4,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 3,
            "relation": "eq"
        },
        "max_score": 0.3438858,
        "hits": [
            {
                "_index": "1234",
                "_type": "doc",
                "_id": "1",
                "_score": 0.3438858,
                "_source": {
                    "data": "19",
                    "text": "Мама кушает салат"
                }
            },
            {
                "_index": "1234",
                "_type": "doc",
                "_id": "2",
                "_score": 0.3438858,
                "_source": {
                    "data": "19",
                    "text": "Папа кушает курицу"
                }
            },
            {
                "_index": "1234",
                "_type": "doc",
                "_id": "3",
                "_score": 0.3438858,
                "_source": {
                    "data": "19",
                    "text": "Сын кушает шоколад"
                }
            }
        ]
    }
}

