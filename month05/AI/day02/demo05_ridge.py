"""
岭回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

# 采集数据
x, y = np.loadtxt(
    '../ml_data/abnormal.txt', delimiter=',',
    usecols=(0, 1), unpack=True)

# 选择、创建模型
model = lm.LinearRegression()
x = x.reshape(-1, 1)  # 把x改为n行1列的2维数组
model.fit(x, y)
# 得到预测结果
pred_y = model.predict(x)

# 选择岭回归模型
model = lm.Ridge(
    150, fit_intercept=True, max_iter=1000)
model.fit(x, y)
ridge_pred_y = model.predict(x)

# 画图
mp.figure('Regression', facecolor='lightgray')
mp.title('Regression', fontsize=16)
mp.xlabel('X', fontsize=12)
mp.ylabel('Y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, color='dodgerblue',
           label='Samples', s=70, marker='o')
mp.plot(x, pred_y, color='orangered',
        label='Linear Regression')
mp.plot(x, ridge_pred_y, color='blue',
        label='Ridge Regression')
mp.legend()
mp.show()