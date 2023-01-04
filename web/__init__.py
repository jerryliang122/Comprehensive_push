# web/__init__.py
from sanic import Blueprint
from .wechat import wechat

web = Blueprint.group(wechat, url_prefix="/wechat")
