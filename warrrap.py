import datetime
import functools

def timefunc(func):
    def warrap(*args, **kwargs):
        now = datetime.datetime.now()
        func()
        last = datetime.datetime.now()
        print(last - now)
    return warrap

@timefunc
def callfun1():
    print('this is callfun1 func')

callfun1()



def timecan(flag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if flag:
                now = datetime.datetime.now()
                func()
                last = datetime.datetime.now()
                print(last - now)
        return wrapper
    return decorator

@timecan(1)
def callfun():
    print('this is callfun func')

callfun()



