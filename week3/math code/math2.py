import numpy as np

# 张量（3维数组，实验室CNN输入常用）
tensor = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])  # 2x2x2张量
print("张量形状：", tensor.shape)  # 查看维度
print("张量求和：", tensor.sum())  # 张量运算