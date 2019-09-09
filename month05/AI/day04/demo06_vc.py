"""
验证曲线
"""

import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp


data = np.loadtxt(
    '../ml_data/car.txt', delimiter=',',
    dtype='U20')
print(data.shape)
data = data.T
train_x, train_y = [], []
encoders = []
for row in range(len(data)):  # 迭代每一列
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(
            encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)
# 整理 训练集的输入与输出
train_x = np.array(train_x).T
train_y = np.array(train_y)
print(train_x[0], '  ', train_y[0])

# 选择模型，训练模型
model = se.RandomForestClassifier(
    max_depth=6, n_estimators=140, random_state=7)

# 验证曲线
n_estimators_params = np.arange(100, 200, 10)
max_depth_params = np.arange(1, 11)
train_scores, test_scores = ms.validation_curve(
    model, train_x, train_y,
    'max_depth', max_depth_params,
    cv=5)
print(test_scores.mean(axis=1))

# 绘制验证曲线
mp.figure('Validation Curve', facecolor='lightgray')
mp.title('Validation Curve', fontsize=14)
mp.xlabel('max_depth')
mp.ylabel('f1-score')
mp.grid(linestyle=":")
mp.plot(max_depth_params,
        test_scores.mean(axis=1), 'o-',
        label='max_depth')
mp.legend()
mp.show()
