import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Series1': [1, 2, 3, 4, 5],
    'Series2': [2, 3, 5, 7, 11],
    'Series3': [10, 15, 12, 13, 10]
}
df = pd.DataFrame(data)

# 设置Category为索引（可选，但可以使图形更清晰）
df = df.set_index('Category')

# 绘制分组柱状图
df.plot.bar()

# 添加标题和标签
plt.title('Grouped Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')

# 显示图例
plt.legend()

# 显示图形
plt.show()