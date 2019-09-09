"""
随机森林回归模型
分析共享单车的需求，从而判断如何进行共享单车的投放
"""

import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

# 加载day数据
day_header = []
data = []
with open('../ml_data/bike_day.csv', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:  # header
            day_header = line.split(',')
        else:
            data.append(line.split(','))

# 整理header与data，解析输入与输出级
day_header = np.array(day_header[2: 13])
data = np.array(data)
x = data[:, 2: 13].astype('f4')
y = data[:, 15].astype('f4')

# 打乱数据集  拆分输入集与输出集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 选择随机森林模型，训练、预测
model = se.RandomForestRegressor(
    max_depth=10,
    n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
predict_test_y = model.predict(test_x)
print(sm.r2_score(test_y, predict_test_y))
day_fi = model.feature_importances_


# 加载hour数据
hour_header = []
data = []
with open('../ml_data/bike_hour.csv', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:  # header
            hour_header = line.split(',')
        else:
            data.append(line.split(','))
# 整理header与data，解析输入与输出级
hour_header = np.array(hour_header[2: 14])
data = np.array(data)
x = data[:, 2: 14].astype('f4')
y = data[:, 16].astype('f4')

# 打乱数据集  拆分输入集与输出集
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 选择随机森林模型，训练、预测
model = se.RandomForestRegressor(
    max_depth=10,
    n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
predict_test_y = model.predict(test_x)
print(sm.r2_score(test_y, predict_test_y))
hour_fi = model.feature_importances_


# 绘制特征重要性
mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('BikeDay Feature Importances', fontsize=14)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
xs = np.arange(len(day_fi))
sorted_ind = day_fi.argsort()[::-1]
mp.bar(xs, day_fi[sorted_ind],
       color='dodgerblue',
       label='BikeDay Feature Importances')
mp.xticks(xs, day_header[sorted_ind])
mp.legend()


mp.subplot(212)
mp.title('BikeHour Feature Importances', fontsize=14)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
xs = np.arange(len(hour_fi))
sorted_ind = hour_fi.argsort()[::-1]
mp.bar(xs, hour_fi[sorted_ind],
       color='orangered',
       label='BikeHour Feature Importances')
mp.xticks(xs, hour_header[sorted_ind])
mp.legend()

mp.tight_layout()
mp.show()