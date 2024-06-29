import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
import math
#统计信息
df = pd.read_excel('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx',usecols='C:I')
df['平均数'] = df.mean(axis = 1)
df['总成绩'] = df.sum(axis = 1)
df['标准差'] = df.std(axis = 1)
df1 = df.sort_values(by=['总成绩'],ascending=False)
df1.to_excel('C:\\Users\\30794\\OneDrive\\桌面\\score1.xlsx',index = False)
#相关系数
df2 = pd.read_excel('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx',usecols='C:I')
print("所有课程之间的相关系数:\n",df2.corr())


def read(url,uc):
    space = [[0,10],[10,20],[20,30],[30,40],[40,50],
             [50,60],[60,70],[70,80],[80,90],[90,100]]
    list2 = list(range(10))
    for t in range(10):
        list2[t] = (space[t][0]+space[t][1])/2

    df = pd.read_excel(url, usecols=uc)
    list1 = list(range(10))
    for i in range(10):
        list1[i] = 0
    for i in df.values:
        j = 0
        for z in space:
            if i[0] >= z[0] and i[0]< z[1]:
                list1[j] += 1
                break
            j += 1
    data = {'A':list2,'B':list1}
    dfx = pd.DataFrame(data)
    return dfx
df3= read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','C')
df3.plot(kind = 'bar',x='A',y='B',color='blue',label = '线性代数')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df4 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','D')
df4.plot(kind = 'bar',x='A',y='B',color='r',label = '英语读写')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df5 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','E')
df5.plot(kind = 'bar',x='A',y='B',color='g',label = '英语视听说')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df6 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','F')
df6.plot(kind = 'bar',x='A',y='B',color='c',label = '数据结构')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df7 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','G')
df7.plot(kind = 'bar',x='A',y='B',color='m',label = 'Java程序设计')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df8 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','H')
df8.plot(kind = 'bar',x='A',y='B',color='k',label = '英语应用能力')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.grid(True)
df9 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','I')
df9.plot(kind = 'bar',x='A',y='B',color='y',label = '管理学')
plt.title('分数柱状图')
plt.xlabel('分数区间')
plt.ylabel('频数')
plt.rcParams['font.sans-serif'] = ['SimHei']


plt.grid(True)
plt.show()



'''


plt.xlabel('')
'''


