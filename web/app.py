from sanic import Sanic
from web.wechat import wechat

app = Sanic("My app")

app.blueprint(wechat)
