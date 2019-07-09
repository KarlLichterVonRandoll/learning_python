"""
    进程函数参数传递
"""

from multiprocessing import Process
import time


# 带参数的进程函数
def func(number, times):
    for i in range(times):
        time.sleep(2)
        print(number * i)


p1 = Process(target=func, args=(2, 3))
p2 = Process(target=func, args=(2,), kwargs={'times': 3})

p1.start()
p2.start()

p1.join()
p2.join()
