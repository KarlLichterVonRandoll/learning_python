"""
    copy_file.py
    分别复制文件上半部分和下半部分

    多进程的 io 操作注意点
    如果在父进程中打开一个文件对象，操作系统中会记录 io 的打开行为，此时创建的子进程会复制父进程中的 io 打开行为；
    而操作系统中不会记录新的 io，也就是说父子进程共用一个 io ,包括文件偏移量。
    以下代码中，如果先执行后半部分读取(bot)，文件偏移量会改变，执行前半部分读取就不会读到数据
"""

from multiprocessing import Process
import os

filename = "img.jpg"
file01name = "img02.jpg"
file02name = "img03.jpg"
size = os.path.getsize(filename)

# 父进程中创建 f1，两个子进程使用 f1 会相互影响
f1 = open(filename, "rb")


def top():
    # f1 = open(filename, "rb")
    f2 = open(file01name, "wb")
    n = size // 2
    f2.write(f1.read(n))
    f1.close()
    f2.close()


def bot():
    # f1 = open(filename, "rb")
    f2 = open(file02name, "wb")
    f1.seek(size // 2, 0)
    f2.write(f1.read())
    f1.close()
    f2.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
p1.join()
p2.join()

print(os.path.getsize(filename))
print(os.path.getsize(file01name))
print(os.path.getsize(file02name))
