import matplotlib.pyplot as plt
import numpy as np

close_price = np.loadtxt('stock.csv',delimiter = ',',usecols=(4,),unpack = True,skiprows=1)

x = np.arange(len(close_price))
plt.plot(x,close_price,'r-')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.title('股票收盘走势',fontsize = 20)
plt.xlabel('时间顺序',fontsize = 15)
plt.ylabel('收盘价',fontsize = 15)
plt.xlim(0.0,max(x)+1)
plt.ylim(min(close_price)-1,max(close_price)+1)
plt.show()
