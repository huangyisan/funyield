# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    def devide(s):
        return s.split('.')
    # return devide(s)
    # return reduce(lambda x, y: x*1 + y*0.001, map(int, devide(s)))
    return reduce(lambda x, y: x*1 + y*(0.1**len(devide(s)[-1])), map(int, devide(s)))

print('str2float(\'123.4561\') =', str2float('123.4561'))
if abs(str2float('123.4561') - 123.4561) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')