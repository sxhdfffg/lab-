import pandas as pd
import numpy as np

# 构造模拟的作物数据（所有字段长度统一为90）
crop_data = {
    "作物名称": ["小麦", "水稻", "玉米", "大豆", "棉花", "高粱"] * 15,  # 6*15=90个
    "亩产": np.random.randint(450, 750, size=90),  # 90个
    "种植面积(亩)": np.random.randint(20, 120, size=90),  # 90个
    "地区": ["华北", "华东", "华中", "西北"] * 22 + ["西南", "东北"]  # 4*22+2=90个
}

# 转成DataFrame
df = pd.DataFrame(crop_data)

# 随机加10个空值
df.loc[np.random.choice(df.index, 10), "亩产"] = np.nan

# 保存为CSV
df.to_csv("作物数据.csv", index=False)

print("✅ 模拟数据集已生成！文件名为「作物数据.csv」")