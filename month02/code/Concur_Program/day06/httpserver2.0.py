"""
    http_server V2.0
    1. 主要功能 ：
   【1】 接收客户端（浏览器）请求.
   【2】 解析客户端发送的请求.
   【3】 根据请求组织数据内容.
   【4】 将数据内容形成http响应格式返回给浏览器.

    2. 升级点 ：
   【1】 采用IO并发，可以满足多个客户端同时发起请求情况.
   【2】 做基本的请求解析，根据具体请求返回具体内容，同时满足客户端简单的非网页请求情况.
   【3】 通过类接口形式进行功能封装.

   技术分析：
       1. 使用tcp通信，基于http协议
       2. 使用 select io 多路复用

   结构：
       采用各类封装

   类的接口设计：
       1. 在用户的角度进行流程设计
         * 当需要完成的功能是一个比较大的概括的功能,可以提供继承方法，让别人使用时继承你的类

         * 针对一个非常具体的功能，尽量帮用户实现更多功能，让用户尽可能少的修改代码或尽可能简单使用

         * 不能够替用户决定的属性，让用户传参

         * 不能替用户决定的复杂功能，让用户重写

       2. 确定功能，参数，使用方法
"""

from socket import *
from select import select


# 具体功能实现
class HTTPServer:
    def __init__(self, addr=("0.0.0.0", 8000), dir=None):
        self.addr = addr
        self.dir = dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        # 创建套接字
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.rlist.append(self.sockfd)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.addr)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("listen the port %d" % self.addr[1])
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            print("=============")
            print(rs)
            self.do_rlist(rs)

    def do_rlist(self, rs):
        for r in rs:
            if r is self.sockfd:
                c, addr = r.accept()
                print("connect from", addr)
                self.rlist.append(c)  # 增加新的 IO 关注
            else:
                self.handle(r)

    def handle(self, connfd):
        # 有客户端发消息
        data = connfd.recv(4096)
        if not data:
            self.rlist.remove(connfd)  # 取消对客户端关注
            connfd.close()
            return
        # 提取请求内容，将字节串串安航切割
        request_line = data.splitlines()[0]
        info = request_line.decode().split(" ")[1]

        # 根据请求内容进行数据整理
        # 分为两类 1.请求网页 2.其他
        if info == "/" or info[-5:] == ".01-html":
            self.get_html(connfd, info)
        else:
            self.get_other(connfd)

    # 返回网页
    def get_html(self, connfd, info):
        if info == "/":
            filename = self.dir + "/index.01-html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/01-html\r\n"
            response += "\r\n"
            response += '<h1>Sorry</h1>'
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/01-html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    # 返回其他
    def get_other(self, connfd):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/01-html\r\n"
        response += "\r\n"
        response += "<h1>wait for http_server3.0</h1>"

        # 将响应发送给浏览器
        connfd.send(response.encode())


# 用户使用 HTTPServer
if __name__ == "__main__":
    """
        通过 HTTPServer 类快速搭建服务，展示自己的网页
    """

    ADDR = ("0.0.0.0", 8888)
    DIR = "./static"  # 网页存储位置

    httpd = HTTPServer(ADDR, DIR)
    httpd.serve_forever()
