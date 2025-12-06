import numpy as np

# 定义损失函数（实验室模型优化的目标）
def loss(x):
    return x**2 + 4*x + 4  # 二次函数，最小值在x=-2

# 梯度下降（SGD，随机梯度下降）
x = 0  # 初始值
lr = 0.1  # 学习率
for i in range(10):
    grad = 2*x + 4  # 损失函数的梯度
    x = x - lr * grad  # 梯度下降更新
    print(f"第{i+1}步：x={round(x,2)}，损失={round(loss(x),2)}")