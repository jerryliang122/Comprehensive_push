from sanic import Sanic
from web.wechat import wechat


def main():
    app = Sanic()
    app.blueprint(wechat)
    app.run(host="127.0.0.1", port=8000)
