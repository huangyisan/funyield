from operator import attrgetter
from collections import namedtuple
metro_data = [
    ('Tokey', 'JP', 111, (100,113)),
    ('Bokey', 'CP', 121, (110,124)),
    ('Zokey', 'XP', 101, (98,110)),
]

# nametuple，用于指定metro_data中最后一个元组的模板，所有的内容都是参数，后面循环对其进行赋值
data_range = namedtuple('data_range', 'start end')
# 用于指定metro_data全部元素的模板，prange其实是data_range
data_areas = namedtuple('data_areas', 'name shortname price prange')

# 生成list信息。这里面data_range和data_areas嵌套了。 prange就是data_range(start,end)。
# 循环的时候，让(start,end)进行赋值metro_data最后一位的元组
data_info = [data_areas(name, shortname, price, data_range(start,end)) \
             for name,shortname, price,(start,end) in metro_data]

# data_areas(name='Tokey', shortname='JP', price=111, prange=data_range(start=100, end=113))
print(data_info[0])
# 100， 获得data_info的0号位数据的prange这个参数的值对应的内部的start的值。也就是100
print(data_info[0].prange.start)

# 定义一个data_name,其生成的方式是需要，name这个参数的值和prange.start的值
data_name = attrgetter('name', 'prange.start')

# 遍历循环，循环的是data_info,根据key排序，排序的依据是prange.start参数对应的值。
for city in sorted(data_info, key=attrgetter('prange.start')):
    print(data_name(city))