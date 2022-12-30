from threading import Thread


def web():
    # 接入入口文件
    from web.app import main

    main()


if __name__ == "__main__":
    web()
