"""
    线程锁
"""

from threading import Lock, Thread

a = b = 0

lock = Lock()


def func():
    while True:
        lock.acquire()
        if a != b:
            print("a=", a, "b=", b)
        lock.release()


t = Thread(target=func)
t.start()

while True:
    with lock:
        a += 1
        b += 1




