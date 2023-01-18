import os
import shutil

# 初始化
def inits():
    # 检查CONF文件夹中是否有文件，如果没有则从init文件夹中复制
    if bool(os.listdir("conf")) == False:
        # 获取init_conf文件夹中的文件
        init_conf = os.listdir("init_conf")
        # 遍历复制文件
        for i in init_conf:
            shutil.copyfile("init_conf/" + i, "conf/" + i)
        print("初始化完成,退出")
        exit(0)


if __name__ == "__main__":
    inits()
    from threading import Thread
    from sanic import Sanic
    from web import web

    app = Sanic("app")
    app.blueprint(web)
    app.run(host="0.0.0.0", port=8000, debug=True, workers=4)
