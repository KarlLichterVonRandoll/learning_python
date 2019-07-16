"""
    gevent 协程模块
"""

import gevent
from gevent import monkey

monkey.patch_time()
from time import sleep


# 协程函数
def foo(a, b):
    print("Running foo...", a, b)
    # gevent.sleep(2)  # 睡眠阻塞会自动查看其他可以执行的协程
    sleep(2)
    print("Foo again...")


def bar():
    print("Running bar...")
    # gevent.sleep(3)
    sleep(3)
    print("Bar again...")


# 生成携程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)


gevent.joinall([f, b])  # 阻塞等待f,b两个协程执行完毕

# gevent.sleep(5)  # gevent睡眠阻塞
