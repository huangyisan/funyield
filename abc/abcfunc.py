from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    def my_normal_method(self):
        pass

    @abstractmethod
    def my_abstract_method(self):
        pass

class B(A):
    pass

class C(A):
    def my_abstract_method(self):
        pass


C()