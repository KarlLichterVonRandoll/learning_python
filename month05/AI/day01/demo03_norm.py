"""
特征归一化处理
归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。
变换后的样本矩阵，每个样本的特征值绝对值之和为1。
"""
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

res = sp.normalize(raw_sample, norm="l1")
print(res)
