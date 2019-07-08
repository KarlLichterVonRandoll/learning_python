import os
import time
pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    # sleep 1 秒后，父进程先于子进程退出，子进程变成孤儿进程，系统进程称为它新的父进程
    time.sleep(1)
    print("Child PID", os.getpid())
    print("Get Parent PID", os.getppid())
else:
    # 父进程 sleep 3 秒，子进程先于父进程退出，父进程不退出，子进程变成僵尸进程
    time.sleep(3)
    print("Get child PID", pid)
    print("Parent PID", os.getpid())
