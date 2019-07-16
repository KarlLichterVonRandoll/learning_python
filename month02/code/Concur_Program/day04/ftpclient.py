"""
    ftpclient.py
"""

from socket import *
import sys
import time

ADDR = ("127.0.0.1", 8888)
TIPS = "查看全部文件(v) 下载文件(g) 上传文件(u) 退出(q)"


# 创建 ftp 客户端类
class FTPclient:
    """
        客户端处理： 查看、上传、下载、退出
    """

    def __init__(self, sockfd):
        self.sockfd = sockfd

    # 查看文件列表
    def do_view(self):
        self.sockfd.send(b"v")  # 发送请求
        # 等待回复
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            # 一次接收文件字符串
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    # 下载文件
    def do_download(self):
        filename = input("输入下载文件名:")
        self.sockfd.send(("g " + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            f = open(filename, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
            print("下载完毕")
        else:
            print(data)

    # 上传文件
    def do_upload(self):
        file_name = input("输入需要上传的文件名或路径:")
        try:
            f = open(file_name, "rb")
        except Exception:
            print("文件不存在")
            return
        file_name = file_name.split("/")[-1]
        self.sockfd.send(("u " + file_name).encode())
        data = self.sockfd.recv(1024).decode()
        if data == "OK":
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    print("上传完成")
                    break
                self.sockfd.send(data)
        else:
            print(data)

    # 退出客户端
    def do_quit(self):
        self.sockfd.send(b"quit")
        self.sockfd.close()
        sys.exit("谢谢使用")
        pass


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPclient(s)

    while True:
        print(TIPS)  # 打印命令提示

        cmd = input("输入命令")

        if cmd.strip() == "v":
            ftp.do_view()
        elif cmd.strip() == "u":
            ftp.do_upload()
        elif cmd.strip() == "g":
            ftp.do_download()
        elif cmd.strip() == "q":
            ftp.do_quit()
        else:
            print("请输入正确命令")


if __name__ == "__main__":
    main()
