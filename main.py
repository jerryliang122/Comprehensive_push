from threading import Thread
from sanic import Sanic
from .web import web


if __name__ == "__main__":
    app = Sanic("app")
    app.blueprint(web)
