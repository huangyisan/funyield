from functools import reduce
from operator import mul
def fact(n):
    return reduce(lambda x,y:x*y, range(1,n+1))
print(fact(10))


def factmul(n):
    return reduce(mul, range(1, n+1))
print(factmul(10))