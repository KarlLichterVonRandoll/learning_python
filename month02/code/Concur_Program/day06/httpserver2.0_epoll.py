from socket import *
from select import *


# 具体功能实现
class HTTPServer:
    def __init__(self, addr=("0.0.0.0", 8000), dir=None):
        self.addr = addr
        self.dir = dir
        self.create_socket()
        self.bind()
        self.fnmap = {self.sockfd.fileno(): self.sockfd}
        self.ep = epoll()

    # 创建套接字
    def create_socket(self):
        # 创建套接字
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.ep.register(self.sockfd, EPOLLIN | EPOLLERR)  # EPOLLIN = 1  EPOLLERR = 8

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.addr)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("listen the port %d" % self.addr[1])
        while True:
            events = self.ep.poll()  # 阻塞等待监控的IO事件发生
            # print(events)  # [(fileno,event),()....]
            # 循环遍历列表，查看哪个 IO 就绪，进行处理
            for fn, event in events:
                # 区分哪个 IO 就绪
                if fn == self.sockfd.fileno():
                    c, addr = self.fnmap[fn].accept()
                    print("connect from", addr)
                    # 关注客户端套接字
                    self.ep.register(c, EPOLLIN | EPOLLERR)
                    self.fnmap[c.fileno()] = c  # 维护字典
                # 判断是否是 EPOLLIN 就绪，EPOLLIN = 1, EPOLLERR = 8
                # EPOLLIN & EPOLLIN = 1, EPOLLERR & EPOLLIN = 0
                elif event & EPOLLIN:
                    self.handle(self.fnmap[fn])

                    data = self.fnmap[fn].recv(1024).decode()
                    if not data:
                        self.ep.unregister(fn)  # 取消关注
                        self.fnmap[fn].close()
                        del self.fnmap[fn]
                        continue
                    print(data)
                    self.fnmap[fn].send(b"OK")


    def handle(self, fn):
        # 有客户端发消息
        data = self.fnmap(fn).recv(4096)
        if not data:
            self.ep.unregister(fn)  # 取消关注
            self.fnmap[fn].close()
            del self.fnmap[fn]
            return
        # 提取请求内容，将字节串串安航切割
        request_line = data.splitlines()[0]
        info = request_line.decode().split(" ")[1]

        # 根据请求内容进行数据整理
        # 分为两类 1.请求网页 2.其他
        if info == "/" or info[-5:] == ".html":
            self.get_html(self.fnmap(fn), info)
        else:
            self.get_other(self.fnmap(fn))

    # 返回网页
    def get_html(self, connfd, info):
        if info == "/":
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += '<h1>Sorry</h1>'
        else:
            # 网页存在
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    # 返回其他
    def get_other(self, connfd):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
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