"""
标签编码
根据字符串形式的特征值在特征序列中的位置，为其指定一个数字标签，用于提供给基于数值算法的学习模型。
"""

import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array(
    ['audi', 'ford', 'audi', 'toyota',
     'ford', 'bmw', 'toyota', 'ford',
     'audi'])
label = sp.LabelEncoder()
res = label.fit_transform(raw_samples)
print(res)

# 根据标签编码的结果矩阵反查字典 得到原始数据矩阵
samples = label.inverse_transform(res)
print(samples)