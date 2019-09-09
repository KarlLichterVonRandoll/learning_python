"""
多项式回归模型
"""

import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.pipeline as pl

# 采集数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1), unpack=True)

# 训练多项式回归模型
x = x.reshape(-1, 1)
model = pl.make_pipeline(
    sp.PolynomialFeatures(8),
    lm.LinearRegression())
# 训练模型
model.fit(x, y)
# 预测输出
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))

# 绘制多项式曲线
px = np.linspace(x.min(), x.max(), 1000)
pred_py = model.predict(px.reshape(-1, 1))

# 画图
mp.figure('Poly Regression', facecolor='lightgray')
mp.title('Poly Regression', fontsize=16)
mp.xlabel('X', fontsize=12)
mp.ylabel('Y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, color='dodgerblue',
           label='Samples', s=70, marker='o')
mp.plot(px, pred_py, color='orangered',
        label='Poly Line')
mp.legend()
mp.show()
