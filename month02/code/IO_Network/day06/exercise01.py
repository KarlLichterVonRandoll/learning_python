"""
    使用UDP客户端查单词
"""

import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    word = input("word>> ")

    if word == "":
        break

    sockfd.sendto(word.encode(), ("127.0.0.1", 8888))

    data, addr = sockfd.recvfrom(1024)
    print(addr)

    print(data.decode())

sockfd.close()