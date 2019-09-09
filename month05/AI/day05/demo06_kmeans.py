"""
kmeans聚类算法
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.cluster as sc

x = np.loadtxt('../ml_data/multiple3.txt',
               delimiter=',', dtype='f8')
print(x.shape)
#  构建KMeans 训练模型
model = sc.KMeans(n_clusters=4)
model.fit(x)
labels = model.labels_  # 获取训练集每个样本类别

# 获取聚类中心
centers = model.cluster_centers_
print(centers)
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

# 绘制样本数据
mp.figure('KMeans', facecolor='lightgray')
mp.title('KMeans', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], label='Samples',
           s=60, c=labels, cmap='jet')
mp.scatter(centers[:, 0], centers[:, 1],
           label='center', marker='+', s=300,
           color='red')
mp.legend()
mp.show()