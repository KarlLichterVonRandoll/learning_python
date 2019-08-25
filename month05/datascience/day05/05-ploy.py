"""
    多项式基本操作
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4 * x ** 3 + 3 * x ** 2 - 1000 * x + 1

# 求多项式函数的导函数
P = [4, 3, -1000, 1]  # 多项式函数中的系数
Q = np.polyder(P)  # 多项式函数求导，根据原多项式函数求出其导函数
xs = np.roots(Q)  # 已知多项式 求多项式函数的根（与x轴交点的横坐标
print(xs)
ys = np.polyval(P, xs)  # 把X带入多项式函数求得函数值
mp.scatter(xs, ys, marker='o', color='red',
           zorder=3)

mp.plot(x, y)
mp.show()
