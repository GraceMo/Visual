'''csv文件将数据作为一系列以逗号分隔的值写入文件'''
'''读取csv文件'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime
'''数据'''
file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f) #创建一个阅读器对象存储在reader中
    header_row = next(reader)  # 单行读取,读取文件头
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    highs,dates,lows = [],[],[]
    i = 0
    for row in reader:   # 获取最高温度
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            dates.append(current_date)# 日期
            highs.append(int(row[1]))  #温度
            lows.append(int(row[3]))
        except Exception:
            print(current_date,': miss data')
        else:
            i += 1
    # print(highs)
print('data counts :',i)
'''绘制图形'''
fig = plt.figure(dpi=128,figsize=(10,6))  #设置显示大小

plt.plot(dates,highs,c='red',alpha=0.5)  #在前为x轴,后为y
plt.plot(dates,lows,c='blue',alpha=0.5)  #添加最低温度
plt.fill_between(dates,lows,highs,alpha=0.1)  # 图表中间区域着色,alpha颜色透明度,0完全透明,1(默认)完全不透明

fig.autofmt_xdate()   # 绘制斜的日期标签
plt.title('Daily high&low temperatures 2014',fontsize=24)
plt.xlabel('Date',fontsize=14)
plt.ylabel('Temperature/F',fontsize=16)
plt.tick_params(axis='both',which = 'major',labelsize=16)
'''设置主刻度大小,
which一共3个参数[‘major’ ， ‘minor’ ，‘both’] 
默认是major表示主刻度，后面分布为次刻度及主次刻度都显示'''
plt.show()















