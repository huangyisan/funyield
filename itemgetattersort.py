from operator import itemgetter
metro_data = [
    ('Tokey', 'JP',111),
    ('Bokey', 'CP',121),
    ('Zokey', 'XP',101),
]

# print(sorted(metro_data,key=lambda x:x[0]))
#
#
# print(sorted(metro_data,key=itemgetter(0)))

cc_name = itemgetter(0,1) #只提取两个元素
for city in metro_data:
    print(cc_name(city))