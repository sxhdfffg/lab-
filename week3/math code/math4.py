import numpy as np

def entropy(p):
    # 计算熵（实验室衡量数据不确定性常用）
    return -np.sum(p * np.log2(p + 1e-10))  # 加1e-10避免log(0)

# 示例：两种概率分布
p = np.array([0.5, 0.5])  # 均匀分布，熵最大
q = np.array([0.8, 0.2])  # 非均匀分布，熵较小

print("p的熵：", round(entropy(p), 2))
print("q的熵：", round(entropy(q), 2))

# KL散度（衡量两个分布的差异，实验室模型优化常用）
kl = np.sum(p * np.log2((p + 1e-10) / (q + 1e-10)))
print("p和q的KL散度：", round(kl, 2))