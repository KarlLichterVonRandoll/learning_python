"""
    ndarray 数组对象维度操作

"""

import numpy as np

a = np.arange(1, 9)
print(a)

"""
   视图变维(数据共享)
"""
b = a.reshape(2, 4)  # 变为二维数组
print(b)
c = a.ravel()  # 变为一维数组
print(c)

"""
    复制变维(数据独立)
"""
d = a.flatten()
print(d)
a += 10
print(a, '\n', d)

"""
    就地变维：直接改变原数组对象的维度，不返回新数组
"""
a.shape = (2, 4)
print(a)
a.resize(2, 2, 2)
print(a)
