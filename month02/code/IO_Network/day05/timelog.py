"""
    编写一个程序，向一个文件中写入如下内容：
     　　　
     　　1.  2019-1-1  18:18:18
     　　2.  2019-1-1  18:18:19
     　　3.  2019-1-1  18:18:24

        循环每隔１秒写入一次,序号从１排列
        ctrl-c结束程序，下次启动程序
        序号要与之前的衔接
"""

import time

f1 = open("time.txt", "a+")

# 文件偏移量指向开头
f1.seek(0, 0)
i = 0
for line in f1:
    i += 1

while True:
    i += 1
    s = "%d.  %s\n"%(i, time.ctime())
    res = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
    f1.write(s)
    f1.flush()
    time.sleep(1)
