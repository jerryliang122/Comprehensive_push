from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def web():
    # 接入入口文件
    from web.app import main

    main()


if __name__ == "__main__":
    # 多进程
    with ProcessPoolExecutor() as executor:
        executor.submit(web)

    # 多线程
    # with ThreadPoolExecutor() as executor:
    #     executor.submit(web)
    #     executor.submit(web)
