"""
模型加载
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import pickle

# 采集数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1), unpack=True)

# 从文件中加载模型
with open('../ml_data/lr.pkl', 'rb') as f:
    model = pickle.load(f)

# 得到预测结果
pred_y = model.predict(x.reshape(-1, 1))

# 评估模型误差
import sklearn.metrics as sm

print(sm.mean_absolute_error(pred_y, y))
print(sm.mean_squared_error(pred_y, y))
print(sm.median_absolute_error(pred_y, y))
print(sm.r2_score(pred_y, y))
