"""
    基于threading的多线程网络并发
    实现步骤
    1. 创建监听套接字
    2. 循环接收客户端连接请求
    3. 当有新的客户端连接创建线程处理客户端请求
    4. 主线程继续等待其他客户端连接
    5. 当客户端退出，则对应分支线程退出
"""

from threading import Thread
from socket import *
import os

ADDR = ("0.0.0.0", 8888)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)
print("start listening...")


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break

        print(data.decode())
        c.send(b"OK")
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle, args=(c,))
    t.daemon = True
    t.start()
