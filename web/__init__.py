# web/__init__.py
from sanic import Blueprint
from .wechat import wechat

api = Blueprint.group(wechat, url_prefix="/wechat")
