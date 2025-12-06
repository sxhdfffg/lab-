import numpy as np
from scipy.stats import binom

# 贝叶斯推断：模拟实验室实验数据预测（比如作物存活率）
# 先验概率：假设作物存活率0.5
prior_success = 1
prior_failure = 1

# 实验数据：10次种植，8次成功
data_success = 7
data_failure = 3

# 后验概率：更新存活率
posterior_success = prior_success + data_success
posterior_failure = prior_failure + data_failure
survival_rate = posterior_success / (posterior_success + posterior_failure)
print("预测作物存活率：", round(survival_rate, 2))  # 输出0.75，理解贝叶斯核心是更新概率