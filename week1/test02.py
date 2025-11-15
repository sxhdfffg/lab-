import numpy as np  # 导入数值计算库
import pandas as pd  # 导入表格处理库

# 1. NumPy（矩阵运算，对应实验室线性代数需求）
matrix = np.array([[1,2],[3,4]])  # 建2x2矩阵
print("矩阵乘法：\n", matrix @ matrix)  # 练矩阵运算，对应线性代数基础

# 2. Pandas（处理实验数据表格）
data = pd.DataFrame({
    "作物": ["水稻", "小麦"],
    "亩产": [520, 410],
    "地区": ["成都", "绵阳"]
})
print("数据前2行：\n", data.head())  # 显示数据，实验室读数据常用操作