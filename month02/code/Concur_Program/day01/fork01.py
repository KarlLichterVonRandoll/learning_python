import os
import time

# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    time.sleep(1)
    print("The new process")
# 父进程执行部分
else:
    time.sleep(2)
    print("The old process")
# 父子进程都会运行
print("fork test finished")
