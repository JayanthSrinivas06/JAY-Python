# Inherits only single class

class Parent:
    def func1(self):
        print('\n __From Parent class__ \n')


class Child(Parent):
    def func2(self):
        print('\n __From child class__ \n')


obj = Child()
obj.func1()
obj.func2()