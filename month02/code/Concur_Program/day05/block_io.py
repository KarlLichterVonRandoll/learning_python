"""
    socket 套接字非阻塞实例
"""

from socket import *
from time import ctime, sleep

# 日志文件
f = open("log.txt", "a+")

sockfd = socket()
sockfd.bind(("127.0.0.1", 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时阻塞
sockfd.settimeout(3)

while True:
    print("waiting for connect...")
    # 没有客户端连接，每隔三秒写一条日志
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    else:
        print("connect from", addr)
        data = connfd.recv(1024).decode()    # 此时connfd.recv 依然阻塞
        print(data)
