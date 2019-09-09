"""
二值化处理
根据一个事先给定的阈值，用0和1表示特征值不高于或高于阈值。
二值化后的数组中每个元素非0即1，达到简化数学模型的目的。
"""

import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

bin = sp.Binarizer(threshold=80)
res = bin.fit_transform(raw_samples)
print(res)

raw_samples[raw_samples <= 80] = 0
raw_samples[raw_samples > 80] = 1
print(raw_samples)
