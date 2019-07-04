import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sockfd.bind(("0.0.0.0", 8768))
while True:
    data, addr = sockfd.recvfrom(5)

    print("收到消息", data.decode())

    n = sockfd.sendto(b"welcome", addr)

# sockfd.close()
