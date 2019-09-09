import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

# 采集数据
x, y = np.loadtxt('single.txt', delimiter=',',
                  usecols=(0, 1), unpack=True)
x = x.reshape(-1, 1)
# 创建模型
model = lm.LinearRegression()  # 线性回归
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y = model.predict(x)
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60, label='Sample')
mp.plot(x, pred_y, c='orangered', label='Regression')
mp.legend()
mp.show()
