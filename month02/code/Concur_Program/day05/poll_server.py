"""
    poll_server.py  完成tcp并发服务

    思路分析： IO 多路服用实现并发
             建立 fileno -> IO 对象字典，并维护

"""

from socket import *
from select import *

# 创建监听套接字作为关注的 IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

print("监控 IO")

# 创建 poll 对象
p = poll()

# 建立查找字典，通过一个 IO 的 fileno 找到 IO 对象
# 始终和 register 的 IO 保持一致
fnmap = {s.fileno(): s}

# 关注 s
p.register(s, POLLIN | POLLERR)  # POLLIN = 1  POLLERR = 8

# 循环监控 IO 发生
while True:
    events = p.poll()  # 阻塞等待监控的IO事件发生
    # print(events)  # [(fileno,event),()....]
    # 循环遍历列表，查看哪个 IO 就绪，进行处理
    for fn, event in events:
        # 区分哪个 IO 就绪
        if fn == s.fileno():
            c, addr = fnmap[fn].accept()
            print("connect from", addr)
            # 关注客户端套接字
            p.register(c, POLLIN | POLLERR)
            fnmap[c.fileno()] = c  # 维护字典
        # 判断是否是 POLLIN 就绪，POLLIN = 1, POLLERR = 8
        # POLLIN & POLLIN = 1, POLLERR & POLLIN = 0
        elif event & POLLIN:
            data = fnmap[fn].recv(1024).decode()
            if not data:
                p.unregister(fn)  # 取消关注
                fnmap[fn].close()
                del fnmap[fn]
                continue
            print(data)
            fnmap[fn].send(b"OK")

