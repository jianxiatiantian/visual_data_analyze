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

# 绘制堆叠柱状图
df.set_index('Category').plot.bar(stacked=True)

# 添加标题和标签
plt.title('Stacked Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')

# 显示图例
plt.legend()

# 显示图形
plt.show()