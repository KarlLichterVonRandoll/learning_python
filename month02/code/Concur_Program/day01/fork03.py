"""
    使用二级子进程解决僵尸进程问题
"""

import os
import time
import sys


def f1():
    for i in range(3):
        time.sleep(2)
        print("write code")


def f2():
    for i in range(2):
        time.sleep(4)
        print("test code")


pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:  # 一级子进程
    p = os.fork()
    if p == 0:  # 二级子进程
        f2()
    else:
        sys.exit("一级子进程结束")
else:
    os.wait()  # 等一级子进程退出
    f1()
