import hashlib
import random

def gen_random():
    a = str(random.randint(1,999))
    print(a)
    for i in a:
        yield i

for i in gen_random():
    print(i)