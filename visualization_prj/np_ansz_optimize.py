import numpy as np
les_name = ['语文','数学','英语','物理','化学']
j = 0
print('科目  ','算术平均数 ','方差 ','中位数  ','最大值 ','最小值')
for i in np.loadtxt('期末成绩.csv',delimiter=',',usecols=(0,1,2,3,4),unpack=True,skiprows=1,encoding='utf-8'):
    print(les_name[j],end='   ')

    print('%8.2f'%np.mean(i),end='')

    #
    print('%6.2f'%np.var(i),end='')

    #
    print('%7.2f'%np.median(i),end=' ')

    #
    print('%7.2f'%np.max(i),end=' ')

    #
    print('%6.2f'%np.min(i))

    j+=1
