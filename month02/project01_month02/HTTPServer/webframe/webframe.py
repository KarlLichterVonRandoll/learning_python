"""
    webframe.py  Simulate backend workflow

    Receive specific requests from httpserver
    Logic processing and data processing based on request
    Feedback the required data to httpserver
"""

from socket import *
import json
from settings import *
from select import select
from urls import *


# Application class, processing a request for a certain aspect
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind((frame_ip, frame_port))

    # start service
    def start(self):
        self.sockfd.listen(5)
        print("start listen app listen", frame_port)
        self.rlist.append(self.sockfd)
        # select listen
        while True:
            rs, ws, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    # 处理具体的　httpserver 请求
    def handle(self, c):
        request = c.recv(1024).decode()
        request = json.loads(request)
        # request => {'method':'GET', 'info':'/'}
        if request['method'] == 'GET':
            if request['info'][-5:] == '.html' or request['info'] == '/':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass

        response = json.dumps(response)
        c.send(response.encode())
        c.close()

    # 获取网页文件
    def get_html(self, info):
        if info == "/":
            filename = DIR + "/index.html"
        else:
            filename = DIR + info
        try:
            fd = open(filename)
        except Exception:
            fd = open(DIR + '/error.html')
            return {'status': '404', 'data': fd.read()}
        else:
            return {'status': '200', 'data': fd.read()}

    # 处理数据
    def get_data(self, info):
        for url, func in urls:
            if url == info:
                return {'status': '200', 'data': func()}
        return {'status': '404', 'data': 'Sorry...'}


app = Application()
app.start()
