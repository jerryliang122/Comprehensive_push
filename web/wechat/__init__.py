# web/wechat/__init__.py
from sanic import Blueprint
from .receive import receive

api = Blueprint.group(receive, url_prefix="/")
