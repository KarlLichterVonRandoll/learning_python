from array import array
from random import random

# 利用一个可迭代对象来建立一个双精度浮点数组(类型码是 'd'),
# 这里用的可迭代对象是一个生成器表达式。
floats = array('d', (random() for i in range(10**7)))

print(floats[-1])  # 查看数组最后一个元素

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # 将数组存入二进制文件
fp.close()

floats2 = array('d')  # 创建一个空的双精度浮点数组

fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # 将1000万个浮点数从二进制文件中取出
fp.close()

print(floats2[-1])

print(floats2 == floats)
