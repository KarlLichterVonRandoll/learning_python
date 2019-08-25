"""
    矢量化
"""
import numpy as np
import math as m


def foo(x, y):
    return m.sqrt(x ** 2 + y ** 2)


a = 3
b = 4
print(foo(a, b))

# 把foo函数矢量化，使之可以处理矢量数据
foovec = np.vectorize(foo)
a = np.array([3, 4, 5, 6])
b = np.array([4, 5, 6, 7])
print(foovec(a, b))

# 使用frompyfunc可以完成与vectorize一样的功能
func = np.frompyfunc(foo, 2, 1)
print(func(a, b))


c = np.array([70, 80, 60, 30, 40])
# 针对源数组中的每一个元素，检测其是否符合条件序列中的每一个条件，
# 符合哪个条件就用取值系列中与之对应的值，
# 表示该元素，放到目标 数组中返回。
d = np.piecewise(
    c,
    [c < 60, c == 60, c > 60],
    [-1, 0, 1])
print(d)
