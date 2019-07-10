"""
    基于 process 的多进程网络并发模型
    实现步骤
      1. 创建监听套接字
      2. 等待接收客户端请求
      3. 客户端连接创建新的进程处理客户端请求
      4. 原进程继续等待其他客户端连接
      5. 如果客户端退出，则销毁对应的进程
"""

from multiprocessing import Process
from socket import *
import sys
import signal

# 全局变量
ADDR = ("0.0.0.0", 8888)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888...")

# 子进程处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"hello")
    c.close()


while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    p = Process(target=handle, args=(c,))
    p.daemon = True
    p.start()




