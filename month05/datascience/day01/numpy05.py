"""
    多维数组的组合与拆分
"""

import numpy as np

ary01 = np.arange(1, 7).reshape(2, 3)
ary02 = np.arange(10, 16).reshape(2, 3)

# 垂直方向完成组合操作，生成新数组
ary03 = np.vstack((ary01, ary02))
print(ary03, ary03.shape)
# 垂直方向完成拆分操作，生成两个数组
a, b, c, d = np.vsplit(ary03, 4)
print(a, b, c, d)

# 水平方向完成组合操作，生成新数组
ary04 = np.hstack((ary01, ary02))
print(ary04, ary04.shape)
# 水平方向完成拆分操作，生成两个数组
e, f = np.hsplit(ary04, 2)
print(e, '\n', f)

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 深度方向（3维）完成组合操作，生成新数组
i = np.dstack((a, b))
print(i.shape)
# 深度方向（3维）完成拆分操作，生成两个数组
k, l = np.dsplit(i, 2)
print("==========")
print(k)
print(l)

a = np.array([1,2,3,4]).reshape(2,2)
print(a)
print(np.split(a, 2, axis=1))

a = np.arange(1,9)		#[1, 2, 3, 4, 5, 6, 7, 8]
b = np.arange(9,17)		#[9,10,11,12,13,14,15,16]
#把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
#把两个数组组合在一起成两列
d = np.column_stack((a, b))
print(d)