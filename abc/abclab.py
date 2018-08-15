from abc import ABC, ABCMeta, abstractmethod
class Base(metaclass=ABCMeta):

    @abstractmethod
    def walk(self):
        pass

    def takl(self):
        pass


    @classmethod
    def __subclasshook__(cls, C):
        if cls is Base:
            if any("foot" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


class human(Base):
    def walk(self):
        print('walk away')

class animal(object):
    footer = 4

class dog(object):
    def __init__(self):
        self.foot = 4
    foot1 = 4
    def foot(self):
        pass

class cat(animal):
    pass

# Base.register(animal)

persion = human()
print(isinstance(persion, Base))
print(issubclass(human, Base))
print(isinstance(dog(), Base))
print(issubclass(dog, Base))
print(isinstance(cat(), Base))
print(issubclass(cat, Base))