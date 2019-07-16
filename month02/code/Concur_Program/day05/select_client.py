"""
    select_client.py
"""

from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.connect(("127.0.0.1", 8888))

while True:
    msg = input(">>")
    s.send(msg.encode())

    data = s.recv(1024)

    print(data.decode())

