"""
    HTTPServer 部分主程序
      获取 http 请求
      解析 http 请求
      将请求发送给 WebFrame
      从 WebFrame 接收反馈数据
      将数据组织为 Response 格式发送给客户端
"""

from socket import *
import sys, re
import json
from threading import Thread
from config import *

# global argument
ADDR = (HOST, PORT)


# communicate with webframe
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return
    # convert dict to　JSON
    data = json.dumps(env)
    # 将解析后的请求发送给　webframe
    s.send(data.encode())
    # receive data from webframe
    data = s.recv(4096 * 100).decode()
    return json.loads(data)


# 将 httpserver 基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket()  # 和浏览器交互
        # self.connect_socket()  # 连接 webframe
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # handle request from client
    def handle(self, c):
        request = c.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except Exception:
            # 客户端断开
            c.close()
            return
        else:
            data = connect_frame(env)
            self.response(c, data)

    # send message to browser/client
    def response(self, c, data):
        # data => {'status': '200', 'data': 'xxxxxx'}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '500':
            pass
            # 给浏览器发送数据
        response_data = responseHeaders + responseBody
        c.send(response_data.encode())

    # Start service
    def serve_forever(self):
        self.sockfd.listen(5)
        print("listen the port %d" % self.port)
        while True:
            c, addr = self.sockfd.accept()
            print("connect from", addr)
            client = Thread(target=self.handle, args=(c,))
            client.setDaemon(True)
            client.start()


if __name__ == "__main__":
    httpd = HTTPServer()
    httpd.serve_forever()
