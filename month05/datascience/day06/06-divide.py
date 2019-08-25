"""
除法相关函数
"""
import numpy as np

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])

print(a / b) # 真除，保留小数点
print(np.true_divide(a, b))  # 真除，保留小数点
print(np.floor_divide(a, b))  # 地板除向下取整
print(np.ceil(a / b))  # 向上取整
print(np.trunc(a / b))  # 截断取整
print(np.round(a / b))  # 四舍五入
