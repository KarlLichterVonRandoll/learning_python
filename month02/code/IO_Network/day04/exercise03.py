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

with open("time.txt", "a+") as f1:
    try:
        with open("time.txt") as f2:
            i = int(f2.readlines()[-1].split(" ")[0][:-1])
    except Exception:
        print("文件为空")
        i = 0

    while True:
        i += 1
        res = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
        f1.write(str(i) + ".  " + res + "\n")
        time.sleep(1)


