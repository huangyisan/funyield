# a = [('a', 1), ('a', 2), ('b', 1)]
# 得到 b = [('a', 3),('b', 1)]
from functools import reduce
a = [('a', 1), ('a', 2), ('b', 1)]
y = {}
def add_dictA(x):
    y.update({x[0]:y.get(x[0],0)+x[1]})
    return y
map(add_dictA, a)
print(y)
list(map(add_dictA, a))
print(y)
# def add_dict(x):
#     y = {}
#     for i in x:
#         y.update({i[0]:y.get(i[0],0)+i[1]})
#     return y
# print(add_dict(a))

# def change_tuple(y):
#     list_b = []
#     for k,v in y.items():
#         list_b.append((k,v))
#     return list_b
#
# print(change_tuple(add_dict(a)))



