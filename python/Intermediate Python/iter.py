

class Test(object):
    def funcA(self):
        pass

    # def __iter__(self):
    #     pass

print(hasattr('ccc','__iter__') or hasattr('ccc','__getitem__'))
print(hasattr(Test,'__iter__') or hasattr(Test,'__getitem__'))
a = (i for i in range(10))
print(a)
print(hasattr(a,'__next__'))

# def gen():
#     for i in range(10):
#         yield i
#     # return (i for i in range(10))
#
# for i in gen():
#     print(i)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
for i in fibon(100):
    print(i)