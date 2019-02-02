import string
import random


def gen_code(length):
    a = string.ascii_letters + string.digits
    code = random.sample(a, length)
    return ''.join(code)


print(gen_code(4))

