import socket


def server_func():
    # 1.创建套接字, 使用ipv4协议, 使用数据流形式传输
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 2.绑定地址
    sock.bind(("127.0.0.1", 8887))

    # 3.设置监听, 队列大小
    sock.listen(100)

    while True:
        # 4.等待客户端连接请求
        print("start listening...")
        try:
            connfd, addr = sock.accept()
            print("receive from", addr)
        except KeyboardInterrupt:
            print("服务器退出")
            break
        except Exception as e:
            print(e)
            continue

        f = open("img02.jpg", "wb")

        while True:
            # 5.接收消息, 设置每次最多接收的字节大小
            data = connfd.recv(1024)
            if not data:
                break
            f.write(data)
        f.close()

        connfd.close()


if __name__ == "__main__":
    server_func()
