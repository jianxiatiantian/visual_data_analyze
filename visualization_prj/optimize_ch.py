import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image#图像处理
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
    df = pd.read_excel(url, usecols=uc)
    list1 = list(range(10))
    for i in range(10):
        list1[i] = 0
    for i in df.values:
        j = 0
        for z in space:
            if i[0] < 100:
                if i[0] >= z[0] and i[0]< z[1]:
                    list1[j] += 1
                    break
                j += 1
            else:
                if i[0] >= z[0] and i[0]<= z[1]:
                    list1[j] += 1
                    break
                j += 1

    return list1
list_zone = ['[0,10)','[10,20)','[20,30)','[30,40)','[40,50)',
             '[50,60)','[60,70)','[70,80)','[80,90)','[90,100]']
list_cnt_1 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','C')

list_cnt_2 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','D')

list_cnt_3 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','E')

list_cnt_4 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','F')

list_cnt_5 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','G')

list_cnt_6 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','H')

list_cnt_7 = read('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx','I')
ax1= plt.subplot(1,2, 1)
ax2= plt.subplot(1,2, 2)
data = {'zone':list_zone,'线性代数':list_cnt_1,'英语读写':list_cnt_2,'英语视听说':list_cnt_3,'数据结构':list_cnt_4,'Java程序设计':list_cnt_5,'英语应用能力':list_cnt_6,'管理学':list_cnt_7}
df = pd.DataFrame(data)
df = df.set_index('zone')
colors = ['r','b','y','k','g','m','c']
#颜色可以不指定，df.plot.bar()中会自动配色
#title,label等多个图拼接时不能直接用plt.title(),plt.xlabel(),plt.ylabel(),不然会被以后的标签设置覆盖
#而在matplotlib中图像的标签直接可以用上述示例设置
df.plot.bar(ax = ax1,title = '分组柱状图',xlabel = '分数区间',ylabel = '频数',legend = True,color = colors)
plt.rcParams['font.sans-serif'] = ['SimHei']
#ax1.set_title('name',fontsize = 5)
#设置title字体大小
plt.savefig('image1.jpg')
#各科箱图
df = pd.read_excel('C:\\Users\\30794\\OneDrive\\桌面\\score.xlsx',usecols='C:I')
plt.rcParams['font.sans-serif'] = ['SimHei']
df.plot(kind='box',ax = ax2,title = '各科成绩箱图',ylabel = '成绩',fontsize = 5,grid = True)
#x轴标签逆时针旋转45度
plt.xticks(rotation = 45)
plt.savefig('image2.jpg')
plt.show()



