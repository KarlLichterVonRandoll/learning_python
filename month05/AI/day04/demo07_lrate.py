"""
学习曲线
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
    max_depth=9, n_estimators=140, random_state=7)

# 学习曲线
lc_params = np.linspace(0.1, 1.0, 10)
_, train_scores, test_scores = ms.learning_curve(
    model, train_x, train_y,
    train_sizes=lc_params, cv=5)

# 绘制学习曲线
mp.figure('Learning Curve', facecolor='lightgray')
mp.title('Learning Curve', fontsize=14)
mp.xlabel('train size')
mp.ylabel('f1-score')
mp.grid(linestyle=":")
mp.plot(lc_params, test_scores.mean(axis=1),
        'o-', label='max_depth')
mp.legend()
mp.show()

