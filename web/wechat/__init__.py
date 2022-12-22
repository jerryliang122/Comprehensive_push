from sanic import Blueprint
from web.wechat import receive

api = Blueprint.group(receive, url_prefix="/wechat")
