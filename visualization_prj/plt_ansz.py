import numpy as np
import matplotlib.pyplot as plt
cn,mt,en,pt,ch = np.loadtxt('期末成绩.csv',delimiter=',',usecols=(0,1,2,3,4),unpack=True,skiprows=1,encoding='utf-8')
x = np.arange(1,len(cn)+1)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(11,7))
ax1 = plt.subplot(2,2,1)
ax2 = plt.subplot(2,2,2)
ax3 = plt.subplot(2,2,3)
ax4 = plt.subplot(2,2,4)

#显示各科成绩的累计积分曲线
plt.sca(ax1)
#语文
count_cn, bins_count_cn = np.histogram(cn, bins=len(cn))#频数，间隔
media_count_cn = [(bins_count_cn[i]+bins_count_cn[i+1])/2 for i in range(len(bins_count_cn)-1)]
pdf_cn = count_cn/sum(count_cn)
cdf_cn = np.cumsum(pdf_cn)
plt.plot(media_count_cn,cdf_cn,'b-',linewidth=1,label='语文')
#数学
count_mt, bins_count_mt = np.histogram(mt, bins=len(mt))#频数，间隔
media_count_mt = [(bins_count_mt[i]+bins_count_mt[i+1])/2 for i in range(len(bins_count_mt)-1)]
pdf_mt = count_mt/sum(count_mt)
cdf_mt = np.cumsum(pdf_mt)
plt.plot(media_count_mt,cdf_mt,'g-',linewidth=1,label='数学')
#英语
count_en, bins_count_en = np.histogram(en, bins=len(en))#频数，间隔
media_count_en = [(bins_count_en[i]+bins_count_en[i+1])/2 for i in range(len(bins_count_en)-1)]
pdf_en = count_en/sum(count_en)
cdf_en = np.cumsum(pdf_en)
plt.plot(media_count_en,cdf_en,'r-',linewidth=1,label='英语')
#物理
count_pt, bins_count_pt = np.histogram(pt, bins=len(pt))#频数，间隔
media_count_pt = [(bins_count_pt[i]+bins_count_pt[i+1])/2 for i in range(len(bins_count_pt)-1)]
pdf_pt = count_pt/sum(count_pt)
cdf_pt = np.cumsum(pdf_pt)
plt.plot(media_count_pt,cdf_pt,'y-',linewidth=1,label='物理')
#化学
count_ch, bins_count_ch = np.histogram(ch, bins=len(ch))#频数，间隔
media_count_ch = [(bins_count_ch[i]+bins_count_ch[i+1])/2 for i in range(len(bins_count_ch)-1)]
pdf_ch = count_ch/sum(count_ch)
cdf_ch = np.cumsum(pdf_ch)
plt.plot(media_count_ch,cdf_ch,'k-',linewidth=1,label='化学')
#plt.title('各科成绩的累计积分曲线',fontsize=18)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlabel('分数间隔',fontsize = 10)
plt.ylabel('累计积分',fontsize = 10)
plt.legend(loc = 'lower right',fontsize = 8,numpoints=2)

#文理科平均成绩联合分布散点图
plt.sca(ax2)
#文科个人平均成绩列表
liberature_lst = [(cn[i]+en[i])/2 for i in range(len(en))]
#理科个人平均成绩列表
science_lst = [(mt[i]+pt[i]+ch[i])/3 for i in range(len(en))]
plt.scatter(liberature_lst,science_lst,c = 'r',marker='o')
#plt.title('文理科平均成绩联合分布散点图')
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlabel('文科平均成绩',fontsize = 15)
plt.ylabel('理科平均成绩',fontsize = 15)
plt.xlim(min(liberature_lst)-1,max(liberature_lst)+1)
plt.ylim(min(science_lst)-1,max(science_lst)+1)
#各科成绩分布直方图
plt.sca(ax3)
#语文
bins_cn = np.arange(min(cn),max(cn),0.5)
plt.hist(cn,bins_cn,rwidth=4,color= 'r',label='语文')
#数学
bins_mt = np.arange(min(mt),max(mt),0.5)
plt.hist(mt,bins_mt,rwidth=4,color= 'b',label='数学')
#英语
bins_en = np.arange(min(en),max(en),0.5)
plt.hist(en,bins_en,rwidth=4,color= 'y',label='英语')
#物理
bins_pt = np.arange(min(pt),max(pt),0.5)
plt.hist(pt,bins_pt,rwidth=4,color= 'k',label='数学')
#化学
bins_ch = np.arange(min(ch),max(ch),0.5)
plt.hist(ch,bins_ch,rwidth=4,color= 'g',label='数学')
#plt.title('各科成绩分布直方图',fontsize=15)
plt.xlabel('分数间隔',fontsize=10)
plt.ylabel('成绩频数',fontsize=10)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize = 8,numpoints=2)
#平均成绩优良中差的饼图分布
plt.sca(ax4)
media_all = [(cn[i]+ch[i]+pt[i]+en[i]+mt[i])/5 for i in range(len(en))]
print(media_all)
rank_fig = ['优','良','中','差']
color = ['b','g','r','y']
cnt_rank = list()
cnt = 0
for i in cn:
    if i>=90:
        cnt+=1
cnt_rank.append(cnt)
cnt = 0
for i in cn:
    if i>=80 and i<90:
        cnt+=1
cnt_rank.append(cnt)
cnt = 0
for i in cn:
    if i>=60 and i<80:
        cnt+=1
cnt_rank.append(cnt)
cnt = 0
for i in cn:
    if i<60:
        cnt+=1
cnt_rank.append(cnt)
plt.pie(cnt_rank,labels=rank_fig,colors=color,startangle=0,shadow=True,explode=(0,0.4,0,0.4),autopct='%.lf%%',textprops={'fontsize':15})
#plt.title('平均成绩优良中差的饼图分布',fontsize=15)
plt.show()


