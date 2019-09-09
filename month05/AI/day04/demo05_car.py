"""
随机森林分类器  小汽车评级
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

# 1.读取文本数据，对每列进行标签编码，基于随机森林分类器进行模型训练，进行交叉验证。
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
# 交叉验证
cv = ms.cross_val_score(model, train_x, train_y,
                        cv=5, scoring='accuracy')
print(cv.mean())
model.fit(train_x, train_y)

# 客户端传递来一组样本，每个样本给出预测结果
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]

# 使用训练时创建的LabelEncoder处理样本输入：
data = np.array(data).T
test_x, test_y = [], []
for row in range(len(data)):  # 迭代每一列
    if row < len(data) - 1:
        test_x.append(
            encoders[row].transform(data[row]))
    else:
        test_y = encoders[row].transform(data[row])
# 使用model对测试样本进行预测
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
# 使用最后一个labelencoder转换输出
print(encoders[-1].inverse_transform(test_y))
print(encoders[-1].inverse_transform(pred_test_y))
