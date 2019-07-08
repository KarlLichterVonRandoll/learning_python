import os
import sys

# 父子进程的退出都不会影响对方的继续执行
pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    print("Child PID", os.getpid())
    sys.exit("子进程退出")
else:
    print("Parent PID", os.getpid())
    """
        os.wait() 处理僵尸进程
    """
    pid, status = os.wait()
    print("pid", pid)
    print("status", status)  # 退出状态 * 256
    while True:  # 父进程不退出
        pass
