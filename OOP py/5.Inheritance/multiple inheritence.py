# Inhertis 2 or more  classes

class Mother:   # Parent class
    mother_name = ''
    def mom(self):
        print(self.mother_name)


class Father:   # Parent class
    father_name = ''
    def dad(self):
        print(self.father_name)


class Son(Mother,Father):   # Child class
    son_name = ''
    def showNames(self):
        print('\n',self.son_name, ', s/o Mr. & Mrs.', self.mother_name , '-' , self.father_name , '\n')


obj = Son()

obj.son_name = 'Jayanth'
obj.mother_name = 'Vijaya'
obj.father_name = 'Venkat'

obj.showNames()