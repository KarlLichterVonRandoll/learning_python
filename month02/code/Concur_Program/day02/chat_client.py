"""
    客户端
    两个进程：
      1. 发送进程，发送请求
      2. 接受进程
"""

from socket import *
import os, sys

# 服务器地址
ADDR = ("127.0.0.1", 9527)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input(">>")
        except KeyboardInterrupt:
            text = "quit"
        if text.strip() == "quit":
            msg = "Q %s" % name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")

        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


# 接受消息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(1024)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\n>>", end="")


def main():
    s = socket(AF_INET, SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入姓名>> ")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 接收服务器反馈
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    pid = os.fork()
    while True:
        if pid < 0:
            sys.exit("Error!")
        # 发送消息
        elif pid == 0:
            send_msg(s, name)
        # 接收消息
        else:
            recv_msg(s)

    # 退出


if __name__ == "__main__":
    main()
