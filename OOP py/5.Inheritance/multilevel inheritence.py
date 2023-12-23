class Apple:        # Base class(grandparent)
    def func1(self):
        print('From Apple')


class Orange(Apple):    # Intermediate class(parent)
    def func2(self):
        print('From Orange')


class Banana(Orange):   # Derived class(child)
    def func3(self):
        print('From Banana')


print("___From Banana's object___")
fruit1 = Banana()    #-->object created fro Derived class
fruit1.func1()
fruit1.func2()
fruit1.func3() 

print("\n___From Oranges's object___")
fruit2 = Orange()
fruit2.func1()
fruit2.func2()
# cant access contents in its child class(Banana)

print("\n___From Apple's object___")
fruit3 = Apple()
fruit3.func1()
# cant access contents in its children classes(Orange and Banana)

print()