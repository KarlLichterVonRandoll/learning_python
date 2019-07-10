"""
    基于fork的多进程网络并发模型
    实现步骤
      1. 创建监听套接字
      2. 等待接收客户端请求
      3. 客户端连接创建新的进程处理客户端请求
      4. 原进程继续等待其他客户端连接
      5. 如果客户端退出，则销毁对应的进程
"""
from socket import *
import os
import signal

# 全局变量
ADDR = ("0.0.0.0", 8888)

# 创建TCP套接字
socketfd = socket()
socketfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketfd.bind(ADDR)
socketfd.listen(5)

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
    # 循环处理客户端连接
    try:
        c, addr = socketfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端事务
    pid = os.fork()
    if pid == 0:
        socketfd.close()
        handle(c)  # 处理具体事物
        os._exit(0)  # 子进程销毁
    # 无论父进程还是fork出错都要继续回去处理连接
    else:
        c.close()  # 父进程不需要和客户端连接
