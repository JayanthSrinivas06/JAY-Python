class Student:
    college = 'VIT-AP University'
    def __init__(self):
        self.marks1 = 'CSE'
        self.marks2 = 'ECE'
        self.marks3 = 'Maths'

    # Instance Method
        #for marks1
    def get_m1(self):   # == get method created == (**also called as Accessors**)
        print('Marks in CSE   :', self.marks1)
    
    def set_m1(self,value):     # == set method created == (**also called as Mutators**)
        self.marks1 = value


        #for marks2
    def get_m2(self):
        print('Marks in ECE   :', self.marks2)
    
    def set_m2(self,value):
        self.marks2 = value


        #for marks3
    def get_m3(self):
        print('Marks in MATHS :', self.marks3 , '\n')
    
    def set_m3(self,value):
        self.marks3 = value

    # Class Method
    @classmethod    # this decorator is used in class method    
    def get_college(cls):        # only 'cls' argument is used in class method
        return cls.college
    
    # Static Method
    @staticmethod   # as argument(self,etc..)didn't used here,some compilers may show error,so this decorator is used to show that it is static method
    def sayHello():     # we may or maynot use arguments in static methods
        print('Hello User')


Student.sayHello()
print('college name :', Student.get_college() , '\n')

s1 = Student()
s2 = Student()

print('***Enter marks for Student1***')
cse1 = int(input('Marks in CSE ='))
ece1 = int(input('Marks in ECE ='))
mat1 = int(input('Marks in MATHS ='))

print('\n***Enter marks for Student2***')
cse2 = int(input('Marks in CSE ='))
ece2 = int(input('Marks in ECE ='))
mat2 = int(input('Marks in MATHS ='))

s1.set_m1(cse1)
s1.set_m2(ece1)
s1.set_m3(mat1)

s2.set_m1(cse2)
s2.set_m2(ece2)
s2.set_m3(mat2)

print('\n___Student 1 Marks___')
s1.get_m1()
s1.get_m2()
s1.get_m3()

print('___Student 2 Marks___')
s2.get_m1()
s2.get_m2()
s2.get_m3()