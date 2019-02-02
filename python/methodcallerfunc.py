from operator import methodcaller
s = 'the time has come'
upcase = methodcaller('upper')
# 其实是使用的str.upper(s)
print(upcase(s))

# 创建replace的函数，但强行指定了第一个参数为' ',替换的字符串为'-'
hiphenate = methodcaller('replace',' ','-')
print(hiphenate(s))