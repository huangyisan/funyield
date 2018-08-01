import datetime
import functools

def timefunc(func):
    def warrap(*args, **kwargs):
        now = datetime.datetime.now()
        func()  # 执行传入的func
        last = datetime.datetime.now()
        print(last - now)
    return warrap

@timefunc  # 将下面的callfun1函数传入到timefunc这个函数里面
def callfun1():
    print('this is callfun1 func')

# 调用callfun1的时候，先讲callfun1传入到timefunc里面，然后执行timefunc函数，先获得now的值，然后调用func()，因为这个是传入的callfun1，所以执行callfun1()函数，得到结果，然后在得到last的值，再打印出last-now的值
callfun1()



def timecan(flag):  # flag是参数
    def decorator(func): # 这个是装饰器
        @functools.wraps(func) # 使用这个装饰器为了避免函数的__name__属性值变成“wrapper”
        def wrapper(*args, **kwargs):
            if flag:
                now = datetime.datetime.now()
                func()
                last = datetime.datetime.now()
                print(last - now)
        return wrapper  # return的是函数
    return decorator  # return的是函数

@timecan(1)
def callfun():
    print('this is callfun func')

callfun()



