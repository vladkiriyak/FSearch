from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_jinja2 import template

routes = web.RouteTableDef()


@routes.get("/")
@template("search_page.html")
async def get_document(request: Request):

    return {'body': "hello"}


@routes.get("/getDocument")
@template("search_page.html")
async def get_document(request: Request):
    print("!" * 20)
    try:
        print(request.rel_url.query['search_query'])
    except:
        pass
    print("!" * 20)

    return {'body': "hello"}
