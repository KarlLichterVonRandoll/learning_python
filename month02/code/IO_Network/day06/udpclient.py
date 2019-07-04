import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("msg>>")
    sockfd.sendto(msg.encode(), ("176.23.4.104", 8768))

    data, addr = sockfd.recvfrom(1024)

    print(data.decode())

sockfd.close()
