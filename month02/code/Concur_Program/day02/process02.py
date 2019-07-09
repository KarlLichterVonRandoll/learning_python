"""
    multiprocessing 创建多个进程
"""

from multiprocessing import Process
import time
import os


def func01():
    time.sleep(2)
    print("chi fan......")
    print(os.getppid(), '---', os.getpid())


def func02():
    time.sleep(3)
    print("shui jiao......")
    print(os.getppid(), '---', os.getpid())


def func03():
    time.sleep(4)
    print("da dou dou......")
    print(os.getppid(), '---', os.getpid())


funcs = [func01, func02, func03]
processes = []

for func in funcs:
    p = Process(target=func)
    processes.append(p)
    p.start()

for process in processes:
    process.join()


