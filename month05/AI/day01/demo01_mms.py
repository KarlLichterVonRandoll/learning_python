"""
范围缩放
"""

import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

# 将每列数据范围缩放到[0,1]区间
mms = sp.MinMaxScaler(feature_range=(0, 1))
res = mms.fit_transform(raw_sample)
print(res)


