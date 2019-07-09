"""
    线程对象属性
"""

from threading import Thread
import time


def func():
    time.sleep(2)
    print("线程属性测试")


t = Thread(target=func, name="Jarvis")
print(t.getName())
t.setName("Friday")
print(t.getName())

t.setDaemon(True)  # 在start前设置，子线程随主线程退出

t.start()
print(t.is_alive())
