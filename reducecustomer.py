from functools import reduce
from operator import mul,add

def fact(n):
    return reduce(mul, range(1,n))

print(fact(4))