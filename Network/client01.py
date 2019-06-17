import socket


def clientfunc():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "hello"

    data = text.encode()

    client.sendto(data, ("127.0.0.1", 7852))

    data, addr = client.recvfrom(200)

    data = data.decode()

    print(data)


if __name__ == "__main__":
    clientfunc()
