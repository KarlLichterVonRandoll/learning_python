"""
    创建两个进程，分别复制一个文件的上下半部分
    将复制内容放到两个新的文件中，按字节分文件
"""
from multiprocessing import Process
import os

file_name = "data01.txt"
file01_name = "data02.txt"
file02_name = "data03.txt"
length = os.path.getsize(file_name)


def func(name, pos):
    f1 = open(file_name, "rb")
    f2 = open(name, "wb")
    if pos == 2:
        f1.seek(-length // 2, pos)
        f2.write(f1.read())
    else:
        f2.write(f1.read(length // 2 + 1))

    f1.close()
    f2.close()


p1 = Process(target=func, args=(file01_name, 0))
p2 = Process(target=func, args=(file02_name, 2))
p1.start()
p2.start()
p1.join()
p2.join()

print(os.path.getsize(file_name))
print(os.path.getsize(file01_name))
print(os.path.getsize(file02_name))
