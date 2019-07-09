"""
    信号量
    信号量数量相当于资源，执行任务必须消耗资源
"""

from multiprocessing import Semaphore, Process
import os
import time

# 创建信号量（最多允许 3 个任务同时执行）
sem = Semaphore(3)


# 任务函数
def func01():
    sem.acquire()  # 想执行必须消耗一个信号量
    print("%s 执行任务" % os.getpid())
    time.sleep(2)
    print("%s 执行任务完毕" % os.getpid())
    sem.release()  # 执行完毕归还信号量


# 10 个任务需要执行
for i in range(10):
    p = Process(target=func01)
    p.start()


