from abc import ABCMeta

class Sized(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
            # else:
            #     return False
        return NotImplemented

class A(Sized):
    pass

class B(Sized):
    def __len__(self):
        return 0

print(issubclass(A, Sized))  # True - should be False
print(issubclass(B, Sized))  # True

print(A.__mro__)