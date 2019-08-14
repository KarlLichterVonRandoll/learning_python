"""
    数据轴向汇总
"""
import numpy as np

data = np.arange(1, 13).reshape(3, 4)
print(data)


def func(ary):
    return np.max(ary), np.mean(ary), np.min(ary)


r = np.apply_along_axis(func, 1, data)
print(r)
r = np.apply_along_axis(func, 0, data)
print(r)
