"""
    接收端 客户端
    1.创建UDP套接字
    2.设置套接字可以发送接受广播 setsockopt
    3.选择接受的端口
"""
from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sockfd.bind(("0.0.0.0", 9876))

while True:
    data, addr = sockfd.recvfrom(1024)

    print(addr)
    print(data.decode())
