"""
    线程基础使用
    1. 封装线程函数
    2. 创建线程对象
    3. 启动线程
    4. 回收线程
"""

from threading import Thread
import time
import os

a = 1


# 创建线程函数
def music(song):
    for i in range(3):
        time.sleep(2)
        print("播放: %s" % song)
        print(os.getpid())
    global a
    print(a)
    a = 10000


# 创建线程对象
t1 = Thread(target=music, args=("黄河大合唱",))
t2 = Thread(target=music, args=("葫芦娃",))
t1.start()
t2.start()
t1.join()
t2.join()

print(a)
