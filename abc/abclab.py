from abc import ABC, ABCMeta, abstractmethod
class Base(metaclass=ABCMeta):

    @abstractmethod
    def walk(self):
        pass

    def takl(self):
        pass


    @classmethod
    def __subclasshook__(cls, C):
        if cls == Base:
            if any("foot" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


class human(Base):
    def walk(self):
        print('walk away')

class animal(object):
    def __init__(self):
        self.foot = 4
    foot1 = 4
    def foot(self):
        pass


# Base.register(animal)

persion = human()
print(isinstance(persion, Base))
print(issubclass(human, Base))
print(isinstance(animal(), Base))