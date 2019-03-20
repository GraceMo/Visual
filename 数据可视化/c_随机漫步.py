'''随机生成一个点的坐标'''
import matplotlib.pyplot as plt
from random import choice
'''得到数据'''
class RandonWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points  #设置最大数目
        self.x_values = [0]  # x 坐标
        self.y_values = [0]
    def fill_walk(self):
        '''得到随机漫步所有的点'''
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:#拒绝原地踏步
                continue
            next_x = self.x_values[-1] + x_step  # 计算点在x轴上的坐标
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
    def get_step(self):
        '''确定每次漫步的距离和方向'''
        direction = choice([1, -1])  # 方向
        distance = choice([0, 1, 2, 3, 4])  # 步幅
        step = direction * distance
        return step
'''数据可视化'''
while True:
    rw = RandonWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=15,c=rw.x_values,cmap=plt.cm.Purples)  #设置颜色映射
    '''设置起点/终点'''
    plt.scatter(0,0,s=100,c='green',edgecolors='None')
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='red')
    '''隐藏坐标轴'''
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    '''调整图表尺寸'''
    plt.figure(figsize=(16,9),dpi=128)
    plt.show()
    keep_running = input('continue?(y/n): ')
    if keep_running == 'n':
        break


