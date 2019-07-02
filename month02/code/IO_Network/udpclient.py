import socket


def client_func():
    sockfd = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    msg = "good night"

    sockfd.sendto(msg.encode(), ("127.0.0.1", 8888))

    data, addr = sockfd.recvfrom(500)
    print(data.decode())
    print(addr)

    sockfd.close()


if __name__ == "__main__":
    client_func()
