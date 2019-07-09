"""
    管道通信
    1. multiprocessing 中管道通信只能同于有亲缘关系的进程中
    2. 管道对象在父进程中创建，子进程通过父进程获取
"""

from multiprocessing import Pipe, Process

# 创建管道, 默认是双向管道, 单向管道 fd1 只能 recv, fd2 只能 send
fd1, fd2 = Pipe()


def app01():
    print("启动 app01, 请登录")
    print("请求 app02 授权")
    fd1.send("app01 请求登录")  # 写入管道
    data = fd1.recv()
    if data:
        print("登录成功:", data)


def app02():
    data = fd2.recv()  # 阻塞等待读取管道内容
    print(data)
    fd2.send(('admin', '123'))


p01 = Process(target=app01)
p02 = Process(target=app02)
p01.start()
p02.start()
p01.join()
p02.join()