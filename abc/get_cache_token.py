import abc
class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def walk(self):
        pass
    def get_token(self):
        return abc.get_cache_token()

class B(A):
    def walk(self):
        pass

class C(object):
    pass

print(B().get_token())

A.register(C)

print(B().get_token())
