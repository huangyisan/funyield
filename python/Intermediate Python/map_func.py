# import pdb
# def multiply(x):
#     return (x * x)
#
#
# def add(x):
#     return (x + x)
#
#
# funcs = [multiply, add]
# for i in range(5):
#     value = map(lambda y: y(i), funcs)
#     print(list(value))
#     # 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#     #        在python2中map直接返回列表，但在python3中返回迭代器
#     #        因此为了兼容python3, 需要list转换一下

import dis

def addfunc(a,b):
    a+=b
    return a

dis.dis(addfunc)

