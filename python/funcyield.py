import hashlib
import random

def gen_str():
    a = str(random.randint(1, 999))
    return a

def gen_random():
    b = gen_str()
    print(b)
    for i in b:
        yield i

for i in gen_random():
    print(i)