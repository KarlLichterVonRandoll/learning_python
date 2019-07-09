"""
    进程对象属性
"""

from multiprocessing import Process
import time


def func():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())


p = Process(target=func, name="edith")

print(p.name)

print(p.pid)

print(p.is_alive())

p.daemon = True

p.start()

print(p.pid)

print(p.is_alive())
