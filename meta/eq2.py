class A:
    def __lt__(self, a):
        return NotImplemented

    def __add__(self, a):
        return NotImplemented
A() < A()