import matplotlib.pyplot as plt
x_values = list(range(1,10001,300))
y_values = list(map(lambda x:pow(x,2),x_values))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,s=20,edgecolors='black',c='red')  # 设置散点边沿颜色black,中心颜色red
'''使用颜色映射,用于突出数据的规律,(颜色渐变)
将c设置为y值列表,使用camp参数告诉pyplot使用哪个颜色映射'''
plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Blues,edgecolors='None',s=40)

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

# plt.tick_params(axis='both',which='major',labelsize=14)
plt.tick_params([0,1100,0,1100000])  # 设置x,y轴的取值范围

# plt.show()
plt.savefig('散点.png',bbox_inches = 'tight')