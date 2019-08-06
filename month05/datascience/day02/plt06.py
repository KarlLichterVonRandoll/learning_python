"""
    散点图
"""
import matplotlib.pyplot as plt
import numpy as np

n = 200
# 生成满足正态分布的随机数, 期望值、标准差、数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)

plt.figure('scatter', facecolor='lightgray')
plt.title('scatter')
plt.scatter(x, y, c='red')
d = (x-172)**2 + (y-60)**2
plt.scatter(x, y, c=d, cmap='jet_r')
plt.show()
