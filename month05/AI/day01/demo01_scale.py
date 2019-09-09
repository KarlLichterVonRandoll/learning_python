"""
均值移除
"""

import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

# 均值移除，对列操作，每列均值为0，标准差为1
r = sp.scale(raw_sample)
print(r)

print(r.mean(axis=0))
print(r.std(axis=0))
