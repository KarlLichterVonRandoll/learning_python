"""
    ndarray 数组的掩码操作
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a + 10)
print(a * 2.5)
print(a + a)

# 输出100以内3的倍数
a = np.arange(1, 10)
mask = a % 3 == 0
print(mask)
print(a[mask])

mask = [2, 2, 3, 3, 6, 6, 4, 4]
print(a)
print(a[mask])
print(a[[True, False, True, False, True, False, True, False, True]])