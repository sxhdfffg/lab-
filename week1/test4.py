import pandas as pd

def filter_high_yield(data_path, threshold):
    # 定义函数：读取数据，筛选亩产超过阈值的作物
    df = pd.read_csv(data_path)
    return df[df["亩产"] > threshold]

# 调用函数（模拟实验室调用代码）
result = filter_high_yield("作物数据.csv", 450)
print("亩产超450kg的作物：\n", result)