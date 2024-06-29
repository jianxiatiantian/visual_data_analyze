import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建两个示例DataFrame，每个都包含坐标数据
df1 = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})

df2 = pd.DataFrame({
    'x': np.random.rand(100) + 1,  # 为了区分，稍微偏移x坐标
    'y': np.random.rand(100)
})

# 创建一个图形和两个子图
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# 在第一个子图上绘制第一个DataFrame的数据
axs[0].scatter(df1['x'], df1['y'], label='DataFrame 1')
axs[0].set_title('DataFrame 1 Plot')
axs[0].legend()

# 在第二个子图上绘制第二个DataFrame的数据
axs[1].scatter(df2['x'], df2['y'], label='DataFrame 2')
axs[1].set_title('DataFrame 2 Plot')
axs[1].legend()

# 显示图形
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()