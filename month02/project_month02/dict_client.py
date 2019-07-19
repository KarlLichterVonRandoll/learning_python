"""
    dict 客户端
    功能：根据用户输入发送请求，得到结果
         一级：注册、登录、退出
         二级：查单词、历史记录、注销

"""

from socket import *
import sys, getpass

# 全局变量
HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST, PORT)


# 查单词处理函数
def do_search(name):
    while True:
        word = input("输入单词:")
        if word == "##":  # 结束单词查询
            break
        msg = "S %s %s" % (name, word)
        s.send(msg.encode())  # 发送请求
        data = s.recv(2048).decode()  # 得到查询结果
        print(data)


def do_history():
    pass


# 二级界面, 登陆后的状态
def logined(name):
    while True:
        print("""
    =========Welcome=========
    1.查单词  2.历史记录  3.注销
    =========================
        """)
        cmd = input("输入选项:")
        if cmd == "1":
            do_search(name)
        elif cmd == "2":
            do_history()
        elif cmd == "3":
            break
        else:
            print("请输入正确选项")


# tcp 套接字
s = socket()
s.connect(ADDR)


# 处理注册函数
def do_register():
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd1 = getpass.getpass("Confirm:")
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        if " " in name or " " in passwd:
            print("用户名和密码不能有空格!")
            continue
        msg = "R %s %s" % (name, passwd)
        s.send(msg.encode())  # 发送给服务器
        data = s.recv(1024).decode()  # 接收结果
        if data == "OK":
            print("注册成功!")
            logined(name)
        else:
            print("注册失败!")
        return


# 处理登录函数
def do_login():
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())  # 发送给服务器
    data = s.recv(1024).decode()  # 接收结果
    if data == "OK":
        print("登录成功!")
        logined(name)
    else:
        print("登录失败!")


# 搭建网络连接
def main():
    while True:
        print("""
    =========Welcome========
    1.注册    2.登录    3.退出
    ========================
        """)
        cmd = input("输入选项:")
        if cmd == "1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b"E")
            sys.exit("客户端退出")
        else:
            print("请输入正确选项")


if __name__ == "__main__":
    main()
