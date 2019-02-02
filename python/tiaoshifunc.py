# a = [('a', 1), ('a', 2), ('b', 1)]
# 得到 b = [('a', 3),('b', 1)]
from collections import defaultdict
a = [('a', 1), ('a', 2), ('b', 1)]
d = defaultdict(int)
def fn(x):
    d[x[0]]+= x[1]

list(map(fn, a))
print(d)


import pprint
message='Today is 2018.7.11,sunny!'
count={}
for Character in message:
     count.setdefault(Character,0)
     count[Character]=count[Character]+1
pprint.pprint(count)

# 正片如下

a = [('a', 1), ('a', 2), ('b', 1)]
c = {}
def func(x):
    c[x[0]] = c.get(x[0], 0) + x[1]
list(map(func,a))
print(c)

