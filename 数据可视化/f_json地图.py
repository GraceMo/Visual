import json
from pygal_maps_world.i18n import COUNTRIES   # 2位数国别码--字典形式
import pygal
from pygal.style import LightColorizedStyle as LCS
file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

def get_country_code(country_name):
    '''根据国家名匹配二位数的国别码'''
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

country_dict = {}  #{'国别名':'population',...}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict["Country Name"]
        # 带小数点的字符串不能转为整数类型,需要float作为中介
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            country_dict[country_code] = population
print(len(country_dict))

count_dic1,count_dict2,count_dic3,count_dic4 = {},{},{},{}
for code,population in country_dict.items():
    '''按人口分组'''
    if population < 10000000:
        count_dic1[code] = population
    elif population < 500000000:
        count_dict2[code] = population
    elif population < 1000000000:
        count_dic3[code] = population
    else:
        count_dic4[code] = population
print(len(count_dic1),len(count_dict2),len(count_dic3),len(count_dic4),)
'''使用RotateStyle样式来调整颜色,提供一个16进制rgb颜色,前2未代表红色,中间g,后b,
LightColorizedStyle(LCS)加亮整个地图的颜色
'''
wm_style = pygal.style.RotateStyle('#336699',base_style=LCS) #返回一个样式对象
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010,by Country'

wm.add('0-10m',count_dic1)
wm.add('10m-50m',count_dict2)
wm.add('50m-100m',count_dic1)
wm.add('>100m',count_dic4)

wm.render_to_file('world_population.svg')



