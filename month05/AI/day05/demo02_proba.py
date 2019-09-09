"""
置信概率
根据样本与分类边界的距离远近，对其预测类别的可信程度进行量化，
离边界越近的样本，置信概率越低，反之，离边界越远的样本，置信概率高。
"""

import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.model_selection as ms
import sklearn.metrics as sm

# 读取数据
data = np.loadtxt('../ml_data/multiple2.txt',
                  delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]
# 训练模型
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=7)
model = svm.SVC(kernel='rbf', C=600, gamma=0.01,
                probability=True)
model.fit(train_x, train_y)
# 针对测试集预测结果   评估分类效果
pred_test_y = model.predict(test_x)
# print(sm.refusion_matrix(test_y, pred_test_y))
print(sm.classification_report(test_y, pred_test_y))

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

# 新增样本，得到每个样本的预测输出与置信概率
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
print(pred_prob_y)
# 置信概率矩阵
probs = model.predict_proba(prob_x)
print(probs)


# 绘制
mp.figure('SVM Classifier', facecolor='lightgray')
mp.title('SVM Classifier', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 调用pcolormesh填充网格化背景
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1],
           label='Samples', s=60, c=test_y,
           cmap='jet')

# 绘制每个测试样本，并给出标注
mp.scatter(prob_x[:, 0], prob_x[:, 1],
           c=pred_prob_y,
           cmap='jet_r', s=80, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})

mp.show()