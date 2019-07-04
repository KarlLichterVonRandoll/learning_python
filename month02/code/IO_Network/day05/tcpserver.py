import socket


def server_func():
    # 1.创建套接字, 使用ipv4协议, 使用数据流形式传输
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 2.绑定地址
    sock.bind(("127.0.0.1", 8888))

    # 3.设置监听, 队列大小
    sock.listen(10)

    while True:
        # 4.等待客户端连接请求
        print("start listening...")
        connfd, addr = sock.accept()
        print("receive from", addr)

        # 5.接收消息, 设置每次最多接收的字节大小
        msg = connfd.recv(1024)
        print(type(msg))
        print(msg.decode())

        # 6.发送消息, 将字符串转换成字节流再发送, 返回发送的字节数
        str01 = b"welcome"
        n = connfd.send(str01)
        print("发送%d字节" % n)

        # 7.关闭连接通路
        connfd.close()


if __name__ == "__main__":
    server_func()
