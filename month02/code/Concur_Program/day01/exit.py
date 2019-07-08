import os, sys
import time

# 父子进程的退出都不会影响对方的继续执行
pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("new process")
    time.sleep(1)
    os._exit(0)
    print("new end")
else:
    print("old process")
    time.sleep(2)
    sys.exit("退出")
    print("old end")


