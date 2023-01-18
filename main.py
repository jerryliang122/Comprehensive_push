from threading import Thread
from sanic import Sanic
from web import web
import os
import shutil

# 初始化
def inits():
    # 检查CONF文件夹中是否有文件，如果没有则从init文件夹中复制
    if bool(os.listdir("conf")) == False:
        shutil.copytree("init_conf/*", "conf/*")
        print("初始化完成,退出")
        exit(0)


if __name__ == "__main__":
    inits()
    app = Sanic("app")
    app.blueprint(web)
    app.run(host="0.0.0.0", port=8000, debug=True, workers=4)
