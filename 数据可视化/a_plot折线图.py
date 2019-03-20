'''matplotlib
数学绘图库,绘制简单的图标,折线图,散点图'''
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#添加数据,x轴为input_values,以1开始,y轴为squares,以0开始,linewidth线条粗细
plt.plot(input_values,squares,linewidth=3)
#设置标题&标签
plt.title('Square Numbers',fontsize = 24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)
#设置刻度
plt.tick_params(axis='both',labelsize = 14)
# plt.show()
plt.savefig('折线.png',bbox_inches = 'tight')