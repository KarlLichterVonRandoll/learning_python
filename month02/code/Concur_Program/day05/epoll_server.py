"""
    epoll_server.py  完成tcp并发服务

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

# 创建 epoll 对象
ep = epoll()

# 建立查找字典，通过一个 IO 的 fileno 找到 IO 对象
# 始终和 register 的 IO 保持一致
fnmap = {s.fileno(): s}

# 关注 s
ep.register(s, EPOLLIN | EPOLLERR)  # EPOLLIN = 1  EPOLLERR = 8

# 循环监控 IO 发生
while True:
    events = ep.poll()  # 阻塞等待监控的IO事件发生
    # print(events)  # [(fileno,event),()....]
    # 循环遍历列表，查看哪个 IO 就绪，进行处理
    for fn, event in events:
        # 区分哪个 IO 就绪
        if fn == s.fileno():
            c, addr = fnmap[fn].accept()
            print("connect from", addr)
            # 关注客户端套接字
            ep.register(c, EPOLLIN | EPOLLERR)
            fnmap[c.fileno()] = c  # 维护字典
        # 判断是否是 EPOLLIN 就绪，EPOLLIN = 1, EPOLLERR = 8
        # EPOLLIN & EPOLLIN = 1, EPOLLERR & EPOLLIN = 0
        elif event & EPOLLIN:
            data = fnmap[fn].recv(1024).decode()
            if not data:
                ep.unregister(fn)  # 取消关注
                fnmap[fn].close()
                del fnmap[fn]
                continue
            print(data)
            fnmap[fn].send(b"OK")
