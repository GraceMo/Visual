import pygal
from random import randint
'''获取数据'''
class Dice():
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)
def frequen():
    dice1 = Dice()
    dice2 = Dice()
    dice3 = Dice()
    results = []
    for roll_num in range(1000):
        result = dice1.roll()+dice2.roll()+dice3.roll()
        results.append(result)
    frequences = []
    for num in range(3,dice1.num_sides*3+1):
        frequence = results.count(num)
        frequences.append(frequence)
    return frequences
frequences1 = frequen()
frequences2 = frequen()
frequences3 = frequen()
'''绘制直方图'''
hist = pygal.Bar()
hist.title = 'Results of rolling Three D6 1000 times'
hist.x_labels = list(range(3,19))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
'''添加三组数据'''
hist.add('D6*1', frequences1)
hist.add('D6*2', frequences2)
hist.add('D6*3', frequences3)
hist.render_to_file('dice_visual.svg')



