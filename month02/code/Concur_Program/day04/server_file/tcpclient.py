"""
    tcp_client.py
"""

from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ADDR = ("127.0.0.1", 8888)

s.connect(ADDR)

while True:
    data = input(":")
    s.send(data.encode())

    msg = s.recv(1024)

    print(msg.decode())
