# web/wechat/__init__.py
from sanic import Blueprint
from .receive import receive

wechat = Blueprint.group(receive, url_prefix="/wechat")
