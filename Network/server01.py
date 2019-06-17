import socket

'''
Server端流程
 1. 建立socket，socket是负责具体通信的一个实例
 2. 绑定，为创建的socket指派固定的端口和ip地址
 3. 接受对方发送内容
 4. 给对方发送反馈，此步骤为非必须步骤
'''


def serverfunc():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr01 = ("127.0.0.1", 7852)
    server.bind(addr01)

    data, addr02 = server.recvfrom(500)

    print(data)
    print(type(data))

    text = data.decode()
    print(type(text))
    print(text)

    rsp = "Ich hab keine Hunge"

    data = rsp.encode()
    server.sendto(data, addr02)


if __name__ == "__main__":
    print("Starting server.........")
    serverfunc()
    print("Ending server.........")
