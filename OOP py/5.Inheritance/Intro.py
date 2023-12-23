class A:    # Parent  class
    x = 'Something'

class B(A):     # B(A)-->here A is inherited into B , so B is a child class
    y = 'Nothing'


obj = B()   # object created
print(obj.x)    #-->B class has right to access things in class A but not viseversa
print(obj.y)

obj1 = A()
print(obj1.x)
print(obj1.y)   #-->we cannot access B by using object of A , even if B inherits from A