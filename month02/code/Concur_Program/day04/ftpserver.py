"""
    ftp 文件服务器
"""

from threading import Thread
from socket import *
import sys, time
import os

ADDR = ("0.0.0.0", 8888)
FTP = "/home/tarena/m1905/month02/code/Concur_Program/day04/server_file/"


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    print("start listening...")

    while True:
        try:
            c, addr = s.accept()
            print("connect from", addr)
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print(e)
            continue

        client = FTPserver(c)
        client.setDaemon(True)
        client.start()


# 创建 ftp 服务器类
class FTPserver(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    # 循环接受请求，分情况调用功能函数
    def run(self):
        while True:
            request = self.connfd.recv(1024).decode()
            if not request or request == "quit":
                return  # run 结束对应客户端线程结束
                # self.do_quit()
            elif request == "v":
                self.do_view()
            elif request[0] == "g":
                filename = request.strip().split(" ")[-1]
                self.do_download(filename)
            elif request[0] == "u":
                filename = request.strip().split(" ")[-1]
                self.do_upload(filename)

    # 处理文件列表请求
    def do_view(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)  # 防止毡包
        # 拼接文件
        filelist = ""
        for file in files:
            # 判断非隐藏文件、非文件夹和普通文件
            if file[0] != "." and os.path.isfile(FTP + file):
                filelist += file + "\n"
        self.connfd.send(filelist.encode())

    # 处理下载文件请求
    def do_download(self, filename):
        try:
            f = open(FTP + filename, "rb")
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)

        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)

    # 处理上传文件请求
    def do_upload(self, filename):
        if filename in os.listdir(FTP):
            self.connfd.send("文件已经存在".encode())
            return
        else:
            self.connfd.send(b"OK")

        f = open(FTP + filename, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()

    # 处理客户端退出请求
    def do_quit(self):
        sys.exit("退出")
        # os._exit(0) 会连带服务器一起退出


if __name__ == "__main__":
    main()
