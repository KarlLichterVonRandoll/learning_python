"""
    numpy 的基本使用
"""
import numpy as np

ary01 = np.array(['a', 2, 3, 4, 5])  # 生成一维数组
print(ary01, type(ary01), ary01.shape)  # 打印数组，查看变量类型，查看数组维度
print(ary01.dtype)  # 查看数组元素类型


ary02 = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])
print(ary02, type(ary02), ary02.shape)
print(ary02.dtype)
print(ary02.size)  # 数组元素的个数  10
print(len(ary02))  # 数组长度  2
# 数组索引，从 0 开始
print(ary02[0])
print(ary02[0][1])
print(ary02[1, 1])


# 生成数组包含 0 到 5(不包含)，步长为 1
a = np.arange(0, 5, 1)
print(a, type(a), a.shape)
print(a.dtype)

# 生成元素都为0的数组，指定元素类型为 int64
b = np.zeros(10, dtype='int64')
print(b, type(b), b.shape)
print(b.dtype)

# 生成元素都为 1 的数组，元素默认类型为 float64
c = np.ones(10)
print(c, type(c), c.shape)
print(c.dtype)
