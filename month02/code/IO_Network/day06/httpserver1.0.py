"""
    获取来自浏览器的请求
    判断如果请求是 index.html,则返回给客户端
    否则返回404
"""

from socket import *


def requests(c):
    # 获取请求将请求内容提取出来
    data = c.recv(4096).decode()
    print(data)
    # 防止浏览器异常退出
    if not data:
        return
    # 判断是 / 则返回 index.html, 不是则返回404
    if data.split(" ")[1] == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>404</h1>"
    c.send(response.encode())



tcpsocket = socket()

tcpsocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

tcpsocket.bind(("0.0.0.0", 8000))

tcpsocket.listen(10)

while True:
    c, addr = tcpsocket.accept()

    requests(c)


