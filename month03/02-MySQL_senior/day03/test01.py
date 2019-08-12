import os
import sys
import time

pid = os.fork()

if pid == 0:
    os._exit(0)
    print("我是子进程", os.getpid(), os.getppid())
else:
    time.sleep(2)
    print("我是父进程", os.getpid())
