from greenlet import greenlet
import time


def fun1():
    print("执行1")
    time.sleep(1)
    gr2.switch()
    print("结束1")
    gr2.switch()


def fun2():
    print("执行2")
    time.sleep(1)
    gr1.switch()
    print("结束2")


# 将函数变为携程
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  # 选择要执行的携程函数
