import os
import time

print("============")
# 赋值语句在父进程中开辟内存空间，子进程从fork之后的语句开始执行，
# 但会copy父进程所有的内存空间，子进程也可以使用 a
a = 1
# 创建子进程
pid = os.fork()

print("~~~~~~~~~~~~")

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    # 这里的赋值不用影响父进程的内存空间
    a = 1000
    print("a=", a)
    print("The new process")
# 父进程执行部分
else:
    time.sleep(2)
    print("a=", a)
    print("The old process")
# 父子进程都会运行
print("a =>", a)
print("fork test finished")
