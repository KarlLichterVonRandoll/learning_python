"""
特征值和特征向量：
    对于n阶方阵A，如果存在数a和非零n维列向量x，使得Ax=ax，
    则称a是矩阵A的一个特征值，x是矩阵A属于特征值a的特征向量
"""
import numpy as np

m = np.mat('10 4 2; 18 6 2; 7 4 6')

# 提取特征值和特征向量
eigvals, eigvecs = np.linalg.eig(m)
print(eigvals)
print(eigvecs)

# 逆向推导原方阵
m2 = eigvecs * np.diag(eigvals) * eigvecs.I
print(m2)

# 抹掉部分特征，生成原方阵
eigvals[1:] = 0  # 抹掉末尾元素的特征信息
m2 = eigvecs * np.diag(eigvals) * eigvecs.I
print(m2)
