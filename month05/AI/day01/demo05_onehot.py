"""
onehot 独热编码
为样本特征的每个值建立一个由一个1和若干个0组成的序列，用该序列对所有的特征值进行编码。
"""

import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array(
    [[1, 3, 2], [7, 5, 4], [1, 8, 6], [7, 3, 9]])
print(raw_samples)

one = sp.OneHotEncoder(sparse=True) # 使用稀疏矩阵表示
res = one.fit_transform(raw_samples)
print(res)