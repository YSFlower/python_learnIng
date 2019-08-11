#多线程demo
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 2)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    threads = []
    # 创建10个下载的线程
    for _ in range(10):
        t = Thread(target=download, args=('Python从入门到住院'+str(_)+'.pdf',))
        threads.append(t)
        t.start()
    # 等所有线程都执行完毕
    for t in threads:
        t.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()