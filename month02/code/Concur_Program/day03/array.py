"""
    开辟共享内存空间
    共享内存中存放一组数据
"""

from multiprocessing import Array, Process

# shm = Array('i', [1, 2, 3, 4])
# shm = Array('i', 5)  # 开辟初始 5 个整型空间，初始为0
shm = Array('c', b'hello')  # 字节串


def func():
    # array 创建的共享内存可迭代
    for i in shm:
        print(i)
    shm[0] = b'H'


p = Process(target=func)
p.start()
p.join()
for i in shm:
    print(i)

print(shm.value)  # .value 只能打印字节串串
