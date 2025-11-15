import pandas as pd
# 读取数据（实验室读实验数据的标准操作）
df = pd.read_csv("作物数据.csv")
print("原始数据行数：", len(df))

# 数据清洗：删除空值（实验室处理数据第一步）
df_clean = df.dropna()
print("清洗后行数：", len(df_clean))

# 筛选数据：亩产>500的作物（实验室数据分析常用）
high_yield = df_clean[df_clean["亩产"] > 500]
print("高产作物：\n", high_yield)