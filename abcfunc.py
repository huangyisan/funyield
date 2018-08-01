import abc
from abc import abstractmethod
class MyABC(metaclass=abc.ABCMeta):
    def abc_method(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        return True

    # 存在该装饰器的，则子类对象必须进行实例化，否则报错
    @abstractmethod
    def do_somethng(self):
        print('yes')


class C(object):
    def abc_method(self):
        print('it is abc method')
    #
    # def do_somethng(self):
    #     print('good')
    pass



# typical client code
c = C()
if isinstance(c, MyABC):  # will be true
    c.abc_method()  # raises AttributeError
else:
    print('not')


