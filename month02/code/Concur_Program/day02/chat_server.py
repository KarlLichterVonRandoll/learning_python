"""
    服务端
    接受请求，分类：
                 进入：维护一个用户信息
                 离开：
                 聊天：将信息发送给其他用户
"""

from socket import *
import os, sys

# 定义全局变量
ADDR = ("0.0.0.0", 9527)  # 服务器地址
user = {}  # 存储用户 {name:address}


# 处理进入聊天室请求
def do_login(s, name, addr):
    if name in user or "管理员" in name:
        s.sendto("用户已存在".encode(), addr)
        return
    s.sendto(b"OK", addr)

    # 通知其他人
    msg = "欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])

    # 将新用户插入字典
    user[name] = addr


# 处理聊天请求
def do_chat(s, name, msg):
    msg = name + ":" + msg
    for i in user:
        s.sendto(msg.encode(), user[i])


# 处理退出请求
def do_exit(s, name):
    msg = "%s 退出了聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b"EXIT", user[i])

    del user[name]


# 请求处理函数
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(" ")
        # 根据不同请求类型具体执行不同事情
        # L 进入  C 聊天  D 退出
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)  # 执行具体工作
        elif tmp[0] == "C":
            text = " ".join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == "Q":
            do_exit(s, tmp[1])


# 搭建网络
def main():
    s = socket(AF_INET, SOCK_DGRAM)

    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        sys.exit()
    elif pid == 0:
        while True:
            text = input("管理员消息")
            msg = "C 管理员 "+text
            s.sendto(msg.encode(), ADDR)
    else:
        do_request(s)


if __name__ == "__main__":
    main()
