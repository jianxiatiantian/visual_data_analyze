'''import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,11)
y = 11 - x
plt.bar(x,y)
for xx,yy in zip(x,y):
    plt.text(xx-0.2,yy+0.1,'%2d'%yy)
plt.show()
'''

'''
import pandas as pd
import matplotlib.pyplot as plt

# 创建一个简单的DataFrame
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': [10, 15, 7, 20, 12]}
df = pd.DataFrame(data)

# 使用matplotlib的pyplot模块
# plt.figure(figsize=(10, 6))  # 设置图像大小
df.plot(kind='bar', x='Category', y='Values', color='blue')  # 使用pandas的plot方法绘制柱状图
plt.title('Bar Chart Example')  # 设置标题
plt.xlabel('Category')  # 设置x轴标签
plt.ylabel('Values')  # 设置y轴标签
plt.grid(True)  # 显示网格线
plt.show()  # 显示图像
'''
import pandas as pd
import matplotlib.pyplot as plt

def read_and_plot(url, column, color, label):
    space = [[0,10],[10,20],[20,30],[30,40],[40,50],
             [50,60],[60,70],[70,80],[80,90],[90,100]]
    list2 = [(space[t][0]+space[t][1])/2 for t in range(10)]

    df = pd.read_excel(url, usecols=column)
    list1 = [0] * 10

    for i in df.values:
        for j, z in enumerate(space):
            if i[0] >= z[0] and i[0] < z[1]:
                list1[j] += 1
                break

    data = {'A': list2, f'B_{label}': list1}
    return pd.DataFrame(data)

# 初始化一个空的DataFrame来保存所有课程的数据
all_data = pd.DataFrame()

# 为每个课程读取和绘制数据
courses = ['C', 'D', 'E', 'F', 'G', 'H', 'I']
colors = ['blue', 'r', 'g', 'c', 'm', 'k', 'y']  # 使用黄色代替白色
for i, (course, color) in enumerate(zip(courses, colors)):

    df = read_and_plot('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx', course, color, courses[i])
    all_data = pd.concat([all_data, df], axis=1)

# 绘制柱状图
plt.rcParams['font.sans-serif'] = ['SimHei']
all_data.set_index('A').plot(kind='bar', color=colors, legend=True)
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.grid(True)
plt.show()
