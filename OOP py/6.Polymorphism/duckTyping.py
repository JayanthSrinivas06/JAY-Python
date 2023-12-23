# Duck typing
# If it looks like a Duck and Quacks like a duck.Then,it is a Duck

class Duck:
    def sound(self):
        print('\nDuck Quacks\n')


class Dog:
    def sound(self):
        print('Dog barks\n')


class Cat:
    def sound(self):
        print('Cat meows\n')


def anySound(obj):      # This method can take any value as it is now able to polymorph     
    obj.sound()

x = Duck()
y = Dog()
z = Cat()
anySound(x)
anySound(y)
anySound(z)
