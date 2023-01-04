from sanic import Sanic
from .web import web


def main():
    app = Sanic()
    app.blueprint(web)
    app.run(host="127.0.0.1", port=8000)
