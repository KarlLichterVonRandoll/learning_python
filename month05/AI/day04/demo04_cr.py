"""
分类报告
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.naive_bayes as nb
import sklearn.model_selection as ms
import sklearn.metrics as sm

# 读取数据
data = np.loadtxt('../ml_data/multiple1.txt',
                  delimiter=',', dtype='f8')
print(data.shape)
# 整理数据集
x = data[:, :2]
y = data[:, 2]

# 训练集测试集划分
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=7)

# 训练模型
model = nb.GaussianNB()

# 做5次交叉验证，若指标满意，再训练模型
ac = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='accuracy')
print(ac.mean())

pw = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='precision_weighted')
print(pw.mean())

rw = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='recall_weighted')
print(rw.mean())

f1 = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='f1_weighted')
print(f1.mean())

# 模型训练
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)

# 输出混淆矩阵
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)

# mp.matshow(cm, cmap='gray')
# mp.show()

# 输出分类报告
cr = sm.classification_report(test_y, pred_test_y)
print(cr)