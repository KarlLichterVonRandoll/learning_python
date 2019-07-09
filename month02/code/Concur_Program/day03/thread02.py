"""
    线程函数参数演示
"""

from threading import Thread
import time


# 含有参数的线程函数
def func(sec, name):
    print("线程函数参数")
    time.sleep(sec)
    print("%s执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=func, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
