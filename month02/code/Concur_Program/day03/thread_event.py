"""
    线程同步互斥方法
    线程 Event
"""

from threading import Thread, Event, Lock

s = None  # 用于通信
e = Event()
lock = Lock()


def yzr():
    print("yzr 前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 操作完共享资源， e 设置, 结束阻塞


t = Thread(target=yzr)
t.start()

print("说对口令就是自己人")
e.wait()  # 阻塞等待 子线程执行

if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("回答正确")
else:
    print("枪毙！")

t.join()
