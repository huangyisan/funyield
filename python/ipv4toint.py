'''a   b  c  d'''
" 123. 1. 2. 1"
'''
a:256*256*256*a
b:256*256*b
c:256*c
d:d

a*256*256*256 + b*256*256 + c*256 +d

256*(a*256*256+b*256+c)+d

256*(256*(256*a+b)+c)+d

256*a+b

lambada 256*x.y:256*x+y

'''
from functools import reduce

def devide(x):
    return x.split('.')

ipv4 = ['123', '1', '2', '1']

list("123.1.2.1".split('.'))[::-1]

map(int,list("123.1.2.1".split('.'))[::-1])



16908667

reduce(lambda x,y:x*256+y, map(int,list("123.1.2.1".split('.'))))

# 前两位数据 513
reduce(lambda x,y:x*256+y, map(int,list("123.1.2.1".split('.'))[2:4]))


# 第三位数据 66049
map(int,list("123.1.2.1".split('.')))[-3]

reduce(lambda x,y:x*256**2+y, [map(int,list("123.1.2.1".split('.')))[1],reduce(lambda x,y:x*256+y, map(int,list("123.1.2.1".split('.'))[2:4]))])

# 第四位数据
map(int,list("123.1.2.1".split('.')))[-4]

ipv4 = "1.1.1.1"
reduce(lambda x,y:x*256**3+y, [list(map(int,list(ipv4.split('.'))))[0], reduce(lambda x,y:x*256**2+y, [list(map(int,list(ipv4.split('.'))))[1],reduce(lambda x,y:x*256+y, list(map(int,list(ipv4.split('.'))[2:4])))])])

reduce(lambda x,y:x*256**2+y,[map(int,list("123.1.2.1".split('.')))[-3],reduce(lambda x,y:x*256+y, map(int,list("123.1.2.1".split('.'))[-3:-1]))])


reduce(lambda x,y:x*256**3+y, [123,65794])

reduce(lambda x,y:x*256*256+y, [reduce(lambda x,y:x*256+y, map(int,list("123.1.2.1".split('.'))[-3:-1])),map(int,list("123.1.2.1".split('.')))[-3]])

reduce(lambda x,y:x*256*256*256 + y, )

map(int,list("123.1.2.1".split('.'))[0:2])