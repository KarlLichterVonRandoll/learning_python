"""
    客户端
"""

from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ADDR = ("127.0.0.1", 8888)
s.connect(ADDR)

while True:
    print("""
       一级界面
    ============
    1.注册 2.登录
    ============
    """)
    cmd = input("输入命令")
    s.send(cmd.encode())

    data = s.recv(1024).decode()

    if data == "ok":
        name = input("输入用户名:")
        passwd = input("输入密码:")
        msg = name.strip() + "," + passwd.strip()
        s.send(msg.encode())
        response = s.recv(1024).decode()
        print(response)
    else:
        print(data)

