from functools import reduce
from operator import mul,iadd
def fact(n):
    return reduce(lambda x,y:x*y, range(1,n+1))
print(fact(10))


def factmul(n):
    return reduce(mul, range(1, n+1))
print(factmul(10))



def addadd(n):
    return reduce(iadd, range(1,n+1))
print(addadd(100))