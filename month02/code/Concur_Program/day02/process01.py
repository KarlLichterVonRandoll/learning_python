"""
    multiprocessing 模块创建进程
    1. 编写进程函数
    2. 生产进程对象
    3. 启动进程
    4. 回收进程
"""

import multiprocessing as mp
from time import *

a = 1


# 进程函数
def fun():
    print("开始一个进程")
    global a
    print("a = ", a)
    a = 1000
    sleep(5)
    print("子进程结束")

start = time()

# 创建进程对象
p1 = mp.Process(target=fun)
p2 = mp.Process(target=fun)
p1.start()  # 启动进程
p2.start()  # 启动进程zzzzzNNNNNNNNNNNNNNNNNN

print(a)
sleep(3)

p1.join()  # 回收进程
p2.join()  # 回收进程

print(time() - start)