import socket


def server_func():
    # 1.创建套接字
    sockfd = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # 2.绑定地址
    sockfd.bind(("127.0.0.1", 8888))

    # 3.接收消息
    data, addr = sockfd.recvfrom(500)

    print("receive from", addr)

    print(data.decode())

    # 4.发送消息
    msg = "welcome"
    sockfd.sendto(msg.encode(), addr)

    # 4.关闭套接字
    sockfd.close()


if __name__ == "__main__":
    print("start recv...")
    server_func()
