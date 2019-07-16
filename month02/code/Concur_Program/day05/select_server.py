"""
    select 方法实现tcp服务
    1. 将关注的 IO 放入到监控列表
    2. 当 IO 就绪时会通过 select 返回
    3. 遍历返回列表，得知哪个 IO 就绪进行处理

"""

from select import select
from socket import *

# 创建监听套接字作为关注的 IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

print("监控IO")

# 设置关注列表
rlist = [s]  # s 用于等待处理连接
wlist = []
xlist = []

# 循环监控 IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    print(len(rlist))
    # 遍历返回值列表，处理就绪的 IO
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from", addr)
            rlist.append(c)  # 增加新的 IO 关注
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)  # 取消对客户端关注
                r.close()
                continue
            print(data)
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)  # 发完消息移除

    for x in ws:
        pass
