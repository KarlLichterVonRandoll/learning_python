"""
    进程池
"""

from multiprocessing import Pool
import time


# 进程池事件
def worker(msg):
    time.sleep(2)
    print(time.ctime(), msg)


# 创建进程池
pool = Pool()

# 向进程池队列添加事件
for i in range(12):
    msg = "hello,%d" % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
