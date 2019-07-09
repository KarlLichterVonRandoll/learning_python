"""
    自定义线程类
"""

from threading import Thread
import time


# 自定义线程类
class MyThread(Thread):
    # 重写父类init
    def __init__(self, target=None, args=None, kwargs=None):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()  # 加载父类init

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, time.ctime()))
        time.sleep(sec)


t = MyThread(target=player, args=(2,), kwargs={"song": "凉凉"})

t.start()
t.join()
