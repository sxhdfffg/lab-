import sqlite3
import pandas as pd

# 连接SQL数据库（实验室连接数据库的标准操作）
conn = sqlite3.connect("test.db")

# 用Pandas读取SQL数据
df = pd.read_sql("SELECT * FROM crops", conn)
print("从SQL读取的数据：\n", df)

# 向SQL写入新数据
new_data = pd.DataFrame({"id": [3], "name": ["玉米"], "yield_kg": [620], "area": ["德阳"]})
new_data.to_sql("crops", conn, if_exists="append", index=False)

# 再次查询，验证写入成功
df_new = pd.read_sql("SELECT * FROM crops", conn)
print("写入后的数据：\n", df_new)