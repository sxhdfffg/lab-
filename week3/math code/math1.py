import numpy as np
from scipy.linalg import lu

# 1. 矩阵分解（LU/SVD，实验室线性代数核心需求）
A = np.array([[3, 2], [1, 0]])
p, l ,u = lu(A)  # LU分解
print("LU分解结果：\n", p, l, u)

# 2. 特征值问题（实验室AI模型常用）
eigenvals, eigenvecs = np.linalg.eig(A)
print("特征值：", eigenvals)
print("特征向量：\n", eigenvecs)

# 验证Av=lamda*v（嘿嘿，我自己写的，今天看懂了）
print(np.allclose(A@eigenvecs, eigenvecs*eigenvals))