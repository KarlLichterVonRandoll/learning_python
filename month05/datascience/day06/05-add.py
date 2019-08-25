"""
加法乘法通用函数
"""
import numpy as np

a = np.arange(1, 7)
print(a)

print("数组裁剪")
print(a.clip(min=3, max=5))
print("数组压缩，寻找大于3的数")
print(a.compress(a > 3))
print("数组压缩，寻找大于3小于5的数")
print(a.compress(np.all([a > 3, a < 5], axis=0)))
print("判断数组中是否所有数大于5")
print(np.all(a > 5))
print("判断数组中是否有大于5的数")
print(np.any(a > 5))
print("数组相加")
print(np.add(a, a))
print("数组元素累加和")
print(np.add.reduce(a))
print("数组元素累加和过程")
print(np.add.accumulate(a))
print("返回调用数组中所有元素的乘积——累乘")
print(np.prod(a))
print("数组元素累乘过程")
print(np.cumprod(a))
print("外和")
print(np.add.outer([10, 20, 30], a))
print("外积")
print(np.outer([10, 20, 30], a))
