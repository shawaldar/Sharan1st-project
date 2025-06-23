from abc import ABC, abstractmethod
class parent (ABC):
    @abstractmethod
    def method_one(self):
        pass
    @abstractmethod
    def method_two(self):
        pass
class child (parent):
    def method_one(self):
        print('Welcome to ABC class')
    def method_two(self):
        print('Welcome to Evolent class')
obj=child()
obj.method_two()


