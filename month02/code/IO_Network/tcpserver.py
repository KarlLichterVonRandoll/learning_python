import socket


def server_func():
    # 1.创建套接字
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 2.绑定地址
    sock.bind(("127.0.0.1", 8888))

    # 3.设置监听
    sock.listen(10)

    while True:
        # 4.等待客户端连接请求
        connfd, addr = sock.accept()
        print("receive from", addr)

        # 5.接收消息
        msg = connfd.recv(500)
        print(msg.decode())
        print(type(msg))

        # 6.发送消息
        str01 = "welcome"
        connfd.send(str01.encode())

        # 7.关闭连接通路
        connfd.close()


if __name__ == "__main__":
    print("start listening...")
    server_func()
