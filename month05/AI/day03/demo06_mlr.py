"""
逻辑回归实现多元分类
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

# 训练逻辑分类器
model = lm.LogisticRegression(
    solver='liblinear', C=500)
model.fit(x, y)

# 绘制分类边界线
# 把区间分为500*500网格矩阵，为每个网格预测类别
# 并设置颜色
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(
    np.linspace(l, r, n), np.linspace(b, t, n))

# 针对每个grid_x与grid_y预测所属类别
mesh_x = np.column_stack(
    (grid_x.ravel(), grid_y.ravel()))
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)

mp.figure('Logistic Classification', facecolor='lightgray')
mp.title('Logistic Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], label='Samples',
           s=80, c=y, cmap='jet')
mp.show()