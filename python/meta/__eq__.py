class A(object):
    def test(self):
        pass

a = A()
b = a
print(id(a))
print(id(b))
a.value = 1
print(id(a))
print(b.value)
