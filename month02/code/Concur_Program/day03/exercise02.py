from threading import Thread
import time


# IO
def io():
    write()
    read()


def write():
    f = open('test.txt', 'w')
    for i in range(180000):
        f.write("Hello world\n")
    f.close()


def read():
    f = open('test.txt')
    lines = f.readlines()
    f.close()


start = time.time()

# 单进程
for i in range(10):
    io()

print(time.time() - start)


start = time.time()
# 多线程
jobs = []
for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print(time.time() - start)
