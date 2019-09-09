"""
案例：事件预测
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm


class DigitEncoder:
    # 模拟LabelEncoder自定义的数字编码器

    def fit_transform(self, y):
        return y.astype('i4')

    def transform(self, y):
        return y.astype('i4')

    def inverse_transform(self, y):
        return y.astype('str')


# 加载并整理数据
data = np.loadtxt(
    '../ml_data/events.txt', delimiter=',',
    dtype='U15')

data = np.delete(data.T, 1, axis=0)
# 整理数据集
x, y, encoders = [], [], []
for row in range(len(data)):
    # 确定当前这组特征使用何种编码器
    if data[row][0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    # 整理数据集
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
y = np.array(y)
print(x.shape, y.shape, x[0], y[0])

# 划分训练集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=7)
model = svm.SVC(
    kernel='rbf', class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 准确率
print((test_y == pred_test_y).sum() / test_y.size)

import sklearn.metrics as sm

print(sm.classification_report(test_y, pred_test_y))

data = [['Tuesday', '13:30:00', '21', '23']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
