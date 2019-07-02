import socket


def client_func():
    # 1.创建套接字
    socker = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 2.请求连接
    socker.connect(("127.0.0.1", 8888))

    # 3.收发消息
    msg = "hello"
    socker.send(msg.encode())

    rst = socker.recv(500)
    print(type(rst))
    print(rst.decode())

    # 4.关闭套接字
    socker.close()


if __name__ == "__main__":
    client_func()
