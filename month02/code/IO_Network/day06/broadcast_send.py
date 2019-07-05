"""
    发送端 服务端
    1. 创建UDP套接字
    2. 设置可以发送广播 setsockopt
    3. 循环向广播地址发送
"""

from socket import *
import time

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    msg = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(2)
    sockfd.sendto(msg.encode(), ("176.23.4.255", 9876))
