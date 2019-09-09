"""
人工分类
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

# 绘制分类边界线
# 把区间分为500*500网格矩阵，为每个网格预测类别
# 并设置颜色
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(
    np.linspace(l, r, n), np.linspace(b, t, n))
# 针对每个grid_x与grid_y预测所属类别
grid_z = np.piecewise(
    grid_x, [grid_x > grid_y, grid_x < grid_y],
    [0, 1])

mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], label='Samples',
           s=80, c=y, cmap='jet')
mp.show()