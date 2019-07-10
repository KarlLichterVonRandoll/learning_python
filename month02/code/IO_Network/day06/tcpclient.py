import socket


def client_func():
    sockfd = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    sockfd.connect(("127.0.0.1", 8887))

    f = open("img.jpg", "rb")
    while True:
        data = f.read(1024)
        if not data:
            break
        sockfd.send(data)

    f.close()

    sockfd.close()


if __name__ == "__main__":
    client_func()
