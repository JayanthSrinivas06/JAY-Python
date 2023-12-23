# Operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2


    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1,m2)
        
    

    def __gt__(self,other):
        s1tm = self.m1 + self.m2
        s2tm = other.m1 + other.m2

        if s1tm > s2tm:
            return True
        else:
            return False

print('\n___Marks of Student 1___')
a = int(input('Enter marks scored in CSE= '))
b = int(input('Enter marks scored in ECE= '))
print('\n___Marks of Student 2___')
c = int(input('Enter marks scored in CSE= '))
d = int(input('Enter marks scored in ECE= '))
print()

s1 = Student(a,b)
s2 = Student(c,d)

s3 = s1 + s2
print('Average marks in CSE = ', s3.m1/2)
print('Average marks in ECE = ', s3.m2/2)
print()

if s1 >s2:
    print('Student 1 wins!!')
else:
    print('Student 2 wins!!')