"""
模型导出成文件
"""

import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import pickle

# 采集数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1), unpack=True)

# 选择、创建模型
model = lm.LinearRegression()
x = x.reshape(-1, 1)  # 把x改为n行1列的2维数组
model.fit(x, y)
# 得到预测结果
pred_y = model.predict(x)

# 评估模型误差
import sklearn.metrics as sm

print(sm.mean_absolute_error(pred_y, y))
print(sm.mean_squared_error(pred_y, y))
print(sm.median_absolute_error(pred_y, y))
print(sm.r2_score(pred_y, y))

# 导出到文件
with open('../ml_data/lr.pkl', 'wb') as f:
    pickle.dump(model, f)

print('dump success.')
