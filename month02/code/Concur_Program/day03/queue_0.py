"""
    消息队列
      符合先进先出原则
"""

from multiprocessing import Queue, Process
from random import randint
import time

# 创建消息队列
q = Queue(5)


def handle():
    for i in range(6):
        x = randint(1, 33)
        q.put(x)  # 消息入队
    q.put(randint(1, 16))


def request():
    while True:
        # print("开始摇号")
        time.sleep(1)
        try:
            print(q.get(timeout=2), end="\n")  # 出队
        except:
            break


p01 = Process(target=handle)
p02 = Process(target=request)
p01.start()
p02.start()
p01.join()
p02.join()
