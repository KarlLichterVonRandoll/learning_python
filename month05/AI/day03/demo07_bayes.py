"""
高斯朴素贝叶斯
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb

# 读取数据
data = np.loadtxt('../ml_data/multiple1.txt',
                  delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]
# 训练模型
model = nb.GaussianNB()
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

# 绘制
mp.figure('Naive Bayes', facecolor='lightgray')
mp.title('Naive Bayes', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], label='Samples',
           s=60, c=y, cmap='jet')
mp.show()