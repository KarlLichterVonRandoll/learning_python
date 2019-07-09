"""
    测试单进程 和 多线程
"""

from threading import Thread
import time


def count(x, y):
    c = 0
    while c < 700000:
        x += 1
        y += 1
        c += 1


# IO
# def io():
#     pass
#
#
# def write():
#     with open("text.txt", "w") as f

start = time.time()

# 单进程实现
for i in range(10):
    count(1, 2)

print(time.time()-start)


start = time.time()
# 多线程实现
jobs = []
for i in range(10):
    t = Thread(target=count, args=(1, 2))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()


print(time.time() - start)
