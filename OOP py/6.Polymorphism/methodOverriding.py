# Method overriding
# overriding a class function over another class like child class executes over parent class

class Parent:
    def Bike(self):
        print('\nI have a Royal Enfield Bike\n')


class Child(Parent):
    def Bike(self):
        print('\nI have a Yamaha Bike\n')
    pass
"""if you comment the above method in child class output comes as in the parent class,so its a practical example of parent and child
    bike of parents belongs to child,but if child has bike he would show his own bike if he has,if he didn't own one,he shows his parent's bike though"""
# it is called overriding and as it is occuring btwn methods,its called as METHOD OVERRIDING

   
obj = Child()
obj.Bike()

