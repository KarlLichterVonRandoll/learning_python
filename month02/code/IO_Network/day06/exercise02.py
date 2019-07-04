"""
    UDP 查单词服务端
"""

import socket


def search(word):
    with open("dict.txt") as f:
        for line in f:
            w = line.split(" ")[0]
            if w > word:
                return "No Found"
            elif word == w:
                return line
        else:
            return "还没找到这个单词"


sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sockfd.bind(("127.0.0.1", 8888))

while True:
    data, addr = sockfd.recvfrom(1024)
    print("receive from", addr)

    msg = search(data.decode())

    n = sockfd.sendto(msg.encode(), addr)
